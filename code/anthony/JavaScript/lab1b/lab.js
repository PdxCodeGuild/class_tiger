// lab09 as js part B

let input = document.querySelectorAll(".input");
let output = document.querySelectorAll(".output");
let bt = document.querySelector('.button');
let textInput = document.getElementById('input');
let answer = document.querySelector(".output-text");
let inUnit;
let outUnit;
let solution;
let value

bt.addEventListener('click', function () {
    for (let i of input) {
        if (i.checked == true) {
            inUnit = parseFloat(i.value);
        }
    }
    for (let j of output) {
        if (j.checked == true) {
            outUnit = parseFloat(j.value);
        }
    }
    value = textInput.value
    solution = ((parseFloat(value) / inUnit) * outUnit);
    answer.setAttribute('placeholder', `Answer: ${solution}`);

})