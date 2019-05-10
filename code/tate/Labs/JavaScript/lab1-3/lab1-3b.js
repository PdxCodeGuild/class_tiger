// Lab 20: Credit Card Validation
// Write a function that returns whther a string containing a
// credit card number is Valid


// cardString = '4556737586899855';
let cardValid = document.querySelector('#cardValid');


function cardValidator() {
  let checkDigit;
  let doubledArray = [];
  let subNine = [];
  let mySum = 0;
  let  cardString = document.querySelector('#cardInput').value;
  console.log(cardString);
  let cardArray = cardString.split('');
  let intArray = [];
  cardArray.forEach(function(item) {
    intArray.push(parseInt(item));
  });
  checkDigit = intArray[intArray.length-1];
  intArray.pop()
  intArray.reverse();
  for (i = 0; i < intArray.length; i++ ){
    // Doubles every other item in intArray
    let myNum = intArray[i];
    if (i % 2 == 0){
      myNum = myNum * 2 ;
    }
    doubledArray.push(myNum);
  }
  for (i = 0; i < doubledArray.length; i++){
    let myNum = doubledArray[i];
    if (myNum > 9){
      myNum = myNum - 9;
    }
    subNine.push(myNum);
  }
  for (i = 0; i < subNine.length; i++){
    mySum += subNine[i];
  }
  let checkNum = mySum.toString();
  checkNum = checkNum.split('')
  if (checkNum[1] == checkDigit.toString()){
    console.log('true');
    cardValid.innerText = 'Card Valid!';

    return true;
  } else {
    console.log('false');
    cardValid.innerText = 'Card Invalid!';

    return false;
  }
}

let validateBtn = document.querySelector('#validateBtn');

function callback() {
  // console.log(cardValidator(cardString.value));
  cardValidator()
}

validateBtn.addEventListener('click', cardValidator);
