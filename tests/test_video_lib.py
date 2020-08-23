# test_video_lib.py

import pytest
import os.path

from bin.video_lib import VideoLib

# Global VideoLib object to be used throughout suite:
vid_lib = VideoLib()

def test_ctor():
    assert vid_lib.language_code == "en-US"

def test_fetch_download_youtube_video_from_uri():
    vid_lib.download_youtube_video_from_uri(f"https://www.youtube.com/watch?v=UniPsEFWu3M", "TwentyOne", "twenty_one.mp4")
    
    assert os.path.exists(f"../videos/TwentyOne")


def test_convert_mp4_to_wav():
    vid_lib.convert_mp4_to_wav("TwentyOne", f"twenty_one.mp4", "twenty_one.wav")

    assert os.path.exists(f"../audio_files/TwentyOne")


def test_get_wav_transcript_from_uri():
    vid_lib.get_wav_transcript_from_uri(f"gs://classroom_1/twenty_one.wav")


    
