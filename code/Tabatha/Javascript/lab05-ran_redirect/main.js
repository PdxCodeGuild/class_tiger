// let siteArr=[
//     "http://www.google.com",
//     "http://fonts.google.com",
//     "http://color.adobe.com/create"
// ]
let siteArr=[
    "http://google.com/search?igu=1",
]
let generate = document.getElementById("random");
let body = document.getElementsByTagName("body")[0];
let message = document.createElement("p");
body.appendChild(message);

let timer = 5;
function countdown(){
    if (timer > 0){
        message.innerText = (`Redirecting in ${timer}seconds...`);
        timer--;
        console.log(timer)
    } else {

        // let frame = document.createElement("iframe");
        let len = siteArr.length;
        let index = Math.floor((Math.random() * (len)) % len);
        // window.location.href = siteArr[index];
        // frame.src = siteArr[index];
        body.innerHTML = `<iframe src='${siteArr[index]}'></iframe>`
    }
}
generate.addEventListener("click", function(){
    setInterval(countdown, 1000);
})
    