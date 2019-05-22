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
var photoDescription = document.getElementById('photo-description');
var photoTitle = document.getElementById('photo-title');
var photoOwner = document.getElementById('photo-owner');
var photoTags = document.getElementById('photo-tags');
var photoViews = document.getElementById('photo-views');

var closeBtn = document.getElementById('close-btn');
var flickr = new Flickr(token);
var htmlContent;

function dispLightbox() {
/* Light box is displayed, fixed modal that slides down from the top of the page
  when an image is clicked. This runs a new flickr request to get information
  about that photo and display it within the modal. 'X' in the upper right closes
  the modal.
 */
  function getInfo () {
    flickr.photos.getInfo({
      photo_id: photoId
    }).then(function (res) {
      console.log('got photo info!', res.body);
      let lightboxPhoto = res.body.photo;
      let tags = lightboxPhoto.tags.tag;
      photoTitle.innerText = lightboxPhoto.title['_content'];
      photoDescription.innerText = lightboxPhoto.description['_content'];
      photoOwner.innerText = lightboxPhoto.owner['username'];
      photoTags.innerText = '';
      photoViews.innerText = lightboxPhoto.views;
      for (let i = 0; i < tags.length ; i ++){
        photoTags.innerHTML += tags[i]._content + ', ';
      }
    }).catch(function (err) {
      console.error('bonk', err);
    });
  }
  let photoId = this.getAttribute('id')
  imgSrc = this.getAttribute("src");
  lightboxImg.setAttribute("src",imgSrc);
  lightbox.style.top = '0px';
  console.log(this.getAttribute('id'));
  getInfo();
}
function closeBtnFunc(){
  lightbox.style.top = '-1200px';
}

function random15Func (length) {
/*
  Generates an array of 15 random numbers. These will be used
  to display a more varied collection of images for the keyword search.
*/

  let random15 = [];
  for(let i = 0; i < 15; i++) {

    myRandom = Math.floor(Math.random()*length)
    while (random15.includes(myRandom)){
      myRandom = Math.floor(Math.random()*length)
    }
    random15.push(myRandom);
  }
  return random15;
}

function goBtnFunc () {
  /* Initiates the main photoSearch function and updates the H1 to then
  keyword being searched
  */
  myInput = document.getElementById('my-input').value;
  galleryH1.innerText = myInput.toUpperCase();
  photoSearch(myInput);
}

function photoSearch(myInput){
  /*
    Updates the Response area with 15 images. These images are pulled from the
    Flickr API based off the keyword entered by the user.
  */
  let responseSectionArray = [responseSection,responseSection2,responseSection3];
  responseSectionArray.forEach(function(element){
    element.innerHTML = "";
  })
  flickr.photos.search({
    text: myInput
  }).then(function (res) {
    console.log('yay!', res.body);
    let myphotos = res.body.photos.photo;
    let random15 = random15Func(myphotos.length);
    for (let i=0; i < 5 ; i++){
      createImgElem( random15[i],0);
    }
    for (let i=5; i < 10 ; i++){
      createImgElem( random15[i],1);
    }
    for (let i=10; i < 15 ; i++){
      createImgElem( random15[i],2);
    }
    function createImgElem(input,num) {
      photo = myphotos[input];
      let imgElem = document.createElement('img');
      imgElem.setAttribute('src',`https://farm${photo.farm}.staticflickr.com/${photo.server}/${photo.id}_${photo.secret}.jpg`);
      imgElem.classList.add('my-img');
      imgElem.setAttribute('id',`${photo.id}`);
      imgElem.addEventListener('click',dispLightbox);
      responseSectionArray[num].appendChild(imgElem);
    }
  }).catch(function (err) {
    console.error('bonk', err);
  });
}

// Event listener so that the 'Enter' Key may be used in the search input
inputObj.addEventListener("keydown", function(event){
  if(event.keyCode === 13){
    event.preventDefault();
    goBtn.click();
  }
});

// Event Listeners for 'Go' and 'X' Buttons
goBtn.addEventListener('click',goBtnFunc);
closeBtn.addEventListener('click',closeBtnFunc);

// Run the photo search function on page load using 'Tate Shepherd Photography'
photoSearch('Tate Shepherd Photography');
