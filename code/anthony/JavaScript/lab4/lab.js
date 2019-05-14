let input = document.getElementById("in-text");
let addBtn = document.getElementById("add-btn");
let inItem = document.getElementById("in-item");
let compItem = document.getElementById("comp-item")

input.autofocus = true;

let newItem = function (innertext) {
    let listItem = document.createElement("li");
    let completeItem = document.createElement("button");
    let label = document.createElement("label");
    let deleteItem = document.createElement("button");
    let br = document.createElement("br");

    label.innerText = innertext;

    completeItem.innerText = "Complete";
    completeItem.className = "complete-btn"
    deleteItem.innerText = "Discard";
    deleteItem.className = "delete-btn";

    listItem.appendChild(label);
    listItem.appendChild(br);
    listItem.appendChild(completeItem);
    listItem.appendChild(deleteItem);


    return listItem;
}

let addItem = function () {
    let listItem = newItem(input.value);
    inItem.appendChild(listItem);
    input.value = "";
    addClick(listItem);
}

let removeItem = function () {
    let listItem = this.parentNode;
    let ul = listItem.parentNode;
    ul.removeChild(listItem);
}

let completedItem = function () {
    let listItem = this.parentNode;
    compItem.appendChild(listItem);
    this.innerText = "Not Complete"
    this.parentNode.style.textDecoration = "line-through";
    addClick(listItem);
}

let unCompletedItem = function () {
    let listItem = this.parentNode;
    inItem.appendChild(listItem);
    this.innerText = "Complete"
    addClick(listItem);
}

addBtn.addEventListener('click', addItem);

input.addEventListener('keyup', function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        addBtn.click();
    }
})

let addClick = function (taskItem) {
    let completeButton = taskItem.querySelector("button.complete-btn");
    if (completeButton.innerText == "Complete") {
        completeButton.onclick = completedItem;
    } else if (completeButton.innerText == "Not Complete") {
        completeButton.onclick = unCompletedItem;
    }
    let deleteButton = taskItem.querySelector("button.delete-btn")
    deleteButton.onclick = removeItem;
}
for (let i = 0; i < inItem.children.length; i++) {
    addClick(inItem.children[i]);
}
for (let i = 0; i < compItem.children.length; i++) {
    addClick(compItem.children[i]);
}


// for (var i=0; i<incompleteTaskHolder.children.length;i++){

//     //bind events to list items chldren(tasksCompleted)
//     bindTaskEvents(incompleteTaskHolder.children[i],taskCompleted);
// }
// //cycle over completedTasksHolder ul list items
// for (var i=0; i<completedTasksHolder.children.length;i++){
// //bind events to list items chldren(tasksIncompleted)
//     bindTaskEvents(completedTasksHolder.children[i],taskIncomplete);
// }