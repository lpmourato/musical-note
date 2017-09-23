from flask import jsonify
import re
import os
from random import Random
import socket
from player import Player


activePlayers = {}
SERVER_ADDRESS = 'http://%s:5000/static/sounds/'
INSTRUMENTS = [ 
    'bass',
    'guitar',
    'piano',
    'all' ]

EASY = 'easy'
HARD = 'hard'


bassArray = []
guitarArray = []
pianoArray = []
currentArray = []

def getKeyNote(playerID, mode, instrument, keyParam):
    if instrument == INSTRUMENTS[0]:
        currentArray = bassArray
    elif instrument == INSTRUMENTS[1]:
        currentArray = guitarArray
    elif instrument == INSTRUMENTS[2]:
        currentArray = pianoArray
    else:
        random = Random()
        randInstrument = random.randint(0, 3)
        return getKeyNote(mode, INSTRUMENTS[randInstrument], keyParam)
    key = ''
    if keyParam:
        key = keyParam
    else:
        random = Random()
        pos = random.randint(0, len(currentArray) - 1)
        key = currentArray[pos]

    # Call getKeyNote if is easy mode and the key get is sharp
    if mode == EASY and isSharpKey(key):
        return getKeyNote(playerID, mode, instrument, keyParam)

    name, ext = os.path.splitext(key)
    print name + ' ' + ext
    # TODO: make key note name confuse to the user
    pathKey = getKeyPathAsJson(instrument, key)
    activePlayer = activePlayers[playerID]
    activePlayer.setCurrentKey(re.sub(r'\d+', '', key[:-4]))
    return pathKey

def getKeyPathAsJson(instrument, key):
    global currentInstrument
    pathKey = SERVER_ADDRESS + instrument + '/' + key
    return jsonify(address = pathKey)

def isSharpKey(key):
    regex = re.compile(r's')
    return regex.search(key);

def match(playerID, userKey):
    activePlayer = activePlayers[playerID]
    if activePlayer.getCurrentKey() == userKey.lower():
        activePlayer.updateScore()
    activePlayer.setCurrentKey(None)
    return activePlayer.toJSON()

def resetData(playerID):
    global SERVER_ADDRESS
    host = socket.gethostbyname(socket.getfqdn())
    SERVER_ADDRESS = 'http://%s:5000/static/sounds/' % (host)
    bassArray = []
    guitarArray = []
    pianoArray = []
    currentArray = []
    playerInstance = Player(playerID)
    activePlayers[playerID] = playerInstance
    # playerInstance.resetScore() //TODO it is really necessary?
    loadKeyNotes()
    return activePlayers[playerID].toJSON();
    # return playerInstance.toJSON();

