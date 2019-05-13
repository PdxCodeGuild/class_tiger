/*

App randomly redirects user to another page.
  Array of URLs as strings, randomly pick one using Math.randomly
  redirect to it using window.location

Use timing events to show a 5 second countdown to user

Use iframes to create a stumbleupon clone


*/
var randomizerBtn = document.getElementById('randomizerBtn');
var urlArray = ['https://en.wikipedia.org/wiki/One_Ring','https://en.wikipedia.org/wiki/Peregrin_Took','https://en.wikipedia.org/wiki/Nazg%C3%BBl','https://en.wikipedia.org/wiki/Tom_Bombadil','https://en.wikipedia.org/wiki/Arnor','https://en.wikipedia.org/wiki/Corsairs_of_Umbar','https://en.wikipedia.org/wiki/Battle_of_the_Pelennor_Fields','https://en.wikipedia.org/wiki/Gr%C3%ADma_Wormtongue','https://en.wikipedia.org/wiki/Th%C3%A9oden','https://en.wikipedia.org/wiki/Saruman','https://en.wikipedia.org/wiki/Sauron','https://en.wikipedia.org/wiki/Gandalf','https://en.wikipedia.org/wiki/Treebeard','https://en.wikipedia.org/wiki/Middle-earth','https://en.wikipedia.org/wiki/Shire_(Middle-earth)','https://en.wikipedia.org/wiki/Frodo_Baggins','https://en.wikipedia.org/wiki/Mount_Doom','https://en.wikipedia.org/wiki/Barad-d%C3%BBr','https://en.wikipedia.org/wiki/Aragorn','https://en.wikipedia.org/wiki/Rohan_(Middle-earth)','https://en.wikipedia.org/wiki/Legolas','https://en.wikipedia.org/wiki/Gimli_(Middle-earth)','https://en.wikipedia.org/wiki/Boromir','https://en.wikipedia.org/wiki/Meriadoc_Brandybuck','https://en.wikipedia.org/wiki/Samwise_Gamgee'];

let interval;

function randomizerFunc() {
  let myRandomIndex = Math.floor(Math.random()*urlArray.length);
  // window.location.assign(urlArray[myRandomIndex]);
  let randomURL = urlArray[myRandomIndex];
  return randomURL;
}

function timerFunc () {
  clearInterval(interval);
  let timerDisplay = document.getElementById('timerDisplay');
  let counter = 5;
  
  timerDisplay.innerText= `Redirecting in ${counter}`;
  counter = 4;
  interval = setInterval(function(){
    timerDisplay.innerText= `Redirecting in ${counter}`;
    counter -= 1;
    if (counter <= -1){
      timerDisplay.innerText= 'Enjoy!';
      clearInterval(interval);
      document.getElementById('myIframe').src = randomizerFunc();

    }
  },1000);
}

randomizerBtn.addEventListener('click',timerFunc);
