from __future__ import print_function
import os
import pickle
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload
import threading


class MemeSongs(object):
    """
    Store and handle MemeSongs access and loading
    """

    def __init__(self, songs=[]):
        self.songs = songs
        self._setup()

    def _setup(self):
        print("Downloading meme songs...")
        downloader = threading.Thread(target=self.download, daemon=True)
        downloader.start()

    def _connect_googledrive(self):
        SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)
        return service

    def download(self):
        SERVICE = self._connect_googledrive()
        ASSETS_DIR = 'assets/'
        MEME_SONG_LIST = 'meme_songs.list'

        if not os.path.exists(ASSETS_DIR):
            os.system('mkdir assets')

        def _extract_song_info(line):
            line = line.split(' ')
            file_id = line[0]
            file_name = line[1].split('\n')[0]
            return (file_id, file_name)

        with open(MEME_SONG_LIST) as fd:
            for line in fd:
                file_id, file_name = _extract_song_info(line)
                song_file_path = f"{ASSETS_DIR}{file_name}"

                if not os.path.exists(song_file_path):
                    request = SERVICE.files().get_media(fileId=file_id)
                    with open(song_file_path, "wb") as song_file:
                        downloader = MediaIoBaseDownload(song_file, request)
                        done = False
                        while not done:
                            status, done = downloader.next_chunk()
                            print("Song {} Download {}%.".format(
                                file_name, int(status.progress() * 100)))

                self.songs.append(song_file_path)
        print("Download finish!")
