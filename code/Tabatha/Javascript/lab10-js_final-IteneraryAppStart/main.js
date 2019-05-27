let mapBlock = document.getElementById("map");
let addBtn = document.getElementById("directions");
let trips = document.getElementById("trip-list");
let tripArr = [{"start":"PORTLAND, OR", "route":"0:0:0", "stay":"0:0:0"}];
let res;
let infoWindow;
let startPos;
let endPos;
let dayStart;
let thisTime = "";
let prevClock;
let totalTrip;
let showRoute = false;
let time;
let tripInfo;
let thisIndex;
let directionsService;
let directionsDisplay;
function initMap() {
    //   initialize map
    directionsService = new google.maps.DirectionsService;
    directionsDisplay = new google.maps.DirectionsRenderer;
    map = new google.maps.Map(mapBlock, {
        center: {lat: -34.397, lng: 150.644},
        zoom: 6
    });
    infoWindow = new google.maps.InfoWindow;
    directionsDisplay.setMap(map);
        // check for geolocation in browser
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                let pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                infoWindow.setPosition(pos);
                infoWindow.setContent('Location found.');
                infoWindow.open(map);
            map.setCenter(pos);
        }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
        });
        } else {
            handleLocationError(false, infoWindow, map.getCenter());
        }
        function handleLocationError(browserHasGeolocation, infoWindow, pos) {
            infoWindow.setPosition(pos);
            infoWindow.setContent(browserHasGeolocation ?
                'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
      }
    }
      
