let quoteBtn = document.getElementById('random-btn');
let quoteListBtn = document.getElementById('random-list')
let filterBox = document.getElementById('filter-box');
let quoteDiv = document.getElementById('quote-card');
let quoteText = document.getElementById('quote-text');
let quoteList = document.getElementById('quote-list');
let bottomBtns = document.getElementById('bottom-btns');
let next = document.getElementById('next-btn');
let back = document.getElementById('back-btn');
var filter;
let page = 1;

filterBox.addEventListener('change', function () {
    filter = filterBox.value;
})

quoteListBtn.addEventListener('click', getList);

next.addEventListener('click', function () {
    page++;
    getList(page);
})

back.addEventListener('click', function () {
    page--;
    getList(page);
})

function getList(page = 1) {
    filter = encodeURIComponent(filter);
    let req = new XMLHttpRequest();

    req.addEventListener('progress', function (e) {
        console.log(e.loaded);
    })
    req.addEventListener('error', function (e) {
        console.log(e.status);
    })
    req.addEventListener('load', function (e) {
        let response = JSON.parse(req.responseText);
        generateList(response);
        // quoteText.innerText = response.quote.body;
        console.log(response);
    })
    if (filter === "undefined") {
        req.open('GET', `https://favqs.com/api/quotes/?filter=${filter}&page=${page}`);
    } else {
        req.open('GET', `https://favqs.com/api/quotes/?page=${page}`);
    }
    req.setRequestHeader('Authorization', `Token token=${TOKEN}`);

    req.send();
}

function generateList(response) {
    let itemList = document.getElementById('quote-list');
    while (itemList.hasChildNodes()) {
        itemList.removeChild(itemList.childNodes[0]);
    }
    for (let i = 0; i < response.quotes.length; i++) {
        let quoteItem = document.createElement('p');
        quoteItem.setAttribute('class', 'quote-text');
        quoteItem.innerText = `${response.quotes[i].body} -${response.quotes[i].author}`;
        quoteList.appendChild(quoteItem);
    }
    if (response.page == 1) {
        next.style.display = 'block';
        back.style.display = 'none';
    } else if (response.last_page == true) {
        next.style.display = 'none';
        back.style.display = 'block';
    } else {
        next.style.display = 'block';
        back.style.display = 'block';
    }
}


quoteBtn.addEventListener('click', generateQuote);

function generateQuote() {
    filter = encodeURIComponent(filter);

    let req = new XMLHttpRequest();

    req.addEventListener('progress', function (e) {
        console.log(e.loaded);
    })
    req.addEventListener('error', function (e) {
        console.log(e.status);
    })
    req.addEventListener('load', function (e) {
        let response = JSON.parse(req.responseText);
        quoteList.innerHTML = `<p>${response.quote.body} -${response.quote.author}</p>`;
        // quoteText.innerText = response.quote.body;
        console.log(response);
    })
    if (filter === "undefined") {
        req.open('GET', `https://favqs.com/api/qotd/?filter=${filter}`);
    } else {
        req.open('GET', `https://favqs.com/api/qotd/`);
    }
    req.setRequestHeader('Authorization', `Token token=${TOKEN}`);

    req.send();

    next.style.display = 'none';
    back.style.display = 'none';
}