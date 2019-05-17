let target = document.getElementById("target");
let button = document.getElementById("button");
let keyword = document.getElementById("keyword");


button.addEventListener("click", function(e) {
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

        console.log(response);
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

    });
    let link = "https://favqs.com/api/quotes?";

    let search_word = encodeURI(keyword.value);
    var url = `${link}?filter=${search_word}`;
    req.open("GET", url);
    req.setRequestHeader("Authorization", 'Token token="722d71297df4d3232791f1aaca95584f"');
    req.send()
});


// let pager = `<ul class="pager">
//   <li class="previous"><a href="#">Previous</a></li>
//   <li class="next"><a href="#">Next</a></li>
// </ul>`;

// function Page(search_word) {
//     let target = document.getElementById("target");
//     let button = document.getElementById("button");
//     let keyword = document.getElementById("keyword");
//     this.search_word = keyword.value;
//
//     this.load = button.addEventListener("click", function(e) {
//     let req = new XMLHttpRequest();
//     req.addEventListener("progress", function(e) {
//         console.log(e.loaded);
//         return response = "Loading...";
//     });
//     req.addEventListener("error", function(e) {
//         console.log(e.status);
//         return response = "Cannot load quote. Try again later!";
//     });
//     req.addEventListener("load", function(e) {
//         console.log(req.responseText);
//         return response = JSON.parse(req.responseText);
//         // return response;
//     });
//     this.request();
//     });
//
//     this.request = function () {
//         let link = "https://favqs.com/api/quotes?";
//         var url = `${link}?filter=${this.search_word}`;
//         req.open("GET", url);
//         req.setRequestHeader("Authorization", 'Token token="722d71297df4d3232791f1aaca95584f"');
//         req.send()
//     }
//
//
// };