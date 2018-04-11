from flask import Flask, request, render_template
from redis import Redis
from flask_cors import CORS
from random import Random
import sounds
import os

if os.environ.get('HOST_REDIS'):
    host_redis = os.environ.get('HOST_REDIS')
else:
    host_redis = 'redis'

if os.environ.get('PORT_REDIS'):
    port_redis = os.environ.get('PORT_REDIS')
else:
    port_redis = 6379

app = Flask(__name__)
CORS(app)
redis = Redis(host=host_redis, port=port_redis)

@app.route('/')
def main_route():
    return render_template('index.html')


@app.route('/play/')
def play():
    playerID = getPlayerID(request)
    mode = request.args.get('mode');
    instrument = request.args.get('instrument');
    key = request.args.get('key');
    return sounds.getKeyNote(encodeStr(playerID), mode, instrument, key)

@app.route('/match/')
def match():
    playerID = getPlayerID(request)
    keyParam = request.args.get('userKey')
    return sounds.match(encodeStr(playerID), keyParam)

@app.route('/reset/')
def reset():
    playerID = getPlayerID(request)
    player = sounds.resetData(encodeStr(playerID))
    return player

def getPlayerID(request):
    return request.args.get('playerID') or "-1"

def encodeStr(value):
    return value.encode('utf-8')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)