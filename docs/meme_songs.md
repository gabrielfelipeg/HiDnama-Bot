# Memesongs

This module is reponsible for download and load meme songs that are available on GoogleDrive.

## Memesongs()

Download all songs that have been specified in `meme_songs.list` file. Before the musics download, the class need create a connection with Google Drive API.

```python
from module.meme_songs import Memesongs
memesongs = Memesongs()
```

Attributes that Memesongs has

| Attribute | Description | 
|:---------: |:----:|
| songs | String list where each string is a music path from downloaded songs |

Any attribute can be acessed by

```python
memesongs.<atributo>
```