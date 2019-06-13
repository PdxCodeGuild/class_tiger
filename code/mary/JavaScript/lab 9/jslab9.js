let req = new XMLHttpRequest();
let target = document.getElementById("target");
let submit=document.getElementById("sub");
let words = document.getElementById("input");
submit.addEventListener("click", function(){
    req.addEventListener("progress", function(e) {
        console.log(e.loaded);
        target.innerText = "Loading..."
    });
    req.addEventListener("error", function(e) {
        console.log(e.status);
        target.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function(e) {
        let response = JSON.parse(req.responseText); 
        console.log(response.quotes);
        for (let i = 0; i < response.quotes.length; i++){
        let resultHTML = `
            <p>${response.quotes[i].body}</p>
            <p><i><a href="${response.quotes[i].url}">${response.quotes[i].author}</a></i></p>
            `  
        target.innerHTML = resultHTML;
        }
    })

req.open("GET", "https://favqs.com/api/quotes/?filter="+words.value);
req.setRequestHeader("Authorization", 'Token token="02be8a807f89b2e9405d27ab904d26a3"');
req.send()
});

