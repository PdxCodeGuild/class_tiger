/********************

Flickr API interaction

***********/

var responseSection = document.querySelector('#response-section');
var responseSection2 = document.querySelector('#response-section2');
var responseSection3 = document.querySelector('#response-section3');
var goBtn = document.getElementById('go-btn');

var flickr = new Flickr(token);
var htmlContent;

function photoSearch(){
  flickr.photos.search({
    text: 'mountains'

  }).then(function (res) {
    console.log('yay!', res.body);
    let myphotos = res.body.photos.photo;

    function createImgElem(i,section) {
      let photo = res.body.photos.photo[i];

      let imgElem = document.createElement('img');
      imgElem.setAttribute('src',`https://farm${photo.farm}.staticflickr.com/${photo.server}/${photo.id}_${photo.secret}.jpg`);
      imgElem.classList.add('my-img');
      responseSection.appendChild(imgElem);
    }

    for (let i=0; i < 5 ; i++){
      createImgElem(i);
    }
    for (let i=6; i < 11 ; i++){
      createImgElem(i);
    }
    for (let i=11; i < 16 ; i++){
      createImgElem(i);
    }

  }).catch(function (err) {
    console.error('bonk', err);
  });
}

goBtn.addEventListener('click',photoSearch);
