/********************

Flickr API interaction

***********/

var responseSection = document.querySelector('#response-section');
var responseSection2 = document.querySelector('#response-section2');
var responseSection3 = document.querySelector('#response-section3');
var goBtn = document.getElementById('go-btn');
var myInput = document.getElementById('my-input').value;
var inputObj = document.getElementById('my-input');
var galleryH1 = document.getElementById('gallery-h1');
var lightbox = document.getElementById('lightbox');
var lightboxImg = document.getElementById('lightbox-img');
var closeBtn = document.getElementById('close-btn');
var flickr = new Flickr(token);
var htmlContent;

function closeBtnFunc(){
  lightbox.style.top = '-1000px';
}

function dispLightbox() {
  imgSrc = this.getAttribute("src");
  lightboxImg.setAttribute("src",imgSrc);
  lightbox.style.top = '0px';
  console.log(imgSrc);
}

function random15Func () {
  let random15 = [];

  for(let i = 0; i < 15; i++) {

    myRandom = Math.floor(Math.random()*100)
    while (random15.includes(myRandom)){
      myRandom = Math.floor(Math.random()*100)
    }
    random15.push(myRandom);
  }
  console.log(random15);
  return random15;
}

function goBtnFunc () {
  myInput = document.getElementById('my-input').value;
  galleryH1.innerText = myInput.toUpperCase();
  photoSearch(myInput);
}

function photoSearch(myInput){

  random15 = random15Func();
  let responseSectionArray = [responseSection,responseSection2,responseSection3];
  responseSectionArray.forEach(function(element){
    element.innerHTML = "";
  })

  flickr.photos.search({
    text: myInput

  }).then(function (res) {
    console.log('yay!', res.body);
    let myphotos = res.body.photos.photo;

    for (let i=0; i < 5 ; i++){
      createImgElem(random15[i],0);
    }
    for (let i=6; i < 11 ; i++){
      createImgElem(random15[i],1);
    }
    for (let i=11; i < 16 ; i++){
      createImgElem(random15[i],2);
    }
    function createImgElem(input,num) {
      let photo = myphotos[input];
      let imgElem = document.createElement('img');
      imgElem.setAttribute('src',`https://farm${photo.farm}.staticflickr.com/${photo.server}/${photo.id}_${photo.secret}.jpg`);
      imgElem.classList.add('my-img');
      imgElem.classList.add(`response-section${num}`);
      imgElem.addEventListener('click',dispLightbox);
      responseSectionArray[num].appendChild(imgElem);
    }

  }).catch(function (err) {
    console.error('bonk', err);
  });
}

photoSearch('landscape');

inputObj.addEventListener("keydown", function(event){
  if(event.keyCode === 13){
    event.preventDefault();
    goBtn.click();
  }
});
goBtn.addEventListener('click',goBtnFunc);
closeBtn.addEventListener('click',closeBtnFunc);
