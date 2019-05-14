


class ATM {
    constructor(balance=0) {
        // DATA: every account needs CONTAINERS for the balance and transactions
      this.balance = balance;
      this.transactions =[]
    }
    // functionality: what an ATM can do/action/make computer do it with functions

    deposit(amount){
        this.balance += amount;
        var currentDate = new Date();
        this.transactions.push(`You deposited: ` + `${amount}`);
        }

    withdraw(amount){
            this.balance -= amount;
            var currentDate = new Date();
            this.transactions.push(`You withdrew: ` + `${amount}`);}

    get_balance() {
        return this.balance;
    }
    check_withdrawal(amount) {
        return this.balance <  amount ;
        }

    print_transactions(){
        return this.transactions.join('\n');
    }

    }


// if is for deposit button then  event listener
//     change listener for option of user
//     initialize new account with empty acct list or name input



let deposit = document.getElementById("deposit" );
let button_deposit = document.getElementById("add");
let withdraw = document.getElementById("withdraw" );
let button_withdraw= document.getElementById("subtract");
// let button_balance= document.getElementById("cash");
// let button_history= document.getElementById("transaction");

// let output_deposit = document.getElementById("message-deposit");
// let output_withdrawal = document.getElementById("message-withdraw");
let output_balance = document.getElementById("show-balance");
let output_history = document.getElementById("show-transactions");

button_deposit.onclick = function add(e) {
    e.preventDefault();
    let cash_added = parseInt(deposit.value); // save my value to something when button is clicked
    atm.deposit(cash_added);
    output_balance.innerText = `Your current balance is $ ${atm.get_balance()}`;
        history()};

button_withdraw.onclick = function subtract(e) {
        e.preventDefault();
            let cash_withdrawn = parseInt(withdraw.value); // save my value to something when button is clicked
             if (atm.check_withdrawal(cash_withdrawn) === false){
                atm.withdraw(cash_withdrawn);
                output_balance.innerText = `Your current balance is $ ${atm.get_balance()}`;}
             else {output_balance.innerText = `Not enough funds`;}
                history()};

// button_balance.onclick= function check(e) {
//             e.preventDefault();
//             output_balance.innerText = `Your current balance is $ ${atm.get_balance()}`
//         };

function history() {
            output_history.innerText = `${atm.print_transactions()}`;}
function init() {
    output_balance.innerText = `Your current balance is $ ${atm.get_balance()}`;
}
var atm = new ATM();
init();

