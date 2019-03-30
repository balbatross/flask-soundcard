from threading import Thread
import soundcard as sc
from .line import Line

class Recorder:

    def __init__(self, mixer_name):
        self.card = sc.get_microphone(mixer_name)
            

    def record(self, project_name):
        print("Recording ", project_name)
        l = Line(project_name + "/line-8", self.card, [7], 44100)
        l.start()
