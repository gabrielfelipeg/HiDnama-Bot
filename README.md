# HiDnama Bot

## Installation

## Usage example

## Development setup

## Dependencies

- [Pydub 0.24.1](http://pydub.com/) - Manipulate audio with a simple and easy high level interface
- [ffmpeg](https://ffmpeg.org/) - A complete, cross-platform solution to record, convert and stream audio and video.

## Modules

- audio_splitter: Split an audio into chunks by a silence threshold. It is used for separating sentences from the input audio.

### Logger

Specifies the basic log standard for all modules using the python logging package.

The logger uses the following message format:
```python
'%(asctime)s|%(levelname)s|%(name)s.%(funcName)s|%(message)s',
```
asctime - ISO_8601
levelname - nível do log
name - nome do pacote seguido do módulo.
funcName - nome da função que originou o log
message - mensagem de log.

## Meta