

// Translate from Python
// ATM

class ATM {
    constructor(name){
        this.balance = 0;
        this.name = name;
        this.check = false;
        this.transaction_arr = [];
    }
    check_balance() {
        alert(this.balance);
    }

    deposit(amount){
        this.balance = this.balance = amount;
        this.transaction_arr.push(`${this.name} deposited $${amount}`);
        return this.balance
    }
    check_withdrawal(amount) {
        if (this.balance - amount >= 0) {
            this.check = true;
            return this.check
        }
    }
    withdrawal(amount) {
        if (this.check_withdrawal(amount) === true) {
            this.balance -= amount;
            this.transaction_arr.push(`${this.name} withdrew $${amount}`);
            return this.balance
        }
    }
    print_transaction() {
        this.transaction_arr.forEach(function(each) {
            alert(each);
        })
    }
    REPL() {
        while (true) {
            let x = prompt(`What would you like to do? \ndeposit, withdraw, check balance, history, or done ? `);
            if (x === "deposit") {
                let amount = parseFloat(prompt(`how much would you like to deposit?`));
                this.deposit(amount);
            } else if (x === "withdraw") {
                let amount = parseFloat(prompt("how much would you like to withdraw? "))
                    this.withdrawal(amount);
            } else if (x === "check balance") {
                this.check_balance();
            } else if (x === "history") {
                this.print_transaction();
            } else if (x === "done"){
                break
            } else {
                alert(`Please try again`)
            }
        }
    }
}
let account_name = prompt("enter your account name: ");
let a1 = new ATM(account_name);
a1.REPL();