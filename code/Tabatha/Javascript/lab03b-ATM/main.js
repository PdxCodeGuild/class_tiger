

// Translate from Python
// ATM

class ATM {
    constructor(name){
        this.balance = 0;
        // name = document.getElementById("name").value;
        this.check = false;
        this.transaction_arr = [];
        console.log(this.balance);
    }
    check_balance() {
        alert(this.balance);
    }
    
    deposit(amount){
        this.balance = this.balance + amount;
        this.transaction_arr.push(`${name} deposited $${amount}`);
        console.log(this.balance);
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
            this.transaction_arr.push(`${name} withdrew $${amount}`);
            return this.balance
        }else alert("Not enough funds");
    }
    print_transaction(newBalance) {
        this.transaction_arr.forEach(function(each) {
            var br = document.createElement("br");
            receipt.appendChild(br);
            var t = document.createTextNode(each);
            receipt.appendChild(t);
        })
    }
}

let nameField = document.getElementById('name');
console.log("name")
let h2 = document.getElementsByTagName("h2")[0];
// let div = document.getElementsByTagName("div")[0];
nameField.addEventListener("change", function (){
    name = document.getElementById("name").value;
    h2.innerText = "Welcome, " + name;
    this.style.display = "none";
})
let account = new ATM(name);
let dep = document.getElementById("deposit");
let withd = document.getElementById("withdraw");
let history = document.getElementById("history");
let done = document.getElementById("done");
let p = document.getElementById("balance");
let printArea = document.getElementsByClassName("print")[0];
dep.addEventListener("click", function () {
    amount = parseFloat(document.getElementById("amount").value);
    newBalance = account.deposit(amount);
    p.innerText = "Balance " + newBalance;
});
withd.addEventListener("click", function () {
    amount = parseFloat(document.getElementById("amount").value);
    newBalance = account.withdrawal(amount);
    p.innerText = "Balance " + newBalance;
});
history.addEventListener("click", function () {
    receipt = document.createElement('p');
    receipt.id = 'receipt';
    receiptBalance = document.createElement('p');
    receiptBalance.id = 'r_balance';
    printArea.appendChild(receipt);
    printArea.removeChild(p);
    receipt.innerText = "Thank You, " + name;
    receipt.appendChild(receiptBalance);
    account.print_transaction(newBalance);
    receiptBalance.innerText = "Balance " + newBalance;
});
done.addEventListener("click", function () {
    h2.innerText = "Thank You";
    p.innerText = "";
});