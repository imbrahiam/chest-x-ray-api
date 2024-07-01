import gdown
import os

def download_model():
    file_id = os.environ.get('GDRIVE_FILE_ID')
    if not file_id:
        raise ValueError("GDRIVE_FILE_ID environment variable not set or empty")
    print(f"File ID: {file_id}")
    url = f'https://drive.google.com/uc?id={file_id}&export=download'
    output = 'complete_model.h5'
    gdown.download(url, output, quiet=False)

if __name__ == "__main__":
    download_model()
