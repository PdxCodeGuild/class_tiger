// Lab 20: Credit Card Validation
// Write a function that returns whther a string containing a
// credit card number is Valid

let checkDigit;
let doubledArray = [];
let subNine = [];
let mySum = 0;
cardString = '4556737586899855';

function cardValidator(cardString) {
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
    return true;
  } else {
    return false;
  }
}
if (cardValidator(cardString)){
  alert('Card Valid');
} else {
  alert('Card Invalid');
}
