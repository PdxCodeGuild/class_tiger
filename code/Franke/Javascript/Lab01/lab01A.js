//
// let User_Grade = prompt('choose a grade between 0 and 100');
// // let letter = '';
//
// function letter_grade(User_Grade) {
//     let letter = '';
//     if (User_Grade >= 90) {
//         letter = 'A';
//     } else if (User_Grade >= 80) {
//         letter = 'B';
//     }
//      else if (User_Grade >= 70) {
//         letter ='C';
//     }
//       else if (User_Grade >= 60) {
//         letter = 'D';
//     }
//        else  {
//         letter = 'F';
//     }
//
//     if(letter !== 'F') {
//         if ( User_Grade%10 >= 7 ) {
//             letter += '+'
//         }
//         if ( User_Grade%10 < 3 ) {
//             letter += '-'
//         }
//     }
//     alert(`The letter grade is ${letter}`)
//
// }

// letter_grade(User_Grade);


let input = document.getElementById("number_grade" );
let button = document.getElementById("button");
// let output = document.getElementsByTagName("p" );
let output = document.getElementById("section-b");

function callback(e) {
    e.preventDefault();
    let letter = '';
    let value = input.value; // save my value to something when button is clicked
    if (value >= 90) {
        letter = 'A';
    } else if (value >= 80) {
        letter = 'B';
    }
     else if (value >= 70) {
        letter ='C';
    }
      else if (value >= 60) {
        letter = 'D';
    }
       else if (value < 60){
        letter = 'F';
    }

    if(letter !== 'F') {
        if ( value%10 >= 7 ) {
            letter += '+'
        }
        if ( value%10 < 3 ) {
            letter += '-'
        }
    }
    output.innerText = `The letter grade is ${letter}`;


}

button.addEventListener('click', callback);