//lab25.py as js part B
let balance = document.querySelector('.balance');
let input = document.querySelector('.input');
let show = document.querySelector('.transaction');
let deposit = document.querySelector('.deposit');
let withdraw = document.querySelector('.withdraw');
let transactions = document.querySelector('.transactions')
let value = 0;
deposit.addEventListener('click', function () {
    value += parseFloat(input.value);
    balance.innerText = `Balance: ${value}`;
    let output = document.createElement('p');
    output.innerText = `Deposit of ${input.value}`;
    transactions.appendChild(output)

})
withdraw.addEventListener('click', function () {
    if (value - parseFloat(input.value) >= 0) {
        value -= parseFloat(input.value);
        let output = document.createElement('p');
        output.innerText = `Withdrawal of ${input.value}`;
        transactions.appendChild(output)
    } else {
        alert('You cannot withdraw that amount!');
    }
    balance.innerText = `Balance: ${value}`;
})
show.addEventListener('click', function () {
    if (transactions.style.display == 'none') {
        transactions.style.display = 'block';
    } else {
        transactions.style.display = 'none';
    }
})