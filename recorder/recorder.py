from threading import Thread
import soundcard as sc
from .line import Line

class Recorder:

    def __init__(self, mixer_name):
        self.card = sc.get_microphone(mixer_name)
            

    def record(self, project_name, channels):
        print("Recording ", project_name)
        for idx, val in enumerate(channels):
            l = Line(project_name + "/line-" + str(val), self.card, [val], 44100)
            l.start()
