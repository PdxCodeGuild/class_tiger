// Display & Nav buttons
let timeBtn = document.getElementById("timebutton");
let stopwatchBtn = document.getElementById("stopwatchbutton");
let timerBtn = document.getElementById("timerbutton");
let seeTime = document.getElementById("seetime");
let seeStopwatch = document.getElementById("seestopwatch");
let seeTimer = document.getElementById("seetimer");
let navBtns = document.getElementsByClassName("navbutton");
let allDisplay = document.getElementsByClassName("display");
            
seeStopwatch.style.display = "none";
seeTime.style.display = "none";
for(let i = 0; i < navBtns.length; i++){
    navBtns[i].addEventListener("click", function(){
        console.log("clicked");
        for(let j = 0; j < allDisplay.length; j++){
            allDisplay[j].style.display = "none";
        }
        if (navBtns[i].id === "timerbutton"){
            seeTimer.style.display = "block";
        } else if (navBtns[i].id === "stopwatchbutton"){
            seeStopwatch.style.display = "block";
        } else if (navBtns[i].id === "timebutton"){
            seeTime.style.display = "block";
        }

})

}
let time = document.getElementById("time");

let timer = document.getElementById("timer");

let stopWatch = document.getElementById("stopwatch");
let startBtn = document.getElementsByClassName("start")[0];
let lapBtn = document.getElementsByClassName("lap")[0];
let stopBtn = document.getElementsByClassName("stop")[0];
let laps = document.getElementsByClassName("laps")[0];
var newDate = new Date();
newDate.setHours(0,0,0,0);
let NewTime;
let sw;
// Current Time
setInterval(function(){
    time.innerText = new Date().toString().split(" ")[4];
},1000)
// Stopwatch
stopWatch.innerText = "00:00:00"

startBtn.addEventListener("click", function(){
    sw = setInterval(function(){
        newDate.setSeconds(newDate.getSeconds()+1);
        newTime = newDate.toString().split(" ")[4];
        stopWatch.innerText = newTime;
    }, 1000)
})
lapBtn.addEventListener("click", function(){
    let newLap = document.createElement("p");
    newLap.class="eachlap";
    newLap.innerText = newTime;
    let numLaps = document.getElementsByClassName("eachlap");
    if (numLaps.length > 2){
        removeLap = laps.firstElementChild;
        laps.removeChild(removeLap)
    }
    laps.appendChild(newLap);
    
})
stopBtn.addEventListener("click", function(){
    clearInterval(sw)
    newDate.setHours(0,0,0,0);
    newTime = newDate.toString().split(" ")[4];
    stopWatch.innerText = newTime;
    laps.innerText = "";
})

// Timer
let min = 0;
let hour = 0;
let sec = 0;
let secondDrop = document.getElementById("seconds");
let minuteDrop = document.getElementById("minutes");
let hourDrop = document.getElementById("hours");
let startTimer = document.getElementById("start-timer");
for (let num = 0; num<24; num++){
    console.log(num);
    let p = document.createElement("p");
    if (num<10){
        p.innerText = "0"+ num;
    }else p.innerText = num;
    p.id=num;
    p.addEventListener("click", function(){
        if (this.id <10){
            hour = "0" + this.id
        } else{
            hour = this.id
        }
        hourDrop.previousElementSibling.innerText = hour;
    })
    hourDrop.appendChild(p);
}
for (let num = 0; num<60; num++){
    console.log(num);
    let p = document.createElement("p");
    if (num<10){
        p.innerText = "0"+ num;
    }else p.innerText = num;
    p.id=num;
    p.addEventListener("click", function(){
        if (this.id <10){
            sec = "0" + this.id
        } else{
            sec = this.id
        }
        secondDrop.previousElementSibling.innerText = sec;
    })
    secondDrop.appendChild(p);
}
for (let num = 0; num<60; num++){
    console.log(num);
    let p = document.createElement("p");
    if (num<10){
        p.innerText = "0"+ num;
    }else p.innerText = num;
    p.id=num;
    p.addEventListener("click", function(){
        if (this.id <10){
            min = "0" + this.id
        } else{
            min = this.id
        }
        minuteDrop.previousElementSibling.innerText = min;
    })
    minuteDrop.appendChild(p);
}
let timerGo;
let theTimer = document.getElementById("the-timer");
theTimer.innerText = "00:00:00"
var timerDate = new Date();

startTimer.addEventListener("click", function(){
    hour=parseInt(hour)
    console.log(min)
    min=parseInt(hour)
    sec=parseInt(sec)
    timerDate.setHours(hour,min,sec,0);
    let zero = hour + min + sec;
    console.log(zero)
    
        timerGo = setInterval(function(){
            if (zero>0){
            
                timerDate.setSeconds(timerDate.getSeconds()-1);
                timerTime = timerDate.toString().split(" ")[4];
                theTimer.innerText = timerTime;
            } else {
                console.log("zero")
                clearInterval(timerGo);
                timerDate.setHours(0,0,0,0);
                timerTime = timerDate.toString().split(" ")[4];
                theTimer.innerText = timerTime;
            }
        }, 1000)
})

//stop buttons don't stop timer
//laps wont stay short