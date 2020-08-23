# video_lib.py

import subprocess
import json
import os

from pytube import YouTube
from google.protobuf.json_format import MessageToJson
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

credential_path = f"/home/nick/Desktop/videolib-869de019615c.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

_PATH_TO_VIDEOS = f"../videos/"
_PATH_TO_AUDIO_FILES = f"../audio_files/"
_PATH_TO_TRANSCRIPT_FILES = f"../transcripts/"

class VideoLib:
    def __init__(self):
        # Get ourselves a speech client to make calls to the server
        self.speech_client = speech_v1.SpeechClient()

        # The language of the supplied audio should be American English
        self.language_code =  "en-US"

        # We expect audio samples to have a sample rate of 44100 Hertz
        self.sample_rate_hertz = 44100

        # We expect two audio channels in our audio samples:
        self.audio_channel_count = 2

        # The transcript of the most recent call to the text to speech hook:
        self.latest_result = None


    def download_youtube_video_from_uri(self, uri: str, folder_name: str) -> None:
        yt = YouTube(uri)
        stream = yt.streams.filter(subtype='mp4').first()
        stream.download(_PATH_TO_VIDEOS + folder_name)


    def convert_mp4_to_wav(self, folder_name: str, mp4_name: str, wav_name: str) -> None:
        path_to_mp4 = _PATH_TO_VIDEOS + folder_name + f"/" + mp4_name
        path_to_wav_folder = _PATH_TO_AUDIO_FILES + folder_name 
        path_to_output_wav = path_to_wav_folder + f"/" + wav_name
       
        if not os.path.exists(path_to_wav_folder):
            os.makedirs(path_to_wav_folder)

        command = f"ffmpeg -i {path_to_mp4} -ab 160k -ac 2 -ar 44100 -vn {path_to_output_wav}" 
        subprocess.call(command, shell=True)


    def get_wav_transcript_from_uri(self, uri: str, folder_name: str, file_name: str) -> None:
        path_to_output_transcript_folder = _PATH_TO_TRANSCRIPT_FILES + folder_name  
        path_to_output_transcript = path_to_output_transcript_folder + f"/" + file_name

        config = {
            "language_code": self.language_code,
            "sample_rate_hertz": self.sample_rate_hertz,
            "audio_channel_count": self.audio_channel_count,
            "enable_word_time_offsets": True
        }

        audio = {
                "uri": uri
        }

        operation = self.speech_client.long_running_recognize(config, audio)
        response = operation.result()

        result = response.results[0]
        most_probable_result = result.alternatives[0]

        if not os.path.exists(path_to_output_transcript_folder):
            os.makedirs(path_to_output_transcript_folder)
 
        with open(path_to_output_transcript, 'w') as json_file:
            json_result = MessageToJson(most_probable_result)
            json_file.write(json_result)
