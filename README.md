# upload.py
upload files to https://starfiles.co, https://anonfiles.com, https://filepipe.io and https://file.io with ease

# installation
1. You need [git](https://git-scm.com/)
2. Install wheel (```pip install wheel```)
3. ```pip install git+https://github.com/CrafterPika/upload.py.git```

# example

short example of usage:
```py
>>> from upload_py import *
>>> file = starfiles()
>>> file.upload("file.txt")
>>> file.url_file()
https://starfiles.co/file/93ebfa
```
