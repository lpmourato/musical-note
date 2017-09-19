'use strict';

const BASS = 'bass';
const GUITAR = 'guitar';
const PIANO = 'piano';

let instrument = 'guitar/?defaultKey';
let loop = null;
function changeInstrumentBass(event) {
    instrument = BASS;
    playSound('bass/?defaultKey=a');
}

function changeInstrumentGuitar(event) {
    instrument = GUITAR;
    playSound('guitar/?defaultKey=a');
}

function changeInstrumentPiano(event) {
    instrument = PIANO;
    playSound('piano/?defaultKey=a');
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
            sound.src = xhttp.response;
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

function load() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 3 && xhttp.status === 200) {
            console.log(xhttp.response);
        }
    }
    xhttp.open("GET", 'http://localhost:5000/load', true)
    xhttp.send();
}