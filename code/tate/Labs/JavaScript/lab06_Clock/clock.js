let displayDate = document.getElementById('display-date');
function addZero(stringNum) {
  num = parseInt(stringNum);
  if (num < 10){
    return `0${stringNum}`;
  } else {
    return stringNum;
  }
}

function clockFunc() {
  let d = new Date();
  let hours = d.getHours();
  let minutes = d.getMinutes();
  let seconds = d.getSeconds();
  displayDate.innerText = `${addZero(hours)}:${addZero(minutes)}:${addZero(seconds)}`;
}
clockFunc();
setInterval(function() {
  clockFunc();
},1000);
