

// Dom Manilpulation
// Unit Converter


let h = document.getElementsByTagName("h2")[0];

function callback(e) {
    let distance = parseFloat(document.getElementById("distance").value);
    
    let start_unit = document.getElementById("startunit").value;
    
    if ((start_unit) == "ft") {
        var convert = distance * 3.3048;
    } else if ((start_unit) == "mi") {
        var convert = distance * 1609.34;
    } else if ((start_unit) == "km") {
        var convert = distance * 1000;
    } else if ((start_unit) == "m") {
        var convert = distance * 1;
    } else if ((start_unit) == "in") {
        var convert = distance * 0.0254;
    } else if ((start_unit) == "y") {
        var convert = distance * 0.9144;
    }
    
    let end_unit = document.getElementById("endunit").value;
    
    if ((end_unit) == "ft") {
        var distance2 = convert * 3.280839895;
    } else if ((end_unit) == "mi") {
        var distance2 = convert * 0.0006213689;
    } else if ((end_unit) == "km") {
        var distance2 = convert * 0.001;
    } else if ((end_unit) == "m") {
        var distance2 = convert * 1;
    } else if ((end_unit) == "in") {
        var distance2 = convert * 39.37007874;
    } else if ((end_unit) == "y") {
        var distance2 = convert * 1.0936132983;
    }
    h.innerText = distance2 + end_unit;
    
}
let button = document.getElementById("button")
button.addEventListener('click', callback);
  