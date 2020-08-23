from pydub import AudioSegment


# not tested
def time_stamp_to_seconds_converter(timestamp: str):  # m:s
    timestamp.split(":")
    return int(timestamp[0]) * 60 + int(timestamp[1])


# not tested
def seconds_to_timestamp_converter(seconds: int):
    minutes = seconds // 60
    sec = seconds % 60
    return str(minutes) + ":" + str(sec)


def save_a_wav_segment(t1: int, t2: int, wav_file_path):  # times should be in seconds
    t1 = t1 * 1000  # Works in milliseconds
    t2 = t2 * 1000
    new_audio = AudioSegment.from_wav(wav_file_path) # should be in wav_files dir/other known path
    new_audio = new_audio[t1:t2]
    identifier = str(t1)[:4] + "_" + str(t2)[:4]
    file_name_parts = wav_file_path.split('.')
    new_file_name = file_name_parts[0] + "_" + identifier + ".wav"
    new_audio.export(new_file_name, format="wav")  # Exports to a wav file in the current path.


def split_all_audio_into_segments(wav_file_path, segment_length):  # files should be from a known path, seg_length in seconds
    audio_length_in_seconds = AudioSegment.from_wav(wav_file_path).duration_seconds
    print("Audio length:", audio_length_in_seconds)
    start_time = 0
    end_time = segment_length
    while True:
        if end_time > audio_length_in_seconds:
            end_time = audio_length_in_seconds
            save_a_wav_segment(start_time, end_time, wav_file_path)
            return
        save_a_wav_segment(start_time, end_time, wav_file_path)
        start_time = end_time
        end_time += segment_length

def xtest():
    test_segment_length = 2
    split_all_audio_into_segments('audio_files/TwentyOne/twenty_one.wav', test_segment_length)
# should see new wav files that are split into this length

