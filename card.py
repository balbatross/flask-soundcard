import soundcard as sc

class Card:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def get_cards(self):
        return sc.all_microphones()

    def get_channels(self, name):
        return sc.get_microphone(name).channels

    def get_audio(self):
        return self.recorder.record(num_frames=1024)

