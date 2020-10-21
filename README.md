# upload.py
upload files to https://starfiles.co, https://anonfiles.com, https://filepipe.io and https://file.io with ease

Version 0.23<br>
Created by <a href="https://github.com/CrafterPika">CrafterPika</a> and <a href="https://github.com/DwifteJB">DwifteJB</a>
## Requirements
- Python 3.8=> (only tested it there)

## Tested Systems
- Debian based system (Ubuntu, Debian, Linux Mint, PopOS)
- Windows 10

## Installation (Over PIP)
1. Install python via your package manager or at [Python](https://python.org)
2. ```pip install upload.py```

# Installation (Over Git and PIP)
1. Install python via your package manager or at [Python](https://python.org)
2. Install [git](https://git-scm.com/)
3. Install wheel (```pip install wheel```)
4. ```pip install git+https://github.com/CrafterPika/upload.py.git```

If pip doesn't work/shows up as invalid try this:

- ```python3 -m ensurepip```

and pip3/pip should work.

## Changelog
- Change log is aviable at [here](https://github.com/CrafterPika/upload.py/blob/main/CHANGELOG.md)

### Example

Short Example:
```py
>>> from upload_py import *
>>> import os
>>> file = starfiles()
>>> file.upload(f"{os.getcwd()}/file.txt")
>>> file.url_file()
'https://starfiles.co/file/288e60'
```
(You also can view [example.py](https://github.com/CrafterPika/upload.py/blob/main/upload_py/example.py) for all services example's)
