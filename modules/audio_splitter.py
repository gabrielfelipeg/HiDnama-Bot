from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import time

def split_audio(audio_path, output_path, min_silence_len=500, silence_thresh=-42):
    """
    split an audio into chunks by a silence threshold

    :param audio_path: path to audio (any format that ffmpeg supports)
    :param output_path: chunks output path
    :param min_silence_len: (in ms) minimum length of a silence to be used for
        a split. default: 500ms
    :param silence_thresh: (in dBFS) anything quieter than this will be
        considered silence. default: -42dBFS
    """

    file_name = os.path.basename(audio_path).split('.')[0]
    print(f"Reading file {file_name}...")
    audio = AudioSegment.from_file(audio_path)

    init_time = time.time()
    chunks = split_on_silence(
        audio,
        min_silence_len = min_silence_len,
        silence_thresh = silence_thresh,
        keep_silence = False
    )
    print(f"Process time: {time.time()-init_time}")
    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"Exporting chunk {i}.")
        chunk.export(
            os.path.join(output_path, f"{file_name}_{i}.mp3"),
            format = "mp3"
        )
