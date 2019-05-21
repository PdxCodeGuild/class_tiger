let target = document.getElementById("ranquote");
let quoteBtn = document.getElementById("getrandom");
let page = 28
let response;
function run(page){
    let req = new XMLHttpRequest();

    req.addEventListener("progress", function(e) {
    });
    req.addEventListener("error", function(e) {
        target.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function(e) {
        response = JSON.parse(req.responseText);
            for (i=0; i<response.quotes.length; i++){
                let quote = response.quotes[i];
                let newQuote = document.createElement("div");
                newQuote.innerHTML = `<blockquote>${quote.body}</blockquote>
                <p><i>-${quote.author}</i></p>`
                target.appendChild(newQuote);
            }
            console.log(this.response)
            if (page > 1){
                prevBtn.disabled = false;
            } else {
                prevBtn.disabled = true;

            }
            if (response.last_page){
                nextBtn.disabled = true;
            } else {
                nextBtn.disabled = false;

            }
    });
    req.addEventListener("abort", function(e) {
        
    })
        // req.open("GET", "https://favqs.com/api/quotes/?hidden=1");
        req.open("GET", `https://favqs.com/api/quotes/?filter=funny&page=${page}`);
        // req.open("GET", `https://favqs.com/api/quotes?page="4${page_id}"&filter="${text}`);
        req.setRequestHeader("Authorization", 'Token token="a28ea03f68455c6ad65e2f981b7f2367"');
        
        req.send();
   
}
    run(page)
    let nextBtn = document.getElementById("next");
    let prevBtn = document.getElementById("prev")
    prevBtn.disabled = true;

    nextBtn.addEventListener("click", function(){
        console.log(response.last_page);
        if (!response.last_page){

            page++
            target.innerText="";
            run(page)
        }
    })
    prevBtn.addEventListener("click", function(){
        if (response.page > 1){

            page--
            target.innerText="";
            run(page)
        } else 
        return
    })