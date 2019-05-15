var ms=0 , s=0, m=0;
var timer;
var stopwatchEl=document.querySelector('.stopwatch');
var lapsContainer=document.querySelector('.laps');

function start() {
    if (!timer) { timer = setInterval(run,10);}
}

function run() {
    stopwatchEl.textContent = getTimer();
    ms++;
    if (ms === 100){
        ms = 0;
        s++;
    }
    if (s === 60){
        s = 0;
        m++;
    }
}

function pause() {
    stopTimer();
}

function stop() {
    stopTimer();
    ms=0;
    s=0;
    m=0;
    stopwatchEl.contentElement = getTimer();
}
function stopTimer() {
     clearInterval(timer);
    timer = false;
}
function getTimer() {
    return (m<10? "0" + m: m) + ":" + (s<10? "0" + s : s)  + ":" + (ms<10? "0" + ms: ms);
}

function restart() {
    stop();
    start();
}
function lap() {
    if (timer) {
        var li = document.createElement("li");
        li.innerText = getTimer();
        lapsContainer.appendChild(li)
    }
}
function resetLaps() {
    lapsContainer.innerHTML = "";
}









// let seconds= 0;
// let minutes= 0;
// let hours= 0;
// let displaySeconds = 0;
// let displayMinutes = 0;
// let displayHours = 0;
// let interval = null;
//
//
// function stopwatch() {
//
//     seconds ++;
//
//     if (seconds/60 === 1){
//         seconds =0;
//         minutes ++;
//         if (minutes/60 ===1){
//             minutes = 0;
//             hours++;
//         }
//     }
//     if(seconds<10){
//         displaySeconds = "0"+ seconds.toString();
//     }
//     else {displaySeconds = seconds;}
//     if(minutes<10){
//         displayMinutes = "0"+ minutes.toString();
//     }
//     else {displayMinutes = minutes;}
//     if(hours <10){
//         displayHours = "0"+ hours.toString();
//     }
//     else {displayHours= hours;}
// document.getElementById("timer").innerHTML= displayHours  + ":" + displayMinutes  + ":" + displaySeconds;
// }
//
// setInterval(stopwatch,1000);
//
// let status = "stopped";
//
// function startStop() {
//     if ( status === "stopped"){
//         interval = window.setInterval(stopwatch,1000);
//         document.getElementById("start").innerHTML= "Stop";
//         status= 'started'}
//     else {window.clearInterval(interval);
//     document.getElementById("start").innerHTML = "Start";}
//     status= 'stopped'
//     }
//
// // start_button = document.getElementById("start");
// // start_button.onclick = startStop() ;
//
// function reset() {
//     window.clearInterval(interval);
//     seconds=0;
//     minutes = 0;
//     hours=0;
//     document.getElementById("timer").innerHTML= "00:00:00";
//     document.getElementById("start").innerHTML = "start";
// }

