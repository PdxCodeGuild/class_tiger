//establish my variables
let target = document.getElementById("content");
let search_bar = document.getElementById("search");
let search_btn = document.getElementById("btn_search");
// let canvas = document.getElementById("myChart");

search_btn.addEventListener('click',retrieve);
// search_bar.addEventListener('change',function(){
//     artist = search_bar.value;});
//


//make ajax request
function retrieve() {
    let req = new XMLHttpRequest();
    // req.addEventListener("progress", function (e) {
    //     // console.log(e.loaded);
    //     target.innerText = "Loading...";
    // });
    // req.addEventListener("error", function (e) {
    //     // console.log(e.status);
    //     target.innerText = "Cannot load. Try again later!";
    // });
    req.addEventListener("load", function (e) {
        // console.log(req.responseText);
        let response = JSON.parse(req.responseText);
        ///call display here so retrieve does both
        let data = response.results;
        console.log(data);
        let kind = [];
        for (var i = 0; i < data.length; i++) {
            kind.push(data[i].kind);
        }

        let artist = [];
        for (var j = 0; j < data.length; j++) {
            artist.push(data[j].artistName);
        }

        let song = [];
        for (var l = 0; l < data.length; l++) {
            song.push(data[l].trackName);
        }

        ///getting objects
        let kinds = kind.reduce(countDuplicates, {});
        let artists = artist.reduce(countDuplicates, {});
        let songs = song.reduce(countDuplicates, {});

        // return key arrays
        let uniqueKinds = Object.keys(kinds);
        let uniqueArtists = Object.keys(artists);
        let uniqueSongs = Object.keys(songs);
        // return value arrays
        var countOfKinds = Object.keys(kinds).map(key => kinds[key]);
        var countOfArtists = Object.keys(artists).map(key => artists[key]);
        var countOfSongs = Object.keys(songs).map(key => songs[key]);

        display(uniqueKinds,countOfKinds,uniqueArtists,countOfArtists,uniqueSongs,countOfSongs);
    });

let link = 'https://itunes.apple.com/search?';
let words = encodeURI(search_bar.value);
var url = `${link}term=${words}`;
req.open("GET", url);
req.send();
}

// // return unique instance of artist/songs/kind with the word
function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}

function countDuplicates(obj, num){
  obj[num] = (++obj[num] || 1);
  return obj;
}


// create doughnut chart and add to DOM
function display(uniqueKinds,countOfKinds,uniqueArtists,countOfArtists,uniqueSongs,countOfSongs){
    console.log(uniqueKinds,countOfKinds);
    var ctx = document.getElementById('mychart').getContext('2d');
    var ctx1 = document.getElementById('mychart1').getContext('2d');
    var ctx2 = document.getElementById('mychart2').getContext('2d');
    var ctx3 = document.getElementById('mychart3').getContext('2d');
var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: uniqueKinds,
        datasets: [{
            data: countOfKinds,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
             borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {},
});

var myDoughnut = new Chart(ctx1, {
type: 'bar',
data: {
    labels: uniqueArtists,
    datasets: [{
        data: countOfArtists,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
             'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
             'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
        ],
         borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
},
options: {},
});
var myDoughnuts = new Chart(ctx2, {
type: 'line',
data: {
    labels: uniqueSongs,
    datasets: [{
        data: countOfSongs,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
         borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
},
options: {},
});
var myDough = new Chart(ctx3, {
type: 'polarArea',
data: {
    labels: uniqueKinds,
    datasets: [{
        data: countOfKinds,
        backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
        ],
         borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
    }]
},
options: {},
})};


