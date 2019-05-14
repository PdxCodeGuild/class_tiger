

// let url = ['https://www.facebook.com/','https://www.instagram.com','https://twitter.com','https://www.w3schools.com'];

// // Math.floor(Math.random() * 10);     // returns a random integer from 0 to 9
// let index = Math.floor(Math.random() * url.length);
// window.location = url[index];
let timer = document.getElementById("timer");
let counter = 5;
setInterval(function() {
    timer.innerText = counter;
    if (counter === 0) {
        let url = ['https://www.facebook.com/','https://www.instagram.com','https://twitter.com','https://www.w3schools.com'];
        let index = Math.floor(Math.random() * url.length);
        window.location = url[index];
    }
    counter -= 1;
}, 1000);




