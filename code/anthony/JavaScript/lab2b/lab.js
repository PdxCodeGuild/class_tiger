//lab11 as js part B
let num1 = document.querySelector('.num1')
let num2 = document.querySelector('.num2')
let btn = document.querySelectorAll('.btn')
let solution = document.querySelector('.answer')
let calc = document.querySelector('.calc')

calc.addEventListener('click', function () {
    let value1 = parseFloat(num1.value);
    let value2 = parseFloat(num2.value);
    let answer
    for (let i of btn) {
        if (i.checked == true) {
            if (i.value == '+') {
                answer = value1 + value2;
            } else if (i.value == '-') {
                answer = value1 - value2;
            } else if (i.value == '*') {
                answer = value1 * value2;
            } else if (i.value == '/') {
                answer = value1 / value2;
            }
        }
    }
    solution.innerText = `Answer: ${answer}`;
})