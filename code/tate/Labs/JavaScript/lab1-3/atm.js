// Lab 25 : ATM
let atmBtnDeposit = document.querySelector('#atmBtnDeposit');
let atmBtnWithdraw = document.querySelector('#atmBtnWithdraw');
let atmBalance = document.querySelector('#atmBalance');
let atmTransactions = document.querySelector('#atmTransactions');

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
function atmInit(){
  atmBalance.innerText = `Account Balance : ${atm1.checkBalance()}`;
}

function atmTransactionsFunc () {
  atmTransactions.innerText = `${atm1.printTransactions()}`;
}

function atmFuncDeposit() {
  let depositAmount = parseInt(document.querySelector('#atmDeposit').value);
  atm1.deposit(depositAmount);
  atmBalance.innerText = `Account Balance : ${atm1.checkBalance()}`;
  atmTransactionsFunc();
}

function atmFuncWithdraw() {
  let withdrawAmount = parseInt(document.querySelector('#atmWithdraw').value);
  atm1.withdraw(withdrawAmount);
  atmBalance.innerText = `Account Balance : ${atm1.checkBalance()}`;
  atmTransactionsFunc();
}
var atm1 = new ATM(0);
atmInit();

atmBtnDeposit.addEventListener('click', atmFuncDeposit);
atmBtnWithdraw.addEventListener('click', atmFuncWithdraw);
