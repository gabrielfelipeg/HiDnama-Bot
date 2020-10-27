from __future__ import print_function
import os
import pickle
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

def connect_googledrive():
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

def try_download():
    service = connect_googledrive()

    all_songs = []

    if not os.path.exists('assets/'):
        os.system('mkdir assets')
    with open('meme_songs.list') as fd:
        for line in fd:
            line = line.split(' ')

            file_id = line[0]
            name_file = line[1].split('\n')[0]
            
            if not os.path.exists('assets/' + name_file):
                request = service.files().get_media(fileId=file_id)
                fh = open('assets/' + name_file, "wb")
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print ("Song {} Download {}%.".format(name_file, int(status.progress() * 100)))

                fh.close()
            all_songs.append('assets/' + name_file)

    return all_songs