stopInput = document.getElementById("end");
    function calculateTime( start=startPos, end=endPos, func) {
        directionsService.route({
            origin: start,
            destination: end,
            travelMode: 'DRIVING'
        }, function(response, status) {
            func(parseInt(response.routes[0].legs[0].duration.value))
        });
    }
    function toSeconds(string) {
        let timeString = string.split(':'),
            s = 0, m = 1;
        while (timeString.length > 0) {
            s += m * parseInt(timeString.pop(), 10);
            m *= 60;
        }
        return s;
    }
    function reDraw(){
        prevClock = currentTime.innerText;
        endPos = tripArr[0].start
        startPos = tripArr[tripArr.length-1].start
        calculateTime(startPos, endPos, function(time){
            let routeTime = document.getElementById("travel-dur");
            let date = new Date(null);
            // time = parseInt(response.routes[0].legs[0].duration.value);
            date.setSeconds(time); 
            let routeResult = date.toISOString().substr(11, 8);
            routeTime.innerText = routeResult.substr(0, 5);
        });
        for (let i=0; i<tripArr.length; i++) {
            let time = 0;
            thisIndex = i;
            let timeLeg = document.createElement("p");
            if (i>0){
                endPos = tripArr[i].start
                startPos = tripArr[i-1].start
                calculateTime(startPos, endPos, function(time){
                    let staySeconds = toSeconds(tripArr[i].stay);
                    let currentSec = toSeconds(prevClock);
                    let totalSec = staySeconds + currentSec + time;
                    let showClock =  new Date(null);
                    showClock.setSeconds(totalSec);
                    let endClock = showClock.toISOString().substr(11, 8);
                    let date = new Date(null);
                    date.setSeconds(time); 
                    let routeResult = date.toISOString().substr(11, 8); //11,5 for hh:mm
                    tripArr[i].route = routeResult;
                    console.log(i)
                    timeLeg.innerText = `${prevClock.substr(0, 5)} to ${endClock.substr(0, 5)}`;
                    prevClock = endClock;
                });
            } else if (i == 0){
                tripArr[i].route = "0:0:0";
                timeLeg.innerText = "";
            }
            let newStop = document.createElement("div");
            let newLoc = document.createElement("p");
            newLoc.className = "destination";
            newLoc.innerText = tripArr[i].start;
            let remove = document.createElement("button");
            remove.id = `${i}`
            remove.className = "trash";
            remove.innerHTML ="<i class='fas fa-trash-alt'></i>";
            let begin = document.createElement("button");
            begin.className = "begin";
            begin.innerHTML ='<i class="far fa-play-circle"></i>';
            begin.addEventListener("click", function(){
                showRoute =true;
                thisIndex = this.previousSibling.id
                thisBegin = this.id
                endPos = this.parentElement.firstElementChild.innerText;
                startPos = this.parentElement.previousSibling.firstElementChild.innerText;
                calculateAndDisplayRoute(directionsService, directionsDisplay);
            })
            let moveUp = document.createElement("button");
            moveUp.className = "move-up";
            moveUp.id = `${i}`;
            moveUp.innerHTML = '<i class="far fa-arrow-alt-circle-up"></i>';
            moveUp.addEventListener("click", function(){
                // moveMeUp = this.parentElement;
                // prev = moveMeUp.previousSibling;
                // trips.insertBefore(moveMeUp, prev);
                // thisStop = this.parentElement.firstElementChild.innerText;
                thisIndex = this.id
                let thisStop = tripArr.splice((thisIndex), 1)[0];
                tripArr.splice(parseInt(thisIndex)-1, 0, thisStop);
                trips.textContent = "";
                reDraw();                    
            })
            let moveDown = document.createElement("button");
            moveDown.className = "move-down";
            moveDown.id = `${i}`;
            moveDown.innerHTML = '<i class="far fa-arrow-alt-circle-down"></i>';
            moveDown.addEventListener("click", function(){
                // moveMeDown = this.parentElement;
                // next = moveMeDown.nextSibling;
                // next2 = next.nextSibling,
                // trips.insertBefore(moveMeDown, next2);
                thisIndex = this.id
                let thisStop = tripArr.splice((thisIndex), 1)[0];
                tripArr.splice(parseInt(thisIndex)+1, 0, thisStop);
                trips.textContent = "";
                reDraw(); 
            })
            remove.addEventListener("click", function(){
                thisIndex = this.id
                tripArr.splice((thisIndex), 1);
                this.parentElement.remove();
                trips.textContent = "";
                reDraw();
            })
            newStop.appendChild(newLoc);
            newStop.appendChild(timeLeg);
            newStop.appendChild(remove);
            newStop.appendChild(moveUp);
            newStop.appendChild(moveDown);
            newStop.appendChild(begin);
            newStop.appendChild(document.createElement("br"));
    trips.appendChild(newStop);
    }
}
let currentTime = document.getElementById("travel-time");
currentTime.innerText = new Date().toString().split(" ")[4];
let stayH = 0;
let stayM = 0;
let minuteDrop = document.getElementById("minutes");
let hourDrop = document.getElementById("hours");
for (let num = 0; num<24; num++){
    let p = document.createElement("p");
    if (num<10){
        p.innerText = "0"+ num;
    }else {p.innerText = num;
    }
    p.id=num;
    p.addEventListener("click", function(){
        if (this.id <10){
            stayH = "0" + this.id
        } else{
            stayH = this.id
        }
        hourDrop.previousElementSibling.innerText = stayH;
    })
    hourDrop.appendChild(p);
}
for (let num = 0; num<60; num++){
    let p = document.createElement("p");
    if (num<10){
        p.innerText = "0"+ num;
    }else p.innerText = num;
    p.id=num;
    p.addEventListener("click", function(){
        if (this.id <10){
            stayM = "0" + this.id
        } else{
            stayM = this.id
        }
        minuteDrop.previousElementSibling.innerText = stayM;
    })
    minuteDrop.appendChild(p);
}
addBtn.addEventListener("click", function(){
    stay= `${stayH}:${stayM}:00`;
    startPos = tripArr[tripArr.length-1].start;
    endPos = stopInput.value;
    calculateTime(startPos, endPos, function(time){
        tripArr.push({"start":`${stopInput.value}`, "route":`${time}`, "stay":`${stay}`});
        trips.innerText="";
        reDraw();
    });
})
function calculateAndDisplayRoute(directionsService, directionsDisplay, start=startPos, end=endPos) {
    directionsService.route({
        origin: start,
        destination: end,
        travelMode: 'DRIVING'
    }, function(response, status) {
        if (status === 'OK') {
            let routeTime = document.getElementById("travel-time");
            let date = new Date(null);
            time = parseInt(response.routes[0].legs[0].duration.value);
            date.setSeconds(time); 
            let routeResult = date.toISOString().substr(11, 8);
            routeTime.innerText = routeResult;
            newTime = document.getElementById(`time${thisIndex}`);
            if (showRoute){
                directionsDisplay.setDirections(response);
            }
            return time;
        } else {
        window.alert('Directions request failed due to ' + status);
    }
    });
}