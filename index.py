from flask import Flask
from card import Card
from recorder import Recorder

app = Flask(__name__)

mixer = Card()
recorder = Recorder('Scarlett')
recorder.record('test-run')

@app.route('/record')
def record():
    recorder.record('test-run')
    #Record channels sepcified in post

@app.route('/channels')
def get_channels():
    return mixer.get_channels()


