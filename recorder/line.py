from threading import Thread
import wave
from pathlib import Path
from .wav import BatchedWav

class Line(Thread):

    def __init__(self, path, card, channel, sample_rate):
        Thread.__init__(self)
        self.path = Path(path)
        self.card = card
        self.channel = channel
        self.sample_rate = sample_rate
        self.recording = False

    def run(self):
        self.recording = True
        _file = BatchedWav(self.path)
        with self.card.recorder(self.sample_rate, channels=self.channel) as recorder:
            while self.recording:
                data = recorder.record(numframes=1024)
                _file.write(data)     
        
        _file.close()
