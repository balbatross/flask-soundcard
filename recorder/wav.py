import scipy.io.wavfile as wave
from pathlib import Path
import numpy
import time

class BatchedWav:
    def __init__(self, path, time_limit):
        print("new file", path)
        self.time_limit = time_limit
        self.buffer = None 
        self.start_time = time.time() * 1000
        self.file = Path(path) 
        self.index = 0

    def write(self, data):
        if(self.buffer is not None): 
            self.buffer = numpy.concatenate([data, self.buffer])
        else:
            self.buffer = data

        if( ( time.time() * 1000 ) - self.start_time > (self.time_limit * 1000)): 
            self.finish_write(self.buffer)
            self.buffer = None
            self.start_time = time.time() * 1000
            self.index += 1

    def finish_write(self, data):
        filename = str(self.file) + "-" + str(self.index) + ".wav"
        wave.write(filename, 44100, data)

    def finish(self):
        self.file.close()
