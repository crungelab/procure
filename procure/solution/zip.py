import requests
import tempfile
import zipfile

from pathlib import Path

from .solution import Solution


class ZipSolution(Solution):
    path = ""
    url = ""

    def update(self):
        path = Path(self.path)
        if path.exists():
            return

        zip_file = self.download_file(self.url)
        self.extract_zip(zip_file, self.path)

    def download_file(self, url: str):
        response = requests.get(url, stream=True)
        temp_file = tempfile.TemporaryFile()
        for chunk in response.iter_content(chunk_size=128):
            temp_file.write(chunk)
        # reset file pointer to beginning
        temp_file.seek(0)
        return temp_file

    def extract_zip(self, file_path, extract_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
