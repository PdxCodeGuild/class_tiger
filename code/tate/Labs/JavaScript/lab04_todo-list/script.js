
/*

Add an item to the List
Remove an item from the List
Mark an item as complete
Sorts items by due date

*/

let todoSubmit = document.querySelector('#todoSubmit');
let todoContainer = document.querySelector('#todo-container');
let completeBtn = document.querySelector('.markDone');
let removeItemBtn = document.querySelector('.removeItemBtn');

function todoFunc(){

  let title = document.querySelector('#titleInput').value;
  let description = document.querySelector('#descriptionInput').value;
  let dateInput = document.querySelector('#dateInput').value;
  let titleOutput = document.createElement('h5');
  let pOutput = document.createElement('p');
  let dateOutput = document.createElement('p');
  let todoItem = document.createElement('div');
  let markDoneBtn = document.createElement('button');
  let removeItemBtn = document.createElement('button');
  let doneIcon = document.createElement('i')

  doneIcon.classList.add('fas');
  doneIcon.classList.add('fa-times');
  markDoneBtn.classList.add('markDone');
  markDoneBtn.classList.add('todoBtns');
  removeItemBtn.classList.add('todoBtns');
  removeItemBtn.classList.add('removeItemBtn');

  todoItem.classList.add("todo-item");
  todoItem.classList.add("u-cf");

  markDoneBtn.innerText = "Complete";
  removeItemBtn.innerText = "Remove";
  pOutput.innerText = `${description}`;
  dateOutput.innerText = `Due Date: ${dateInput}`;
  titleOutput.innerText = `${title}`;

  removeItemBtn.appendChild(doneIcon);
  markDoneBtn.addEventListener('click', completeFunc);
  removeItemBtn.addEventListener('click', removeFunc);

  todoItem.appendChild(titleOutput);
  todoItem.appendChild(pOutput);
  todoItem.appendChild(dateOutput);
  todoItem.appendChild(removeItemBtn);

  todoItem.appendChild(markDoneBtn);
  todoItem.id = `${dateInput}`;

  todoContainer.appendChild(todoItem);
  sortFunc();
}

function sortFunc() {
  let items = document.getElementsByClassName('todo-item');
  let arr = Array.prototype.slice.call( items );
  itemsSorted = arr.sort(function(a,b) {
    return a.id.localeCompare(b.id);
  });
  todoContainer.innerHTML = '';
  itemsSorted.forEach(function(item){
    todoContainer.appendChild(item);
  });
}

function removeFunc() {
  let itemRemove = this.parentElement;
  itemRemove.parentElement.removeChild(itemRemove);
}

function completeFunc () {
  let itemCompleted = this.parentElement;
  let doneContainer = document.querySelector('#done-container');
  itemCompleted.classList.add('done-list');
  itemCompleted.classList.remove('todo-item');
  doneContainer.appendChild(itemCompleted);
  itemCompleted.removeChild(this);
}

todoSubmit.addEventListener('click', todoFunc);
