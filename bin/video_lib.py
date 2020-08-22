# video_lib.py

import subprocess
import os

from pytube import YouTube
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

credential_path = f"/home/nick/Desktop/videolib-869de019615c.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

_PATH_TO_VIDEOS = f"../videos/"
_PATH_TO_AUDIO_FILES = f"../audio_files/"

class VideoLib:
    def __init__(self):
        # Get ourselves a speech client to make calls to the server
        self.speech_client = speech_v1.SpeechClient()

        # The language of the supplied audio should be American English
        self.language_code =  "en-US"


    def download_youtube_video_from_uri(self, uri: str, folder_name: str, file_name: str) -> None:
        yt = YouTube(uri)
        stream = yt.streams.filter(subtype='mp4').first()
        stream.download(_PATH_TO_VIDEOS + folder_name)
        os.rename(_PATH_TO_VIDEOS + folder_name + f"/" + yt.title + ".mp4", _PATH_TO_VIDEOS + folder_name + f"/" + file_name)


    def convert_mp4_to_wav(self, folder_name: str, mp4_name: str, wav_name: str):
        path_to_mp4 = _PATH_TO_VIDEOS + folder_name + f"/" + mp4_name
        path_to_wav_folder = _PATH_TO_AUDIO_FILES + folder_name 
        path_to_output_wav = path_to_wav_folder + f"/" + wav_name
       
        if not os.path.exists(path_to_wav_folder):
            os.makedirs(path_to_wav_folder)

        command = f"ffmpeg -i {path_to_mp4} -ab 160k -ac 2 -ar 44100 -vn {path_to_output_wav}" 
        subprocess.call(command, shell=True)