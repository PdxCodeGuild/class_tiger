let req = new XMLHttpRequest();
let target = document.getElementById("target");
let target2=document.getElementById("target2")
req.addEventListener("progress", function(e) {
});
req.addEventListener("error", function(e) {
    target.innerText = "Error. Please Try Again.";
});
req.addEventListener("load", function(e) {
    let response = JSON.parse(req.responseText);
    let top_list=[];   
    let next_list=[];
    for(let i=0; i<5; i++){      
        let print=  `
        <i><a href="${response.artists.artist[i].url}">${response.artists.artist[i].name}</a></i>`
        top_list.push(print)
        let no_c=top_list.join('')
        target.innerHTML=no_c   
    }
    for(let d=5; d<10; d++){      
        let print=  `
        <i><a href="${response.artists.artist[d].url}">${response.artists.artist[d].name}</a></i>`
        next_list.push(print)
        let no_comma=next_list.join('')
        target2.innerHTML=no_comma
    } 
})
req.open("GET", "http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=31744144d1f0d44dac39e3dd9f62eacd&format=json");
req.setRequestHeader("Authorization", 'Token token="31744144d1f0d44dac39e3dd9f62eacd"');
req.send()




