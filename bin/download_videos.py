import json

from video_lib import VideoLib

_YOUTUBE_BASE_URI = f"https://www.youtube.com/watch?v="

vid_lib = VideoLib()

vid_lib.download_youtube_video_from_uri(_YOUTUBE_BASE_URI + "axXn_Vn2vYo", "College_Writing_101")
vid_lib.download_youtube_video_from_uri(_YOUTUBE_BASE_URI + "RSoRzTtwgP4", "College_Writing_101")
vid_lib.download_youtube_video_from_uri(_YOUTUBE_BASE_URI + "ZQTQSbjecLg", "College_Writing_101")
vid_lib.download_youtube_video_from_uri(_YOUTUBE_BASE_URI + "lrk4oY7UxpQ&feature=youtu.be", "Political_Science_227")
vid_lib.download_youtube_video_from_uri(_YOUTUBE_BASE_URI + "n9defOwVWS8&feature=youtu.be", "Political_Science_227")
vid_lib.download_youtube_video_from_uri(_YOUTUBE_BASE_URI + "qxiD9AEX4Hc&feature=youtu.be", "Political_Science_227")
