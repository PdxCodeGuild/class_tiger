
let submit = document.getElementById("sub");
let done = document.getElementById("done");
let input = document.getElementById("input");
let reset=document.getElementById("reset")
let nums = [];
submit.addEventListener("click", function (){
    console.log(input.value);
    nums.push(input.value);
    console.log(nums);
    const sum = nums.reduce((total, amount) => parseInt(total) + parseInt(amount));
    document.getElementById("total").innerHTML =  "Sum: " + sum;
    done.addEventListener("click", function(){
        x = sum / nums.length;
        document.getElementById("average").innerHTML = "Average: " + x;  
    
    });
});
