// #Write a program that prompts the user for a string,
// #  and encodes it with ROT13. For each character, find the corresponding character,
// # add it to an output string. Notice that there are 26 letters in the English language,
// # so encryption is the same as decryption.

// for char in text:
//         index = alphabet.find(char)
//         output += alphabet_rotated[index]
//     return output

let input = document.getElementById("input" );
let button = document.getElementById("button");
// let output = document.getElementsByTagName("p" );
let output = document.getElementById("section-b");

function callback(e) {
    // e.preventDefault();
    let value = input.value;
    let lower = value.toLowerCase();
    var rot = 'nopqrstuvwxyzabcdefghijklm';
    var alphabet = 'abcdefghijklmnopqrstuvwyxz';
    var result = '';
    for (element of lower) {
       let index = alphabet.indexOf(element);
       result += rot[index];

    }
output.innerText = `The rot13 of  ${value} is ${result}`;
}
button.addEventListener('click', callback);


