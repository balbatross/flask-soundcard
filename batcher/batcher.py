from pathlib import Path
import os

class Batcher:

    def __init__(self, base_dir):
        self.path = Path(base_dir)
        if(os.path.isdir(Path(self.path)) is False):
            os.mkdir(self.path)

    def create_project(self, name):
        if(os.path.isdir(self.path / name)):
            return
        else:
            os.mkdir(self.path / name)

    def get_file(self, name, ix):
        return str((self.path / name / (name + "-" + ix + ".wav")))
