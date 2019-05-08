let operations = ['+', '-', '*', '/'];
let input = true;
while (input) {
    answer = prompt("What is the operation you would like to perform? or type 'done'. ");
    if (answer == 'done') {
        break;
    } if (operations){
        let num1 = prompt("What is the first number? ");
        let num2 = prompt("What is the second number? ");
        if (answer == '+') {
            var add = parseInt(num1) + parseInt(num2);
            alert("Answer: " + add);
        } else if (answer == '-') {
            var sub = parseInt(num1) - parseInt(num2);
            alert("Answer: " + sub);
        } else if (answer == '*') {
            var mult = parseInt(num1) * parseInt(num2);
            alert("Answer: " + mult);
        } else if (answer == '/') {
            var div = parseInt(num1) / parseInt(num2);
            alert("Answer: " + div);
        } 
    }
}
