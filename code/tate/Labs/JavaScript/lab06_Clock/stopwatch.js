/*

Clock app

*/

class MyTime {
  constructor (hours=0,minutes=0,seconds=0,milliseconds=0) {
    this.hours = hours;
    this.minutes = minutes;
    this.seconds = seconds;
    this.milliseconds = milliseconds;
  }
}

let stopwatchDisp = document.getElementById('stopwatch-disp');
var stopwatchLaps = document.getElementById('stopwatch-laps');
var storeTime = new MyTime(0,0,0,0);

let startButton = document.getElementById('start-button');
let lapButton = document.getElementById('lap-button');
let clearButton = document.getElementById('clear-button');
let resetButton = document.getElementById('reset-button');
let stopwatchInterval;
let laps = 1;


function addZero(stringNum) {
  num = parseInt(stringNum);
  if (num < 10){
    return `0${stringNum}`;
  } else {
    return stringNum;
  }
}
function lapFunc() {
  pOutput = document.createElement('p');
  pOutput.innerText = `Lap ${laps}: ${addZero(storeTime.hours)}:${addZero(storeTime.minutes)}:${addZero(storeTime.seconds)}`;
  stopwatchLaps.appendChild(pOutput);
  laps += 1;
}
function clearFunc() {
  stopwatchLaps.innerHTML = '';
  laps = 1;
}

function stopwatchFunc() {
  let d = new Date();
  resetButton.style.display = 'none';

  d.setHours(storeTime.hours,storeTime.minutes,storeTime.seconds,storeTime.milliseconds);

  stopwatchDisp.innerText = `${addZero(storeTime.hours)}:${addZero(storeTime.minutes)}:${addZero(storeTime.seconds)}`;

  stopwatchInterval = setInterval(function() {
    d.setSeconds(d.getSeconds() + 1);
    stopwatchDisp.innerText = `${addZero(d.getHours())}:${addZero(d.getMinutes())}:${addZero(d.getSeconds())}`;
    storeTime.seconds = d.getSeconds();
    storeTime.minutes = d.getMinutes();
    storeTime.hours = d.getHours();
  },1000);

  function stopFunc(){
    clearInterval(stopwatchInterval);
    stopwatchDisp.innerText = `${addZero(storeTime.hours)}:${addZero(storeTime.minutes)}:${addZero(storeTime.seconds)}`;
    startButton.innerHTML = 'Start';
    startButton.removeEventListener('click', stopFunc);
    startButton.addEventListener('click', stopwatchFunc);
    resetButton.style.display = 'inline';

    return storeTime;
  }

  if (startButton.innerText.toLowerCase() == 'start'){
    startButton.innerText = 'Stop';
    startButton.removeEventListener('click', stopwatchFunc);
    startButton.addEventListener('click', stopFunc);

  }
  lapButton.addEventListener('click',lapFunc);
}

function resetFunc() {
  storeTime.seconds = 0;
  storeTime.minutes = 0;
  storeTime.hours = 0;
}

clearButton.addEventListener('click',clearFunc);
startButton.addEventListener('click', stopwatchFunc);
resetButton.addEventListener('click', resetFunc);
