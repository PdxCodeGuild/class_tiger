
function todolist() {
    var item = document.getElementById("input").value;
    var text = document.createTextNode(item);
    var new_element = document.createElement("li");

    let button_completed = document.createElement('button');
    button_completed.classList.add("btn-primary");
    button_completed.innerHTML = 'Done';
    button_completed.onclick = function() {
       document.getElementById("todo").removeChild(this.parentElement);
        let new_element = document.createElement('li');
        new_element.appendChild(text);
        document.getElementById("completed").appendChild(new_element);
    };

    let button_removed = document.createElement('button');
    button_removed.classList.add("btn-primary");
    button_removed.innerHTML = 'remove';
    button_removed.onclick = function() {
       document.getElementById("todo").removeChild(this.parentElement);

    };
    new_element.appendChild(text);
    new_element.appendChild(button_completed);
    new_element.appendChild(button_removed);
    document.getElementById("todo").appendChild(new_element)
    
}