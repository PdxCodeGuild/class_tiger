// lab25.py as js

class ATM {
    constructor(balance = 0) {
        this.balance = balance;
        this.transactions = [];
    }
    getBalance() {
        return this.balance;
    }
    setBalance(balance) {
        this.balance = balance;
        this.transactions.push(`Deposit of ${balance}`);
        this.transactions.push('\n');
    }
    withdraw(amount) {
        this.setBalance(this.balance - amount);
        this.transactions.push(`Withdraw of ${amount}`);
        this.transactions.push('\n');
    }
    checkWithdrawal(amount) {
        if (this.balance - amount < 0) {
            alert("You cannot withdraw that much");
            alert(`Your balance is ${this.balance}`)
        } else {
            this.withdraw(amount);
            alert(`Your new balance is ${this.balance}`)
        }
    }
}
let menuOptions = ['deposit', 'withdraw', 'balance', 'transactions', 'quit'];
let atm = new ATM()
while (true) {
    let userInput;
    let input;
    do {
        userInput = prompt("What would you like to do? (deposit, withdraw, balance, 'transactions', quit")
    } while (!(menuOptions.includes(userInput)));
    if (userInput == 'deposit') {
        input = parseFloat(prompt("How much would you like to deposit?"));
        atm.setBalance(atm.getBalance() + input);
        alert(`Your new balance is: ${atm.getBalance()}`)
    } else if (userInput == 'withdraw') {
        input = parseFloat(prompt("How much would you like to withdraw?"));
        atm.checkWithdrawal(input);
    } else if (userInput == 'balance') {
        alert(`Your balance is ${atm.getBalance()}`);
    } else if (userInput == 'transactions') {
        alert(`${atm.transactions}`);
    } else {
        break;
    }
}