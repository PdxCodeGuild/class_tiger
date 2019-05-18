let target = document.getElementById("target");
let search_btn = document.getElementById("button");
let keyword = document.getElementById("keyword");
let next_btn = document.getElementById("next");
let previous_btn = document.getElementById("previous");
let footer = document.getElementById("pager");
let search;
let page =1;



search_btn.addEventListener('click',retrieve);
///increment and decrement pages of content
next_btn.addEventListener('click', function () {
    page ++;
    retrieve();
});
previous_btn.addEventListener('click', function () {
    page --;
    retrieve();
});
///for a new search update
keyword.addEventListener('change',function(){
    search = target.value;
});
//run AJAX
function retrieve(){
    let req = new XMLHttpRequest();
    req.addEventListener("progress", function(e) {
        console.log(e.loaded);
        target.innerText = "Loading...";
    });
    req.addEventListener("error", function(e) {
        console.log(e.status);
        target.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function(e) {
        console.log(req.responseText);
        let response = JSON.parse(req.responseText);
        ///call display here so retrieve does both
        display(response);
    });


        let link = "https://favqs.com/api/quotes?";

    search = encodeURI(keyword.value);
    var url = `${link}?filter=${search}&page=${page}`;
    req.open("GET", url);
    req.setRequestHeader("Authorization", `Token token=${Token}`);
    req.send();

}


/// you don't need to return a variable created in function just call it
function display(response){

        let content = response.quotes;
        console.log(content);
        var output = '';
        for(var i in content ) {
             let resultHTML = `
            <p>${content[i].body}</p>
            <p><i><a href="${content[i].url}">${content[i].author}</a></i></p>
            `;
            output += resultHTML;
            }
            target.innerHTML = output;

        if(response.page === 1){
            next_btn.style.display = 'inline';
            footer.style.justifyContent = 'flex-end';
            previous_btn.style.display = 'none';
        }
        else if(response.last_page === true){
            next_btn.style.display = 'none';
            previous_btn.style.display = 'inline';
            footer.style.justifyContent = 'flex-start';
        }
        else{
            next_btn.style.display = 'inline';
            previous_btn.style.display = 'inline';
            footer.style.justifyContent = 'space-between';
        }
}



