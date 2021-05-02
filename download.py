import requests
import json

def download_files_list():
    url = 'https://data-engineering-interns.macpaw.io/files_list.data'
    r = requests.get(url, allow_redirects=True)
    files = str.splitlines(r.content.decode('utf-8'))

    return files

def download_file(filename):
    url = 'https://data-engineering-interns.macpaw.io/' + filename
    r = requests.get(url, allow_redirects=True)

    data = r.content.decode('utf-8')
    data = json.loads(data)

    return data