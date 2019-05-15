let clockNav = document.getElementById('clock-nav');
let stopwatchNav = document.getElementById('stopwatch-nav');
let timerNav = document.getElementById('timer-nav');

let stopwatch = document.querySelector('#stopwatch');
let clock = document.querySelector('#clock-app');
let timer = document.querySelector('#timer');

function clockNavFunc() {
  stopwatch.style.display = 'none';
  clock.style.display = 'flex';
  clock.style.justifyContent = 'center';
  timer.style.display = 'none';


  clockNav.classList.add("active-nav");
  timerNav.classList.remove("active-nav");
  stopwatchNav.classList.remove("active-nav");
}


function stopwatchNavFunc() {
  stopwatch.style.display = 'flex';
  stopwatch.style.justifyContent = 'center';
  clock.style.display = 'none';
  timer.style.display = 'none';


  clockNav.classList.remove("active-nav");
  timerNav.classList.remove("active-nav");
  stopwatchNav.classList.add("active-nav");

}


function timerNavFunc() {
  timer.style.display = 'flex';
  timer.style.justifyContent = 'center';
  clock.style.display = 'none';
  stopwatch.style.display = 'none';

  clockNav.classList.remove("active-nav");
  timerNav.classList.add("active-nav");
  stopwatchNav.classList.remove("active-nav");

}


clockNav.addEventListener('click',clockNavFunc);
stopwatchNav.addEventListener('click',stopwatchNavFunc);
timerNav.addEventListener('click',timerNavFunc);
