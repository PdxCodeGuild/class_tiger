

var taskList = document.getElementById("list");
var doneList = document.getElementById("complete");

var trash = document.getElementsByClassName("trash");

function addTask(){
    var task = document.createElement("li");
    var newTask = document.getElementById("newtask").value;
    var t = document.createTextNode(newTask);
    var complete = document.createElement("button");
    complete.className = "check";
    complete.innerHTML ="<i class='fas fa-clipboard-check'></i>";
    complete.addEventListener("click", function(){
        console.log("clicked")
        doneList.appendChild(this.parentElement);
        this.remove();
    })
    task.appendChild(complete);
    document.getElementById("newtask").value = "";
    var trashBtn = document.createElement("button");
    var icon = document.createElement("i");
    trashBtn.className = "trashBtn";
    trashBtn.innerHTML = "<i class='fas fa-trash-alt'></i>";
    trashBtn.addEventListener("click", function(){
        this.parentElement.remove();
    })
    task.appendChild(trashBtn);
    taskList.appendChild(task);
    task.appendChild(t);
}
