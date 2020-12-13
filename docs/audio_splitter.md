# Audio Splitter

Split an audio into chunks by a silence threshold. It is used for separating sentences from the input audio.

## split_audio

```python
split_audio(audio_path, output_path, min_silence_len=500, silence_thresh=-42)
```
Split an audio into chunks by a silence threshold. Audio must be a file and all chunks will be writed in disk.

Parameters

| Parameter | Description | Default Value
|:---------: |:----:| :----: |
|audio_path | path to audio (any format that ffmpeg (supports) | -
|output_path | chunks output path | -
|min_silence_len | (in ms) minimum length of a silence to be used for a split. | 500ms
|silence_thresh | (in dBFS) anything quieter than this will be considered silence. | -42dBFS
