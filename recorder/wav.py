import wave
from pathlib import Path

class BatchedWav:
    def __init__(self, path):
        print("new file", path)
        self.file = wave.open(str(Path(path)))

    def write(self, data):
        self.file.writeframes(data)

    def finish(self):
        self.file.close()