def loadKeyNotes():
    bassArray.append('a0.mp3')
    bassArray.append('a1.mp3')
    bassArray.append('a2.mp3')
    bassArray.append('as.mp3')
    bassArray.append('as1.mp3')
    bassArray.append('as2.mp3')
    bassArray.append('b0.mp3')
    bassArray.append('b1.mp3')
    bassArray.append('b2.mp3')
    bassArray.append('c0.mp3')
    bassArray.append('c1.mp3')
    bassArray.append('c2.mp3')
    bassArray.append('c28.mp3')
    bassArray.append('cs0.mp3')
    bassArray.append('cs1.mp3')
    bassArray.append('cs2.mp3')
    bassArray.append('d0.mp3')
    bassArray.append('d1.mp3')
    bassArray.append('d2.mp3')
    bassArray.append('ds.mp3')
    bassArray.append('ds1.mp3')
    bassArray.append('ds2.mp3')
    bassArray.append('e0.mp3')
    bassArray.append('e1.mp3')
    bassArray.append('e2.mp3')
    bassArray.append('f0.mp3')
    bassArray.append('f1.mp3')
    bassArray.append('f2.mp3')
    bassArray.append('fs.mp3')
    bassArray.append('fs1.mp3')
    bassArray.append('fs2.mp3')
    bassArray.append('g.mp3')
    bassArray.append('g1.mp3')
    bassArray.append('g2.mp3')
    bassArray.append('gs.mp3')
    bassArray.append('gs1.mp3')
    bassArray.append('gs2.mp3')

    guitarArray.append('a1.mp3')
    guitarArray.append('a2.mp3')
    guitarArray.append('a3.mp3')
    guitarArray.append('a4.mp3')
    guitarArray.append('as1.mp3')
    guitarArray.append('as2.mp3')
    guitarArray.append('as4.mp3')
    guitarArray.append('b1.mp3')
    guitarArray.append('b2.mp3')
    guitarArray.append('b4.mp3')
    guitarArray.append('c.mp3')
    guitarArray.append('c1.mp3')
    guitarArray.append('c2.mp3')
    guitarArray.append('c3.mp3')
    guitarArray.append('cs.mp3')
    guitarArray.append('cs1.mp3')
    guitarArray.append('cs2.mp3')
    guitarArray.append('cs3.mp3')
    guitarArray.append('d0.mp3')
    guitarArray.append('d1.mp3')
    guitarArray.append('d2.mp3')
    guitarArray.append('d3.mp3')
    guitarArray.append('ds0.mp3')
    guitarArray.append('ds1.mp3')
    guitarArray.append('ds2.mp3')
    guitarArray.append('ds3.mp3')
    guitarArray.append('e0.mp3')
    guitarArray.append('e1.mp3')
    guitarArray.append('e2.mp3')
    guitarArray.append('e3.mp3')
    guitarArray.append('f0.mp3')
    guitarArray.append('f1.mp3')
    guitarArray.append('f2.mp3')
    guitarArray.append('f3.mp3')
    guitarArray.append('fs0.mp3')
    guitarArray.append('fs1.mp3')
    guitarArray.append('fs2.mp3')
    guitarArray.append('fs3.mp3')
    guitarArray.append('g0.mp3')
    guitarArray.append('g1.mp3')
    guitarArray.append('g2.mp3')
    guitarArray.append('g3.mp3')
    guitarArray.append('gs.mp3')
    guitarArray.append('gs1.mp3')
    guitarArray.append('gs2.mp3')
    guitarArray.append('gs3.mp3')


    pianoArray.append('a0.mp3')
    pianoArray.append('a1.mp3')
    pianoArray.append('a2.mp3')
    pianoArray.append('as0.mp3')
    pianoArray.append('as1.mp3')
    pianoArray.append('as2.mp3')
    pianoArray.append('b0.mp3')
    pianoArray.append('b1.mp3')
    pianoArray.append('b2.mp3')
    pianoArray.append('c0.mp3')
    pianoArray.append('c1.mp3')
    pianoArray.append('c2.mp3')
    pianoArray.append('cs0.mp3')
    pianoArray.append('cs1.mp3')
    pianoArray.append('cs2.mp3')
    pianoArray.append('d0.mp3')
    pianoArray.append('d1.mp3')
    pianoArray.append('d2.mp3')
    pianoArray.append('ds0.mp3')
    pianoArray.append('ds1.mp3')
    pianoArray.append('ds2.mp3')
    pianoArray.append('e0.mp3')
    pianoArray.append('e1.mp3')
    pianoArray.append('e2.mp3')
    pianoArray.append('f0.mp3')
    pianoArray.append('f1.mp3')
    pianoArray.append('f2.mp3')
    pianoArray.append('fs.mp3')
    pianoArray.append('fs1.mp3')
    pianoArray.append('fs2.mp3')
    pianoArray.append('g0.mp3')
    pianoArray.append('g1.mp3')
    pianoArray.append('g2.mp3')
    pianoArray.append('gs0.mp3')
    pianoArray.append('gs1.mp3')
    pianoArray.append('gs2.mp3')

