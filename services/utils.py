import os
from pathlib import Path
from tempfile import NamedTemporaryFile


class CsvFileWriter(object):
    def __init__(self, csv_data: str):
        self.csv_data = csv_data
        self.file = NamedTemporaryFile(mode="w", delete=False)

    def __enter__(self):
        self.file.write(self.csv_data)
        self.file.flush()
        self.file.close()
        return Path(self.file.name)

    def __exit__(self, *args, **kwargs):
        os.remove(Path(self.file.name))