from flask import Flask
from card import Card
from recorder import Recorder
from batcher import Batcher

app = Flask(__name__)

mixer = Card()
recorder = Recorder('Scarlett')
batcher = Batcher('./garden-sessions')

batcher.create_project("test-run")
new_file = batcher.get_file("test-run", 0) 
recorder.record(new_file)

@app.route('/record')
def record():
    recorder.record('test-run')
    #Record channels sepcified in post

@app.route('/channels')
def get_channels():
    return mixer.get_channels()


