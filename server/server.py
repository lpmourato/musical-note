from flask import Flask, request
from flask_cors import CORS
from random import Random
import os.path
import sounds

app = Flask(__name__)
CORS(app)
keyParam = ''

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/play/')
def play():
    playerID = request.args.get('playerID')
    mode = request.args.get('mode');
    instrument = request.args.get('instrument');
    key = request.args.get('key');
    return sounds.getKeyNote(encodeStr(playerID), mode, instrument, key)

@app.route('/match/')
def match():
    playerID = request.args.get('playerID')
    keyParam = request.args.get('userKey')
    return sounds.match(encodeStr(playerID), keyParam)

@app.route('/reset/')
def reset():
    playerID = request.args.get('playerID')
    player = sounds.resetData(encodeStr(playerID))
    return player

def encodeStr(value):
    return value.encode('utf-8')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

