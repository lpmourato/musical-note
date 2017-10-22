'use strict';

let MusicalNote = function() {};

const HOST_ADDRESS = 'http://localhost:5000';
const Instruments = {
    BASS: 'bass',
    GUITAR: 'guitar',
    PIANO: 'piano',
    ALL: 'all',
}
const EASY = 'easy';
const HARD = 'hard';

const state = {
    currentMode: 'easy',
    selectedInstrument: 'guitar',
    soundInterval: null,
    currentKey: '',
    score: 0,
    playerID: '0',  //TODO: use sessionID
}

MusicalNote.prototype.init = function() {
    console.log('init');
    musicalNote.reset();
    musicalNote.createEvents('instrument', 'changeInstrument');
    musicalNote.createEvents('key-button', 'match');

    document.getElementById('play').addEventListener('click', function() {
        musicalNote.play();
    });
    document.getElementById('autoPlay').addEventListener('click', function() {
        musicalNote.autoPlay();
    });
    document.getElementById('stop').addEventListener('click', function() {
        musicalNote.stop();
    });
    document.getElementById('mode').addEventListener('click', function() {
        musicalNote.switchMode();
    });
}

MusicalNote.prototype.createEvents = function(classes, method) {
    let buttons = document.getElementsByClassName(classes);
    for (let i = 0; i < buttons.length; i++) {
        let button = buttons[i];
        button.addEventListener('click', function() {
            switch(method) {
                case 'changeInstrument': {
                    musicalNote.changeInstrument(button.value);
                    break;
                }
                case 'match': {
                    musicalNote.match(button.value.toLowerCase());
                    break;
                }
            }
        });
    }
}

MusicalNote.prototype.changeInstrument = function(name) {
    state.selectedInstrument = name.toLowerCase();
    if (name.toLowerCase() === Instruments.ALL) {
        const pos = parseInt(Math.random() * (3 - 0) + 0);
        const inst = Object.values(Instruments);
        state.selectedInstrument = inst[pos];
    }
    state.currentKey = undefined;
    this.playSound(`${HOST_ADDRESS}/static/sounds/${state.selectedInstrument}/default.mp3`);
}

MusicalNote.prototype.play = function() {
    if (this.isEasyMode()) {
        return
    }
    let address = `${HOST_ADDRESS}/play?playerID=${state.playerID}&mode=${state.currentMode}&instrument=${state.selectedInstrument}`;
    const request = musicalNote.requestHeaders(address);
    fetch(request).then(function(response) {
        if(response.ok && response.status === 200) {
            response.json().then(keyNote => {
                console.log(keyNote);
                state.currentKey = keyNote.address;
                musicalNote.playSound(state.currentKey);
            });
        }
      }).catch(function(error) {
        console.log(error);
      });
}

MusicalNote.prototype.playSound = function(key) {
    let sound = document.getElementById('sound');
    sound.src = key || state.currentKey;
    console.log(sound.src);
    sound.play();
}

MusicalNote.prototype.isEasyMode = function() {
    if (state.currentKey && sound.src && state.currentMode === EASY) {
        musicalNote.playSound(state.currentKey);
        return true;
    }
    return false;
}

MusicalNote.prototype.autoPlay = function() {
    musicalNote.play();
    state.soundInterval = setInterval(function(){
        musicalNote.play();
    }, 2500);
}

MusicalNote.prototype.stop = function() {
    clearInterval(state.soundInterval);
}

MusicalNote.prototype.reset = function() {
    state.playerID = parseInt(Math.random() * (1000 - 0) + 0)
    const request = musicalNote.requestHeaders(`${HOST_ADDRESS}/reset?playerID=${state.playerID}`);
    fetch(request).then(function(response) {
        if(response.ok && response.status === 200) {
            response.json().then(player => {
                console.log(player);
                const p = document.getElementById('playerID');
                p.textContent = player._Player__playerID;
            });
        }
      }).catch(function(error) {
        console.log(error);
      });
}

MusicalNote.prototype.match = function(key) {
    state.currentKey = undefined;
    const request = musicalNote.requestHeaders(`${HOST_ADDRESS}/match?playerID=${state.playerID}&userKey=${key}`);
    fetch(request).then(function(response) {
        if(response.ok && response.status === 200) {
            response.json().then(player => {
                console.log(player);
                state.score = player._Player__score;
                const spanScore = document.getElementById('score');
                spanScore.textContent = state.score;
            });
        }
      }).catch(function(error) {
        console.log(error);
      });
}

MusicalNote.prototype.switchMode = function() {
    state.currentMode = state.currentMode === EASY ? HARD : EASY;
    document.getElementById('mode').value = state.currentMode.toUpperCase();
}

MusicalNote.prototype.requestHeaders = function(url) {
    const headers = new Headers();

    const init = { method: 'GET',
                   headers: headers,
                   mode: 'cors',
                   cache: 'default' };
    const req = new Request(url, init);
    return req;
}

const musicalNote = new MusicalNote();
musicalNote.init();