'use strict';

let musicalNote = function() {};

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

musicalNote.prototype.init = function() {
    console.log('init');
    musicalNote.prototype.reset();
    musicalNote.prototype.createEvents('instrument', 'changeInstrument');
    musicalNote.prototype.createEvents('key-button', 'match');
    const btnPlay = document.getElementById('play');
    btnPlay.addEventListener('click', function() {
        musicalNote.prototype.play();
    });
    const btnAutoPlay = document.getElementById('autoPlay');
    btnAutoPlay.addEventListener('click', function() {
        musicalNote.prototype.autoPlay();
    });
    const btnStop = document.getElementById('stop');
    btnStop.addEventListener('click', function() {
        musicalNote.prototype.stop();
    });
    const btnMode = document.getElementById('mode');
    btnMode.addEventListener('click', function() {
        musicalNote.prototype.switchMode();
    });
}

musicalNote.prototype.createEvents = function(classes, method) {
    let buttons = document.getElementsByClassName(classes);
    for (let i = 0; i < buttons.length; i++) {
        let button = buttons[i];
        button.addEventListener('click', function() {
            switch(method) {
                case 'changeInstrument': {
                    musicalNote.prototype.changeInstrument(button.value);
                    break;
                }
                case 'match': {
                    musicalNote.prototype.match(button.value.toLowerCase());
                    break;
                }

            }
        });
    }
}

musicalNote.prototype.changeInstrument = function(name) {
    selectedInstrument = name.toLowerCase();
    if (name.toLowerCase() === ALL) {
        const pos = parseInt(Math.random() * (3 - 0) + 0);
        const inst = [BASS, GUITAR, PIANO];
        selectedInstrument = inst[pos];
    }
    currentKey = undefined;
    this.playSound(`${HOST_ADDRESS}/static/sounds/${selectedInstrument}/a2.mp3`);
}

musicalNote.prototype.play = function() {
    if (this.isEasyMode()) {
        return
    }
    let xhttp = new XMLHttpRequest();
    sound.style.display = "none";
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 3 && xhttp.status === 200) {
            const response = JSON.parse(xhttp.response);
            currentKey = response.address;
            musicalNote.prototype.playSound(currentKey);
        }
    }
    let address = `${HOST_ADDRESS}/play?playerID=${playerID}&mode=${currentMode}&instrument=${selectedInstrument}`;
    xhttp.open("GET", address, true);
    xhttp.send();
}

musicalNote.prototype.playSound = function(key) {
    let sound = document.getElementById('sound');
    sound.src = key || currentKey;
    console.log(sound.src);
    sound.play();
}

musicalNote.prototype.isEasyMode = function() {
    if (currentKey && sound.src && currentMode === EASY) {
        musicalNote.prototype.playSound(currentKey);
        return true;
    }
    return false;
}

musicalNote.prototype.autoPlay = function() {
    musicalNote.prototype.play();
    soundInterval = setInterval(function(){
        musicalNote.prototype.play();
    }, 2500);
}

musicalNote.prototype.stop = function() {
    clearInterval(soundInterval);
}

musicalNote.prototype.reset = function() {
    playerID = parseInt(Math.random() * (1000 - 0) + 0)
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 3 && xhttp.status === 200) {
            console.log(xhttp.response);
            const response = JSON.parse(xhttp.response);
            const p = document.getElementById('playerID');
            p.textContent = response._Player__playerID;
        }
    }
    xhttp.open("GET", `${HOST_ADDRESS}/reset?playerID=${playerID}`, true);
    xhttp.send();
}

musicalNote.prototype.match = function(key) {
    currentKey = undefined;
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 3 && xhttp.status === 200) {
            const response = JSON.parse(xhttp.response);
            score = response._Player__score;
            const spanScore = document.getElementById('score');
            spanScore.textContent = score;
        }
    }
    xhttp.open("GET", `${HOST_ADDRESS}/match?playerID=${playerID}&userKey=${key}`, true)
    xhttp.send();
}

musicalNote.prototype.switchMode = function() {
    currentMode = currentMode === EASY ? HARD : EASY;
    document.getElementById('mode').value = currentMode.toUpperCase();
}

musicalNote.prototype.init();