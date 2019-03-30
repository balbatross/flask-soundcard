import wave
from pathlib import Path

class BatchedWav:
    def __init__(self, path):
        self.file = wave.open(Path(path))

    def write(self, data):
        self.file.writeframes(data)

    def finish(self):
        self.file.close()
