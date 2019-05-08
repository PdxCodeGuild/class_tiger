// lab09.py as js

let meterObj = {
    m: 1,
    ft: 3.28,
    in: 39.37,
    yd: 1.09,
    km: .001,
    mi: .006
};

let inNum;
let inUnit;
let outUnit;
let solution;

do {
    inNum = prompt("How many? (Enter a number)");
} while (isNaN(inNum));

do {
    inUnit = prompt("From what unit? (m, ft, in, yd, km, mi)");
} while (!(inUnit in meterObj));

do {
    outUnit = prompt("To what unit? (m, ft, in, yd, km, mi)");
} while (!(outUnit in meterObj));

solution = ((inNum / meterObj[inUnit]) * meterObj[outUnit]);

alert(`${inNum}${inUnit} converted to ${outUnit} is ${solution}${outUnit}`);