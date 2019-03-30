from flask import Flask, request
from card import Card
from recorder import Recorder
from batcher import Batcher
import json
app = Flask(__name__)

mixer = Card()
recorder = Recorder('Scarlett')
batcher = Batcher('./garden-sessions')


@app.route('/status')
def status_check():
    return json.dumps({'status': 'OK'})

@app.route('/live')
def go_live():
    return "hello"

@app.route('/record')
def record():
    batcher.create_project(request.args['name'])
    recorder.record(batcher.get_dir(request.args['name']), [0,1,2,3,4,5,6,7])
    #Record channels sepcified in post

@app.route('/channels')
def get_channels():
    return mixer.get_channels()


