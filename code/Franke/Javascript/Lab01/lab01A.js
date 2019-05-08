// User_Grade = input("Choose a grade between O and 100? >").strip()
// User_Grade = int(User_Grade)
//
// def letter_grade(User_Grade):
//     if User_Grade >= 90:
//         letter ='A'
//     elif User_Grade >= 80:
//         letter ='B'
//     elif User_Grade >= 70:
//         letter ='C'
//     elif User_Grade >= 60:
//         letter ='D'
//     else:
//         letter ='F'
//
//     if letter != 'F':
//         if User_Grade%10 >= 7:
//             letter += '+'
//         elif User_Grade%10 < 3:
//             letter += '-'
//
//     print(f'The letter grade is: {letter}')
//
//
// letter_grade(User_Grade)


let User_Grade = prompt('choose a grade between 0 and 100');
// let letter = '';

function letter_grade(User_Grade) {
    let letter = '';
    if (User_Grade >= 90) {
        letter = 'A';
    } else if (User_Grade >= 80) {
        letter = 'B';
    }
     else if (User_Grade >= 70) {
        letter ='C';
    }
      else if (User_Grade >= 60) {
        letter = 'D';
    }
       else  {
        letter = 'F';
    }

    if(letter !== 'F') {
        if ( User_Grade%10 >= 7 ) {
            letter += '+'
        }
        if ( User_Grade%10 < 3 ) {
            letter += '-'
        }
    }
    alert(`The letter grade is ${letter}`)

}

letter_grade(User_Grade);