"""
upload.py

upload files to https://starfiles.co, https://anonfiles.com, https://filepipe.io and https://file.io with ease
"""

__version__ = "0.17"
__author__ = 'CrafterPika'
__credits__ = 'Dwifte'


import json
import requests
import re
from bs4 import BeautifulSoup
import os

class anonfiles():

    def __init__(self):
        pass

    def upload(self, filename):
        files = {
            'file': (f'{os.getcwd()}/{filename}', open( f'{os.getcwd()}/{filename}', 'rb')),
        }
        response = requests.post('https://api.anonfiles.com/upload', files=files)
        global download_url
        global file
        file = filename
        download_url = json.loads(response.text)

    def url_short(self):
        dwnld = download_url['data']['file']['url']['short']
        print(f"{dwnld}")

    def url_full(self):
        dwnld = download_url['data']['file']['url']['full']
        print(f"{dwnld}")

    def metadata(self):
        dwnld = download_url['data']['file']['url']['full']
        name = re.sub(r'^.*?/', '', file)
        print(f"Filename: {name}")

class starfiles():

    def __init__(self):
        pass

    def upload(self, filename):
        files = {
            'upload': (f'{os.getcwd()}/{filename}', open( f'{os.getcwd()}/{filename}', 'rb')),
        }
        response = requests.post('https://starfiles.ml/api/upload_file', files=files)
        global file_url
        file_url = json.loads(response.text)


    def url_file(self):
        dwnld = file_url['file']
        print(f"https://starfiles.ml/file/{dwnld}")

    def url_file_direct(self):
        dwnld = file_url['file']
        print(f"https://starfiles.ml/api/direct/{dwnld}")

    def url_ipa_install(self):
        dwnld = file_url['file']
        print(f"itms-services://?action=download-manifest&url=https://starfiles.ml/api/installipa/{dwnld}")

    def metadata(self):
        dwnld = file_url['file']
        response = requests.post(f'https://starfiles.co/api/file/fileinfo?file={dwnld}')
        meta = json.loads(response.text)
        name = meta['name']
        size = meta['tidy_size']
        print(f"Name: {name}\nSize: {size}")

class filepipe():

    def __init__(self):
        pass

    def upload(self, filename):
        files = {
            'file': (f'{os.getcwd()}/{filename}', open( f'{os.getcwd()}/{filename}', 'rb')),
        }
        response = requests.post('https://api.filepipe.io/upload.php', files=files)
        soup = BeautifulSoup(response.text, 'html.parser')
        global row
        row = soup.find('code')

    def dl_url(self):
        print(f"{row.get_text()}")

class fileio():

    def __init__(self):
        pass

    def upload(self, filename):
        files = {
            'file': (f'{os.getcwd()}/{filename}', open( f'{os.getcwd()}/{filename}', 'rb')),
        }
        response = requests.post('https://file.io', files=files)
        global download_url
        download_url = json.loads(response.text)

    def dl_url(self):
        dwnld = download_url['link']
        print(f"{dwnld}")
