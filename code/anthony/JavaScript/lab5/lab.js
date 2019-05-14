let randomList = ["../lab1b/index.html", "../lab2b/index.html", "../lab3b/index.html", "../lab4/index.html"];
let iframe = document.querySelector('#iframe');
let message = document.querySelector('.message');
let ranBtn = document.querySelector('#ran-btn');
let stopBtn = document.querySelector('#stop-btn');


let rando = function (list) {
    return list[Math.floor(Math.random() * (list.length + 1))];
}
let counter = 10;

function countdown() {

    message.innerText = `Page will redirect in ${counter} seconds....`
    if (counter < 1) {
        iframe.setAttribute('src', rando(randomList));
        counter = 10;
    }
    counter--;
}
let interval;
ranBtn.addEventListener('click', function () {
    clearInterval(interval);
    countdown();
    interval = setInterval(countdown, 1000);
})
stopBtn.addEventListener('click', function () {
    clearInterval(interval);
})