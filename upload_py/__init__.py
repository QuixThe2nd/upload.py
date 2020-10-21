"""
upload.py

upload files to https://starfiles.co, https://anonfiles.com, https://filepipe.io and https://file.io with ease
"""

__version__ = "0.24"
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
            'file': (f'{filename}', open( f'{filename}', 'rb')),
        }
        response = requests.post('https://api.anonfiles.com/upload', files=files)
        global dwnld_anon_short
        global dwnld_anon_full
        global download_url
        global file
        file = filename
        download_url = json.loads(response.text)
        dwnld_anon_short = download_url['data']['file']['url']['short']
        dwnld_anon_full = download_url['data']['file']['url']['full']

    def url_short(self):
        return dwnld_anon_short

    def url_full(self):
        return dwnld_anon_full

    def metadata(self):
        dwnld = download_url['data']['file']['url']['full']
        name = re.sub(r'^.*?/', '', file)
        filename1 = f"Filename: {name}"
        return filename1
    
class bayfiles():

    def __init__(self):
        pass

    def upload(self, filename):
        files = {
            'file': (f'{filename}', open( f'{filename}', 'rb')),
        }
        response = requests.post('https://api.bayfiles.com/upload', files=files)
        global dwnld_bay_short
        global dwnld_bay_full
        global download_url
        global file
        file = filename
        download_url = json.loads(response.text)
        dwnld_bay_short = download_url['data']['file']['url']['short']
        dwnld_bay_full = download_url['data']['file']['url']['full']

    def url_short(self):
        return dwnld_bay_short

    def url_full(self):
        return dwnld_bay_full

    def metadata(self):
        dwnld = download_url['data']['file']['url']['full']
        name = re.sub(r'^.*?/', '', file)
        filename1 = f"Filename: {name}"
        return filename1

class starfiles():

    def __init__(self):
        pass

    def upload(self, filename):
        files = {
            'upload': (f'{filename}', open( f'{filename}', 'rb')),
        }
        response = requests.post('https://starfiles.co/api/upload/upload_file', files=files)
        global file_url
        file_url = json.loads(response.text)
        global dwnld_star
        dwnld_star = file_url['file']


    def url_file(self):
        dwnld = f"https://starfiles.ml/file/{dwnld_star}"
        return dwnld

    def url_file_direct(self):
        dwnld = f"https://starfiles.ml/api/direct/{dwnld_star}"
        return dwnld

    def url_ipa_install(self):
        dwnld = f"itms-services://?action=download-manifest&url=https://starfiles.ml/api/installipa/{dwnld_star}"
        return dwnld

    def metadata(self):
        dwnld = file_url['file']
        response = requests.post(f'https://starfiles.ml/api/file/fileinfo?file={dwnld_star}')
        meta = json.loads(response.text)
        name = meta['name']
        size = meta['tidy_size']
        meta = f"Name: {name}\nSize: {size}"
        return meta

class filepipe():

    def __init__(self):
        pass

    def upload(self, filename):
        files = {
            'file': (f'{filename}', open( f'{filename}', 'rb')),
        }
        response = requests.post('https://api.filepipe.io/upload.php', files=files)
        soup = BeautifulSoup(response.text, 'html.parser')
        global row
        row = soup.find('code')

    def dl_url(self):
        dwnld = f"{row.get_text()}"
        return dwnld

class fileio():

    def __init__(self):
        pass

    def upload(self, filename):
        files = {
            'file': (f'{filename}', open( f'{filename}', 'rb')),
        }
        response = requests.post('https://file.io', files=files)
        global download_url
        download_url = json.loads(response.text)

    def dl_url(self):
        dwnld = download_url['link']
        return dwnld
