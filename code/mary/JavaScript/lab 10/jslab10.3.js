let req3 = new XMLHttpRequest();
let search = document.getElementById("search");
let input = document.getElementById("input");
let submit = document.getElementById("sub");

submit.addEventListener("click", function(){
    req3.addEventListener("progress", function(e) {
    });
    req3.addEventListener("error", function(e) {
        target.innerText = "Error. Please Try Again.";
    });
    req3.addEventListener("load", function(e) {
        let response = JSON.parse(req3.responseText); 
        let sim = []
        let cleaned= response.artist.bio.content.replace('<a href="https://www.last.fm/music/'+response.artist.name.replace(/ /g, '+')+'">Read more on Last.fm</a>. User-contributed text is available under the Creative Commons By-SA License; additional terms may apply.', '')
        for(let d=0; d<response.artist.similar.artist.length; d++){         
            let c = `<a href="${response.artist.similar.artist[d].url}"> ${response.artist.similar.artist[d].name}</a>`
            sim.push(c)
            let nope = sim.join('')
            let info = `
                <h2>${response.artist.name}</h2><br/>
                <p>${cleaned}</p><i><a href="https://www.last.fm/music/${input.value.replace(' ', '+')}">Find tracks and photos</a></i><br/><h4>Explore Similar Artists:</h4><h5>${nope}</h5>
            
        `
        search.innerHTML=info
        
        }
    })
req3.open("GET", "http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist="+input.value+"&api_key=31744144d1f0d44dac39e3dd9f62eacd&format=json");
req3.setRequestHeader("Authorization", 'Token token="31744144d1f0d44dac39e3dd9f62eacd"');
req3.send()
});