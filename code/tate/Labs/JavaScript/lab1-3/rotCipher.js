/* Lab 13 RotCipher : JavaScript*/

let numInput = document.querySelector("#numInput");
let textInput = document.querySelector('#textInput');
let rotBtn = document.querySelector("#rotBtn");
let rotOutput = document.querySelector("#rotOutput");

const alphabet = ("abcdefghijklmnopqrstuvwxyz").split("");
let outputString = [];

function rotEncrypt (userInput,num) {
  outputString = [];
  const alphabet = ("abcdefghijklmnopqrstuvwxyz").split("");
  userInput = userInput.toLowerCase();
  userInput = userInput.split('');
  num = parseInt(num);
  userInput.forEach(function(item) {

    if ( item === ' ') {
      outputString.push(' ');
      return ' ';
    };
    let getIndex = alphabet.indexOf(item)
    getIndex = getIndex + num;

    if ((getIndex + num) > 25) {
     getIndex = getIndex % 26;
    }
    outputString.push(alphabet[getIndex]);
  })

  outputString = outputString.join('');
  return outputString;
}

function callback() {
   let output= rotEncrypt(textInput.value,numInput.value);
   rotOutput.innerText = `${output}`;
}

rotBtn.addEventListener('click', callback);
