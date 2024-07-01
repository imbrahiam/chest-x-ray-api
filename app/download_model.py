import gdown
import os

def download_model():
    file_id = os.environ.get('GDRIVE_FILE_ID')
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'complete_model.h5'
    gdown.download(url, output, quiet=False)

if __name__ == "__main__":
    download_model()
