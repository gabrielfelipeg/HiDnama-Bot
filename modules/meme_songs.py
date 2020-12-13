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
    Store, load, download and handle MemeSongs.
    """

    def __init__(self, songs=[]):
        """
        Create a MemeSongs object, where self.songs are all meme songs loaded.
        
        Keyword arguments:
            songs -- A list of songs that has been loaded previously. (default: [])

        Return:
            None
        """
        self.songs = songs
        self._setup()

    
    def _setup(self):
        """
        Used to start a thread to download the meme songs while
        bot start his other functions.
        
        Keyword arguments:
            None

        Return:
            None
        """   
        print("Downloading meme songs...")
        downloader = threading.Thread(target=self.download, daemon=True)
        downloader.start()

    def _connect_googledrive(self):
        """
        Start connection with GoogleDrive API, need to use token.pickle
        key and if not exist, create it.
        
        Keyword arguments:
            None

        Return:
            service -- The connection with GoogleDrive API.
        """
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
        """
        Use a GoogleDrive API connection to download
        memes songs stored there.
        
        Keyword arguments:
            None

        Return:
            None
        """
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
