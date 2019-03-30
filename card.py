import soundcard as sc

class Card:
    def __init__(self, sample_rate=44100):
        self.input = sc.get_microphone('Scarlett')
        self.channels = self.input.channels
        self.recorder = self.input.recorder(sample_rate)

    def get_channels(self):
        return self.channels

    def record(self, channels):


