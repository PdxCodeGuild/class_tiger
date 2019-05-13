let rotCipherNav = document.querySelector('#rotCipherNav');
let cardValidationNav = document.querySelector('#cardValidationNav');
let atmNav = document.querySelector('#atmNav');
//
// let rotCipher = document.querySelector('.rot-cipher');
// let atm = document.querySelector('.atm');




function rotCipherFunc() {
  document.querySelector('.rot-cipher').style.display = 'block';
  document.querySelector('.atm').style.display = 'none';
  document.querySelector('.card-validator').style.display = 'none';

  rotCipherNav.classList.add("section-active");
  atmNav.classList.remove("section-active");
  cardValidationNav.classList.remove("section-active");
}
function cardValidationFunc() {
  document.querySelector('.rot-cipher').style.display = 'none';
  document.querySelector('.atm').style.display = 'none';
  document.querySelector('.card-validator').style.display = 'block';

  rotCipherNav.classList.remove("section-active");
  atmNav.classList.remove("section-active");
  cardValidationNav.classList.add("section-active");
}
function atmFunc() {
  document.querySelector('.rot-cipher').style.display = 'none';
  document.querySelector('.atm').style.display = 'block';
  document.querySelector('.card-validator').style.display = 'none';

  rotCipherNav.classList.remove("section-active");
  atmNav.classList.add("section-active");
  cardValidationNav.classList.remove("section-active");
}
rotCipherNav.addEventListener('click', rotCipherFunc);
cardValidationNav.addEventListener('click', cardValidationFunc);
atmNav.addEventListener('click', atmFunc);
