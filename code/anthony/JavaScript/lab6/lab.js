// Menu
let menClock = document.getElementById('menuclock');
let menStop = document.getElementById('menustopwatch');
let menCount = document.getElementById('menucountdown');
let clockDiv = document.getElementById('clock-face');
let stopDiv = document.getElementById('stop-watch');
let countDiv = document.getElementById('countdown');

menClock.addEventListener('click', function () {
    clockDiv.style.display = "block";
    stopDiv.style.display = "none";
    countDiv.style.display = "none";
})
menStop.addEventListener('click', function () {
    clockDiv.style.display = "none";
    stopDiv.style.display = "block";
    countDiv.style.display = "none";
})
menCount.addEventListener('click', function () {
    clockDiv.style.display = "none";
    stopDiv.style.display = "none";
    countDiv.style.display = "block";
})





// Clock
let clockFace = document.getElementById('clock-face');
let clock = document.createElement('p');
let time

function digit(num) {
    return num > 9 ? "" + num : "0" + num;
}


setInterval(function () {
    time = new Date();

    clock.innerText = `${digit(time.getHours())}:${digit(time.getMinutes())}:${digit(time.getSeconds())}`;

    clockFace.appendChild(clock);
}, 1000)

// Stopwatch
let stopWatch = document.getElementById('stopwatch');
let stopdiv = document.getElementById('stop-watch');
let start = document.getElementById('start');
let stop = document.getElementById('stop');
let lap = document.getElementById('lap');
let resetbtn = document.getElementById('resetbtn');
let stopwatch = new Date();
stopwatch.setHours(0, 0, 0, 0);
// console.log(stopwatch);
// stopwatch.setMinutes(0);
// stopwatch.setSeconds(0);
// stopwatch.setMilliseconds(0);
let counter = 1;
resetbtn.addEventListener('click', function () {
    stopwatch.setHours(0, 0, 0, 0);
    // stopwatch.setMinutes(0);
    // stopwatch.setSeconds(0);
    // stopwatch.setMilliseconds(0);

    stopWatch.innerText = `${digit(stopwatch.getHours())}:${digit(stopwatch.getMinutes())}:${digit(stopwatch.getSeconds())}:${digit(stopwatch.getMilliseconds()
    )}`

    let laptimes = document.querySelectorAll('.laptime');
    for (let item of laptimes) {
        let something = item.parentNode;
        something.removeChild(item);
    }

    counter = 1;
})
let interval;
start.addEventListener('click', function () {
    clearInterval(interval);
    interval = setInterval(function () {
        stopwatch.setMilliseconds(stopwatch.getMilliseconds() + 100);
        stopWatch.innerText = `${digit(stopwatch.getHours())}:${digit(stopwatch.getMinutes())}:${digit(stopwatch.getSeconds())}:${digit(stopwatch.getMilliseconds()
            )}`
    }, 100)
})

stop.addEventListener('click', function () {
    clearInterval(interval);
})

lap.addEventListener('click', function () {
    let laptimes = document.createElement('p');
    laptimes.className = 'laptime'
    laptimes.innerText = `Lap ${counter} ${digit(stopwatch.getHours())}:${digit(stopwatch.getMinutes())}:${digit(stopwatch.getSeconds())}:${digit(stopwatch.getMilliseconds()
        )}`
    stopdiv.appendChild(laptimes);
    counter += 1;
})

// Countdown Timer
let cdbackground = document.getElementById('countdown');
let cdStart = document.getElementById('cdstart');
let cdStop = document.getElementById('cdstop');
let cdReset = document.getElementById('cdreset');
let cdHours = document.getElementById('hours');
let cdMinutes = document.getElementById('minutes');
let cdSeconds = document.getElementById('seconds');
let cdInput = document.getElementById('cdinput');
let countdownText = document.getElementById('countdown-text');

let countdownTimer = new Date();
countdownTimer.setHours(0, 0, 0, 0);
// countdownTimer.setMinutes(0);
// countdownTimer.setSeconds(0);

let cdInterval
let flash

cdHours.addEventListener('click', function () {
    countdownTimer.setHours(cdInput.value);
    cdInput.value = '';
    countdownText.innerText = `${digit(countdownTimer.getHours())}:${digit(countdownTimer.getMinutes())}:${digit(countdownTimer.getSeconds())}`;

})
cdMinutes.addEventListener('click', function () {
    countdownTimer.setMinutes(cdInput.value);
    cdInput.value = '';
    countdownText.innerText = `${digit(countdownTimer.getHours())}:${digit(countdownTimer.getMinutes())}:${digit(countdownTimer.getSeconds())}`;

})
cdSeconds.addEventListener('click', function () {
    countdownTimer.setSeconds(cdInput.value);
    cdInput.value = '';
    countdownText.innerText = `${digit(countdownTimer.getHours())}:${digit(countdownTimer.getMinutes())}:${digit(countdownTimer.getSeconds())}`;

})
cdStart.addEventListener('click', function () {
    clearInterval(cdInterval);
    cdInterval = setInterval(function () {
        countdownTimer.setSeconds(countdownTimer.getSeconds() - 1);
        countdownText.innerText = `${digit(countdownTimer.getHours())}:${digit(countdownTimer.getMinutes())}:${digit(countdownTimer.getSeconds())}`;
        if (countdownTimer.getHours() == 0) {
            if (countdownTimer.getMinutes() == 0) {
                if (countdownTimer.getSeconds() == 0) {
                    flash = setInterval(function () {
                        if (cdbackground.style.background == 'cyan') {
                            cdbackground.style.background = 'orange';
                        } else {
                            cdbackground.style.background = 'cyan';
                        }
                        clearInterval(cdInterval);
                    }, 500)
                }
            }
        }
    }, 1000)
})
cdStop.addEventListener('click', function () {
    clearInterval(cdInterval);
    clearInterval(flash);
})
cdReset.addEventListener('click', function () {
    clearInterval(cdInterval);
    countdownTimer.setHours(0, 0, 0, 0);
    countdownText.innerText = `${digit(countdownTimer.getHours())}:${digit(countdownTimer.getMinutes())}:${digit(countdownTimer.getSeconds())}`;
    cdbackground.style.background = 'white';
})