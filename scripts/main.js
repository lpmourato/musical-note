'use strict';

const BASS = 'bass';
const GUITAR = 'guitar';
const PIANO = 'piano';
const ALL = 'all';

let instrument = 'guitar/?defaultKey';
let loop = null;
let currentKey = '';
let score = 0;

function changeInstrumentBass(event) {
    instrument = BASS;
    playSound('bass/?defaultKey=a2.mp3');
}

function changeInstrumentGuitar(event) {
    instrument = GUITAR;
    playSound('guitar/?defaultKey=a2.mp3');
}

function changeInstrumentPiano(event) {
    instrument = PIANO;
    playSound('piano/?defaultKey=a2.mp3');
}

function changeInstrumentAll(event) {
    instrument = ALL;
    playSound('all');
}

function play() {
    playSound();
}

function playSound(keyNote) {
    let xhttp = new XMLHttpRequest();
    let sound = document.getElementById('sound');
    sound.style.display = "none";
    document.body.appendChild(sound);
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 3 && xhttp.status === 200) {
            console.log(JSON.parse(xhttp.response))
            const response = JSON.parse(xhttp.response);
            sound.src = response.address;
            console.log(response.address);
            sound.play();
        }
    }
    const key = keyNote ? keyNote : instrument
    xhttp.open("GET", `http://localhost:5000/${key}`, true);
    xhttp.send();
}

function autoPlay() {
    playSound();
    loop = setInterval(function(){
        playSound();
    }, 2500);
}

function stop() {
    clearInterval(loop);
}

function match(key) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 3 && xhttp.status === 200) {
            const response = JSON.parse(xhttp.response);
            score = response.score;
            const spanScore = document.getElementById('score');
            spanScore.textContent = score;
        }
    }
    xhttp.open("GET", `http://localhost:5000/match/?userKey=${key}`, true)
    xhttp.send();
}

function switchMode() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 3 && xhttp.status === 200) {
            const button = document.getElementById('mode');
            button.value = xhttp.response;
        }
    }
    xhttp.open("GET", 'http://localhost:5000/switch', true)
    xhttp.send();
}