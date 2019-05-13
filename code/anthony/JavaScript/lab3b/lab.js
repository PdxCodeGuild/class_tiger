//lab25.py as js part B
let balance = document.querySelector('.balance');
let input = document.querySelector('.input');
let deposit = document.querySelector('.deposit');
let withdraw = document.querySelector('.withdraw');
let value = 0;
let transaction = [];
deposit.addEventListener('click', function () {
    value += parseFloat(input.value);
    balance.innerText = `Balance: ${value}`;

})
withdraw.addEventListener('click', function () {
    if (value - parseFloat(input.value) >= 0) {
        value -= parseFloat(input.value);
    } else {
        alert('You cannot withdraw that amount!');
    }
    balance.innerText = `Balance: ${value}`;
})