var mapBlock = document.getElementById("map");
let addBtn = document.getElementById("directions");
let trips = document.getElementById("trip-list");
var res;
var infoWindow;
var startPos;
var endPos;
var dayStart;
    function initMap() {
    //   initialize map
        var directionsService = new google.maps.DirectionsService;
        var directionsDisplay = new google.maps.DirectionsRenderer;
        map = new google.maps.Map(mapBlock, {
            center: {lat: -34.397, lng: 150.644},
            zoom: 6
        });
        infoWindow = new google.maps.InfoWindow;
        directionsDisplay.setMap(map);


        // check for geolocation in browser
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
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
    beginBtn = document.getElementById("begin");
    // dayStart = document.getElementById("start");
    startDiv = document.getElementById("start-div");
    stopInput = document.getElementById("end");
    addStop = document.getElementById("add-stop");
    addStop.style.display = "none";
    beginBtn.addEventListener("click", function() {
        startPos = document.getElementById("start").value;
        let newStop = document.createElement("list");
        let newStart = document.createElement("p");
        newStart.className = "origin";
        newStart.innerText = startPos;
        newStop.appendChild(newStart);
        trips.appendChild(newStop);
        startDiv.style.display = "none";
        addStop.style.display = "inline";
        return startPos

    })
    addBtn.addEventListener("click", function(){
            calculateAndDisplayRoute(directionsService, directionsDisplay);
            startPos = trips.lastElementChild.firstElementChild.innerText;
            endPos = document.getElementById("end").value;


    
            
        })
        
    }
    function newDest (response){
        let newStop = document.createElement("list");
        let newStart = document.createElement("p");
        newStart.className = "origin";
        let newEnd = document.createElement("p");
        newEnd.className = "destination";
        let newDur = document.createElement("p");
        newDur.className = "duration";
        newStart.innerText = response.routes[0].legs[0].start_address;
        // newEnd.innerText = response.routes[0].legs[0].end_address;
        newDur.innerText = response.routes[0].legs[0].duration.text;
        var remove = document.createElement("button");
        remove.className = "check";
        remove.innerHTML ="<i class='fas fa-trash-alt'></i>";
        var moveUp = document.createElement("button");
        moveUp.className = "move-up";
        moveUp.innerHTML = "<i class='fas fa-sort-up'></i>";
        moveUp.addEventListener("click", function(){
            moveMeUp = this.parentElement;
            prev = moveMeUp.previousSibling;
            trips.insertBefore(moveMeUp, prev);
        })
        var moveDown = document.createElement("button");
        moveDown.className = "move-down";
        moveDown.innerHTML = "<i class='fas fa-sort-down'></i>";
        moveDown.addEventListener("click", function(){
            moveMeDown = this.parentElement;
            next = moveMeDown.nextSibling;
            next2 = next.nextSibling,
            trips.insertBefore(moveMeDown, next2);
        })
        remove.addEventListener("click", function(){
            console.log("clicked")
            this.parentElement.remove();
        })
        // var lineBreak = document.createElement("br");
        newStop.appendChild(newStart);
        // newStop.appendChild(newEnd);
        newStop.appendChild(newDur);
        newStop.appendChild(moveUp);
        newStop.appendChild(moveDown);
        newStop.appendChild(remove);
        newStop.appendChild(document.createElement("br"));
        trips.appendChild(newStop);
    }
    function calculateAndDisplayRoute(directionsService, directionsDisplay) {
        
        directionsService.route({
            origin: startPos,
            destination: endPos,
            travelMode: 'DRIVING'
        }, function(response, status) {
            if (status === 'OK') {
                directionsDisplay.setDirections(response);
                console.log(response)
                let showTime = document.getElementById("travel-time");
                var date = new Date(null);
                let totalSeconds;
                totalSeconds = parseInt(response.routes[0].legs[0].duration.value);
                date.setSeconds(totalSeconds); // specify value for SECONDS here
                var result = date.toISOString().substr(11, 8);
                newDest(response)
                showTime.innerText = result;
                console.log(endPos);
                document.getElementById("start").value = endPos;
                document.getElementById("end").value = "";
            } else {
            window.alert('Directions request failed due to ' + status);
        }
      });
    }

    