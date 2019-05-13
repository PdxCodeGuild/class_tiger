let submit = document.getElementById("sub");
let plus= document.getElementById("add");
let minus = document.getElementById("minus");
let mult = document.getElementById("mult");
let divide = document.getElementById("div");
let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");

plus.addEventListener("change", function(){
    submit.addEventListener("click", function(){
        const sum = parseInt(num1.value) + parseInt(num2.value);
        document.getElementById("answer").innerHTML =  "Answer: " + sum;
    })
})

minus.addEventListener("change", function(){
    submit.addEventListener("click", function(){
        const less = parseInt(num1.value) - parseInt(num2.value);
        document.getElementById("answer").innerHTML =  "Answer: " + less;
    })
})

mult.addEventListener("change", function(){
    submit.addEventListener("click", function(){
        const mult = parseInt(num1.value) * parseInt(num2.value);
        document.getElementById("answer").innerHTML =  "Answer: " + mult;
    })
})

divide.addEventListener("change", function(){
    submit.addEventListener("click", function(){
        const x = parseInt(num1.value) / parseInt(num2.value)
        document.getElementById("answer").innerHTML =  "Answer: " + x;
    })
})