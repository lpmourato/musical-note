from flask import Flask, request
from flask_cors import CORS
from random import Random
import os.path
import sounds

app = Flask(__name__)
CORS(app)
keyParam = ''

def init_app():
    sounds.resetData()

init_app()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/bass/')
def basssound():
    keyParam = request.args.get('defaultKey')
    return sounds.getKeyNote('bass', keyParam)


@app.route('/guitar/')
def guitarsound():
    keyParam = request.args.get('defaultKey')
    return sounds.getKeyNote('guitar', keyParam)

@app.route('/piano/')
def pianosound():
    keyParam = request.args.get('defaultKey')
    return sounds.getKeyNote('piano', keyParam)

@app.route('/all')
def allsound():
    return sounds.getKeyNote('all', 'a2.mp3')

@app.route('/match/')
def match():
    keyParam = request.args.get('userKey')
    return sounds.match(keyParam)

@app.route('/switch')
def switch():
    return sounds.getMode()


