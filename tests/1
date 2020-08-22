# test_video_lib.py

import pytest

from bin.video_lib import VideoLib

# Global VideoLib object to be used throughout suite:
vid_lib = VideoLib()

def test_ctor():
    assert vid_lib.language_code == "en-US"

def test_fetch_download_youtube_video_from_uri():
    print(vid_lib.download_youtube_video_from_uri(f"https://www.youtube.com/watch?v=UniPsEFWu3M", "TwentyOne"))

    
