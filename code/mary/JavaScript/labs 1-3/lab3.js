const word_list = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

const word_list2= {0: "", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}

const word_list3={100: "One Hundred", 200: "Two Hundred", 300: "Three Hundred", 400: "Four Hundred", 500: "Five Hundred", 600: "Six Hundred", 700: "Seven Hundred", 800: "Eight Hundred", 900: "Nine Hundred"}

let submit = document.getElementById("sub");

submit.addEventListener("click", function(){
    let num = document.getElementById("num");
    let x = num.value;
    if (x >=0 && x<=19){
        document.getElementById("end").innerHTML = word_list[x];
    }
    else if (x>=20 && x<= 99){
        document.getElementById("end").innerHTML= word_list2[(Math.floor(x/10)*10)] +" "+ word_list[x%10];
    }
    else if (x>=100 && x<=999){
        p=Math.floor(x%100)
        t=Math.floor(Math.floor(p/10)*10)
        document.getElementById("end").innerHTML= word_list3[(Math.floor(x/100)*100)] + " " + word_list2[t] +" "+ word_list[x%10];
        }
    
 
});
