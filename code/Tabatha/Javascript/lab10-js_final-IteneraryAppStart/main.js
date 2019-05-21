var mapBlock = document.getElementById("map");
let addBtn = document.getElementById("directions");
let trips = document.getElementById("trip-list");
let tripArr = ["Portland, OR", "Eugene, OR", "Salem, OR", "Medford, OR"];
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
    // beginBtn = document.getElementById("begin");
    // // dayStart = document.getElementById("start");
    // startDiv = document.getElementById("start-div");
    stopInput = document.getElementById("end");
    // addStop = document.getElementById("add-stop");
    // addStop.style.display = "none";
    // beginBtn.addEventListener("click", function() {
    //     startPos = document.getElementById("start").value;
    //     let newStop = document.createElement("list");
    //     let newLoc = document.createElement("p");
    //     newLoc.className = "origin";
    //     newLoc.innerText = startPos;
    //     newStop.appendChild(newLoc);
    //     trips.appendChild(newStop);
    //     startDiv.style.display = "none";
    //     addStop.style.display = "inline";
    //     return startPos

    // })
    
        
        
        
        
        //     })
        
        // }
        function reDraw(){
            for (i=0; i<tripArr.length; i++) {
                tripArr[i]
                
                let newStop = document.createElement("div");
                let newLoc = document.createElement("p");
                newLoc.className = "destination";
                // let newEnd = document.createElement("p");
                // newEnd.className = "destination";
                // let newDur = document.createElement("p");
                // newDur.className = "duration";
                newLoc.innerText = tripArr[i];
                // // newEnd.innerText = response.routes[0].legs[0].end_address;
                // newDur.innerText = response.routes[0].legs[0].duration.text;
                var remove = document.createElement("button");
                remove.id = `${i}`
                remove.className = "check";
                remove.innerHTML ="<i class='fas fa-trash-alt'></i>";
                var begin = document.createElement("button");
                begin.id = `${i}`
                begin.className = "begin";
                begin.innerHTML ='<i class="far fa-play-circle"></i>';
                begin.addEventListener("click", function(){
                    endPos = this.parentElement.firstElementChild.innerText;
                    startPos = this.parentElement.previousSibling.firstElementChild.innerText;
                    calculateAndDisplayRoute(directionsService, directionsDisplay);
                    console.log(endPos, startPos, this)
                })
                var moveUp = document.createElement("button");
                moveUp.className = "move-up";
                moveUp.id = `${i}`;
                moveUp.innerHTML = '<i class="far fa-arrow-alt-circle-up"></i>';
                moveUp.addEventListener("click", function(){
                    // moveMeUp = this.parentElement;
                    // prev = moveMeUp.previousSibling;
                    // trips.insertBefore(moveMeUp, prev);
                    thisStop = this.parentElement.firstElementChild.innerText;
                    thisIndex = this.id
                    tripArr.splice((thisIndex), 1);
                    tripArr.splice(parseInt(thisIndex)-1, 0, thisStop);
                    trips.textContent = "";
                    reDraw();                    
                })
                var moveDown = document.createElement("button");
                moveDown.className = "move-down";
                moveDown.id = `${i}`;
                moveDown.innerHTML = '<i class="far fa-arrow-alt-circle-down"></i>';
                moveDown.addEventListener("click", function(){
                    console.log(this.id)
                    // moveMeDown = this.parentElement;
                    // next = moveMeDown.nextSibling;
                    // next2 = next.nextSibling,
                    // trips.insertBefore(moveMeDown, next2);
                    thisStop = this.parentElement.firstElementChild.innerText;
                    thisIndex = this.id
                    tripArr.splice((thisIndex), 1);
                    tripArr.splice(parseInt(thisIndex)+1, 0, thisStop);
                    console.log(parseInt(thisIndex)+1)
                    trips.textContent = "";
                    reDraw();
                })
                remove.addEventListener("click", function(){
                    console.log("clicked")
                    this.parentElement.remove();
                })
                newStop.appendChild(newLoc);
                newStop.appendChild(remove);
                newStop.appendChild(moveUp);
                newStop.appendChild(moveDown);
                newStop.appendChild(begin);
                newStop.appendChild(document.createElement("br"));
        trips.appendChild(newStop);
    }
    }
    addBtn.addEventListener("click", function(){
        tripArr.push(stopInput.value);
        trips.innerText="";
        reDraw();
    })
}
    function calculateAndDisplayRoute(directionsService, directionsDisplay) {
        
        directionsService.route({
            origin: `${startPos}`,
            destination: `${endPos}`,
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
                showTime.innerText = result;
                console.log(result);
                // document.getElementById("start").value = endPos;
                // document.getElementById("end").value = "";
            } else {
            window.alert('Directions request failed due to ' + status);
        }
      });
    }

    