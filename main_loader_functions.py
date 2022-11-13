import requests
from urllib.parse import urlparse
from os.path import splitext


def picture_loader(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def get_extension(url):
    path = urlparse(url).path
    file_path, extension = splitext(path) 
    return extension