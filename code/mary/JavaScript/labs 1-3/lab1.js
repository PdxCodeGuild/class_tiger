let nums = [];
let input = true;
while(input) {
    user = prompt("Enter a number, or 'done'.");
    if (user == 'done'){
        break;
    } if (user == parseInt(user)) {
        nums.push(user);
        const sum = nums.reduce((total, amount) => parseInt(total) + parseInt(amount));
        x = sum / nums.length;
        alert(x);
    }
}






