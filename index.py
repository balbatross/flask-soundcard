from flask import Flask, request, stream_with_context, Response
from card import Card
from recorder import Recorder
from batcher import Batcher
import json
from live import genHeader
app = Flask(__name__)

mixer = Card()
recorder = Recorder('Scarlett')
batcher = Batcher('./garden-sessions')

@app.route('/cards')
def get_cards():
    cards = mixer.get_cards()
    json_cards = list(map(lambda x: {
            'id':x.id,
            'channels': x.channels, 
            'loopback': x.isloopback,
            'name': x.name
        }, cards))
    return json.dumps(json_cards)

@app.route('/cards/<card_name>/channels')
def get_channels(card_name):
    channels = mixer.get_channels(card_name)
    return json.dumps(channels)

@app.route('/cards/<card_name>/channels/<channel>/feed')
def get_channel_feed(card_name, channel):
    def gen():
        with mixer.get_audio_context(card_name, channel) as mic:
            CHUNK = 1024
            sampleRate = 44100
            bitsPerSample = 16
            channels = 1
            data = mixer.get_audio(mic)
            wav_header = genHeader(sampleRate, bitsPerSample, channels, data)
            chunk = wav_header + data
                
            while True:
                yield(chunk)
                data = mixer.get_audio(mic)
                chunk = data
    return Respone(stream_with_context(gen()))

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



