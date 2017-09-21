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

@app.route('/bass/')
def basssound():
    keyParam = request.args.get('defaultKey')
    # if keyParam:
    #     return sounds.SERVER_ADDRESS + 'bass/a2.mp3'
    return sounds.getKeyNote('bass', keyParam)


@app.route('/guitar/')
def guitarsound():
    keyParam = request.args.get('defaultKey')
    if keyParam:
        return sounds.SERVER_ADDRESS + 'guitar/a2.mp3'
    return sounds.getKeyNote('guitar');

@app.route('/piano/')
def pianosound():
    keyParam = request.args.get('defaultKey')
    if keyParam:
        return sounds.SERVER_ADDRESS + 'piano/a2.mp3'
    return sounds.getKeyNote('piano')

@app.route('/all')
def allsound():
    return sounds.getKeyNote('all')

@app.route('/load')
def load():
    sounds.loadKeyNotes()
    return 'Files loaded with success!'


