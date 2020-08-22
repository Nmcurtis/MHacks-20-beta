# video_lib.py

import os

from pytube import YouTube
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

credential_path = f"/home/nick/Desktop/videolib-869de019615c.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

_PATH_TO_VIDEOS = f"/videos"

class VideoLib:
    def __init__(self):
        # Get ourselves a speech client to make calls to the server
        self.speech_client = speech_v1.SpeechClient()

        # The language of the supplied audio should be American English
        self.language_code =  "en-US"


    def download_youtube_video_from_uri(self, uri: str, file_name: str):
        yt = YouTube(uri)
        
        

    
