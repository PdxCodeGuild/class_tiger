// lab11.py as js

let operatorChoices = ['+', '-', '*', '/', 'done'];
let num1 = 0;
let num2 = 0;
let solution = 0;
let operator;
let flag = true;
while (flag) {
    do {
        operator = prompt("What would you like to do? ('+', '-', '*', '/', 'done')");
        if (operator == 'done') {
            flag = false;
        }
    } while (!(operatorChoices.includes(operator)));
    if (flag == false) {
        break;
    }
    do {
        num1 = prompt("What is the first number?");
    } while (isNaN(num1));
    do {
        num2 = prompt("What is the second number?");
    } while (isNaN(num2));
    if (operator == '+') {
        solution = parseInt(num1) + parseInt(num2);
    } else if (operator == '-') {
        soltuion = parseInt(num1) - parseInt(num2);
    } else if (operator == '*') {
        solution = parseInt(num1) * parseInt(num2);
    } else {
        solution = parseInt(num1) / parseInt(num2);
    }
    alert(`${num1} ${operator} ${num2} = ${solution}`);
}