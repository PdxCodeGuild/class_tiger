// Lab 25 : ATM

class ATM {
  constructor(balance=0) {
    this.balance = balance;
    this.transactions = [];
  }
  checkBalance () {
    return this.balance;
  }
  deposit (amount) {
    this.balance += amount;
    this.transactions.push('User deposited: ' + `${amount}`);
    return this.balance;
  }
  checkWithdraw (amount) {
    if (amount <= this.balance){
      return true;
    } else {
      return false;
    }
  }
  withdraw (amount) {
    if (this.checkWithdraw(amount)){
      this.balance -= amount;
      this.transactions.push('User withdrew: ' + `${amount}`);

    } else {
      alert('Insufficient funds');
    }
    return this.balance;
  }
  printTransactions (){
    return this.transactions.join('\n');
  }

}

let atm1 = new ATM(10);


function repl (account){
  while (true){
    let userChoice = prompt('What would you like to do? \nChoose: deposit, withdraw, check balance, history, quit').toLowerCase();

    if (userChoice === 'quit') {
      alert('Goodbye');
      break;
    } else if (userChoice === 'deposit'){
      let amount = parseInt(prompt('How much would you like to deposit?'));
      atm1.deposit(amount);
    } else if (userChoice === 'withdraw'){
      let amount = parseInt(prompt('How much would you like to withdraw?'));
      atm1.withdraw(amount);
    } else if (userChoice === 'check balance'){
      alert(atm1.checkBalance());
    } else if (userChoice === 'history'){
      alert(atm1.printTransactions());
    } else {
      alert('Invalid Input');
    }

  }
}

repl(atm1);
