let stopwatch=document.getElementById("stopwatch");
let start = document.getElementById("start");
let stop = document.getElementById("stop");
let lap=document.getElementById("lap");
let reset=document.getElementById("reset");
let time = setInterval(timer, 1000);
let d= new Date();
let counter=1;
d.setHours(0, 0, 0, 0);  
let face = `${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}:${d.getMilliseconds()
}`
stopwatch.innerHTML=face;

function timer() {
    let date = new Date();
    document.getElementById("clock").innerHTML = date.toLocaleTimeString();
}

let interval;
start.addEventListener('click', function () {
    clearInterval(interval);
    interval = setInterval(function () {
        d.setMilliseconds(d.getMilliseconds() + 100);
        stopwatch.innerText = `${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}:${d.getMilliseconds()}`
    }, 100);
});

stop.addEventListener('click', function () {
    clearInterval(interval);
});
lap.addEventListener('click', function(){
    // clearInterval(interval);
    let list = document.createElement("li");                
    let new_input = document.createTextNode(`Lap: ${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}:${d.getMilliseconds()
    }`);  
    list.appendChild(new_input);                            
    document.getElementById("list").appendChild(list);
    reset.addEventListener('click', function(){
        list.remove()
    })

})
reset.addEventListener('click', function(){
    clearInterval(interval);
    d.setHours(0, 0, 0, 0);  
    stopwatch.innerHTML = `${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}:${d.getMilliseconds()
}`
})