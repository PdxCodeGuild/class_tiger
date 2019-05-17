/*
Lab 09 Random Quotes

Set up favqs.com API to show random quote

need to set up pagination so that all results for this list of quotes is displayed

use some sort of 'test if last page' logic to run function to keep displaying more Quotes
until the user reaches the last page.


encodeURIComponent('?x=test')
*/

var responseSection = document.querySelector('#response-section');
let nextPageBtn = document.getElementById('next-page');
let previousPageBtn = document.getElementById('previous-page');
let pageNums = document.getElementById('page-numbers');
let pageNumBtn = document.querySelector('.page-number-btn')
var page = 1;


function nextPageQuotes (){
  responseSection.innerHTML = "";
  page += 1;
  let pageNumBtns = document.getElementsByClassName('page-number-btn');

  let l = pageNumBtns.length;
  let checkArray = [];
  for (let i = 0; i < l ; i++){
    checkArray.push(parseInt(pageNumBtns[i].innerText));
  }

  console.log(checkArray);

  if (checkArray.includes(page) == false){
    let pageNum = document.createElement('button');
    pageNum.innerText = `${page}`;
    pageNum.classList.add('button-primary');
    pageNum.classList.add('page-number-btn');
    pageNums.appendChild(pageNum);
    pageNum.addEventListener('click',pageNumQuotes);
  }

  getQuotes();
};

function previousPageQuotes (){
  responseSection.innerHTML = "";
  page -= 1;
  // console.log(page);
  getQuotes();
};

function pageNumQuotes () {
  page = parseInt(this.innerText);
  responseSection.innerHTML = "";
  // console.log(page);

  getQuotes();
};

function getQuotes(){

  let req = new XMLHttpRequest();

  req.addEventListener("progress",function(e) {
    // console.log(e.loaded);
    responseSection.innerHTML = "<p>loading...</p>";

  });
  req.addEventListener("error",function(e) {
    // console.log(e.status);
    responseSection.innerHTML = "<p>Error, try again later</p>";

  });

  req.addEventListener("load",function(e) {
    // console.log(req.responseText); // returns the raw text response
    let response = JSON.parse(req.responseText);
    // console.log(response); // returns a Javascript object

    // console.log(response.last_page);
    if (response.last_page == true){
      nextPageBtn.style.display = "none";
    }else{
      nextPageBtn.style.display = "inline";
    }

    if (page <= 1){
      previousPageBtn.style.display = "none";
    }else{
      previousPageBtn.style.display = "inline";

    }

    for (let i = 0; i < response.quotes.length;i++) {
      let resultHTML = `
      <hr>
      <p>${response.quotes[i].body}</p>
      <p><i><a href="${response.quotes[i].url}">${response.quotes[i].author}</a></i></p>
      `
      responseSection.innerHTML += resultHTML;
    }
  });

  req.open("GET","https://favqs.com/api/quotes?page="+page.toString()+"&filter=" + 'knowledge&type=tag')

  req.setRequestHeader("authorization", `Token token=${token}`);

  req.send();
};

getQuotes();

pageNumBtn.addEventListener('click',pageNumQuotes);
previousPageBtn.addEventListener('click',previousPageQuotes);
nextPageBtn.addEventListener('click',nextPageQuotes);
