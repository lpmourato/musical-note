'use strict';

let MusicalNote = function() {};

const HOST_ADDRESS = 'http://localhost:5000';
const BASS = 'bass';
const GUITAR = 'guitar';
const PIANO = 'piano';
const ALL = 'all';
const EASY = 'easy';
const HARD = 'hard';

let currentMode = 'easy';
let selectedInstrument = 'guitar';
let soundInterval = null;
let currentKey = '';
let score = 0;
let playerID = '0'; //TODO: use sessionID

MusicalNote.prototype.init = function() {
    console.log('init');
    musicalNote.reset();
    musicalNote.createEvents('instrument', 'changeInstrument');
    musicalNote.createEvents('key-button', 'match');

    const btnPlay = document.getElementById('play');
    btnPlay.addEventListener('click', function() {
        musicalNote.play();
    });
    const btnAutoPlay = document.getElementById('autoPlay');
    btnAutoPlay.addEventListener('click', function() {
        musicalNote.autoPlay();
    });
    const btnStop = document.getElementById('stop');
    btnStop.addEventListener('click', function() {
        musicalNote.stop();
    });
    const btnMode = document.getElementById('mode');
    btnMode.addEventListener('click', function() {
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
    selectedInstrument = name.toLowerCase();
    if (name.toLowerCase() === ALL) {
        const pos = parseInt(Math.random() * (3 - 0) + 0);
        const inst = [BASS, GUITAR, PIANO];
        selectedInstrument = inst[pos];
    }
    currentKey = undefined;
    this.playSound(`${HOST_ADDRESS}/static/sounds/${selectedInstrument}/a2.mp3`);
}

MusicalNote.prototype.play = function() {
    if (this.isEasyMode()) {
        return
    }
    let address = `${HOST_ADDRESS}/play?playerID=${playerID}&mode=${currentMode}&instrument=${selectedInstrument}`;
    const request = musicalNote.requestHeaders(address);
    fetch(request).then(function(response) {
        if(response.ok && response.status === 200) {
            response.json().then(keyNote => {
                console.log(keyNote);
                currentKey = keyNote.address;
                musicalNote.playSound(currentKey);
            });
        }
      }).catch(function(error) {
        console.log(error);
      });
}

MusicalNote.prototype.playSound = function(key) {
    let sound = document.getElementById('sound');
    sound.src = key || currentKey;
    console.log(sound.src);
    sound.play();
}

MusicalNote.prototype.isEasyMode = function() {
    if (currentKey && sound.src && currentMode === EASY) {
        musicalNote.playSound(currentKey);
        return true;
    }
    return false;
}

MusicalNote.prototype.autoPlay = function() {
    musicalNote.play();
    soundInterval = setInterval(function(){
        musicalNote.play();
    }, 2500);
}

MusicalNote.prototype.stop = function() {
    clearInterval(soundInterval);
}

MusicalNote.prototype.reset = function() {
    playerID = parseInt(Math.random() * (1000 - 0) + 0)
    const request = musicalNote.requestHeaders(`${HOST_ADDRESS}/reset?playerID=${playerID}`);
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
    currentKey = undefined;
    const request = musicalNote.requestHeaders(`${HOST_ADDRESS}/match?playerID=${playerID}&userKey=${key}`);
    fetch(request).then(function(response) {
        if(response.ok && response.status === 200) {
            response.json().then(player => {
                console.log(player);
                score = player._Player__score;
                const spanScore = document.getElementById('score');
                spanScore.textContent = score;
            });
        }
      }).catch(function(error) {
        console.log(error);
      });
}

MusicalNote.prototype.switchMode = function() {
    currentMode = currentMode === EASY ? HARD : EASY;
    document.getElementById('mode').value = currentMode.toUpperCase();
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