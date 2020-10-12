# upload.py
upload files to https://starfiles.co, https://anonfiles.com, https://filepipe.io and https://file.io with ease

Version 1.0
Created by <a href="https://github.com/CrafterPika">CrafterPika</a> and <a href="https://github.com/DwifteJB">DwifteJB</a>
## Requirements
- Python 3.8=> (only tested it there)

## Tested Systems
Debian based system (Ubuntu, Debian, Linux Mint, PopOS)

Windows 10

# Installation
1. Install python via your package manager or at [Python](https://python.org)
2. Install [git](https://git-scm.com/)
3. Install wheel (```pip install wheel```)
4. ```pip install git+https://github.com/CrafterPika/upload.py.git```

If pip doesn't work/shows up as invalid try this:

```python3 -m ensurepip```

and pip3/pip should work.

### Example

Short Example:
```py
>>> from upload_py import *
>>> file = starfiles()
>>> file.upload("file.txt")
>>> file.url_file()
```
(You also can view [example.py](https://github.com/CrafterPika/upload.py/blob/main/upload_py/example.py) for all services example's)
