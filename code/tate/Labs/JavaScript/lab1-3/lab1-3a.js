/* Lab 13 RotCipher : JavaScript version*/

const alphabet = ("abcdefghijklmnopqrstuvwxyz").split("");
let outputString = [];
// let userInput = prompt("What would you like to encrypt? > ").toLowerCase();
// let num = parseInt(prompt("With how much rotation would you like to encrypt? > "));

function rotEncrypt (userInput,num) {
  outputString = [];
  userInput = userInput.split('');

  userInput.forEach(function(item) {
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
// rotEncrypt(userInput,num);


while (true) {
  let userInput = prompt("What would you like to encrypt? \n (\'quit\' to exit)").toLowerCase();
  if (userInput === "quit") {
    alert("Goodbye");
    break;
  }
  let num = parseInt(prompt("With how much rotation would you like to encrypt? > "));
  alert(rotEncrypt(userInput,num));

}
