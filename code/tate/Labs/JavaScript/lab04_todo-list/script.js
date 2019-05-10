
/*

Add an item to the List

Remove an item from the List

Mark an item as complete

*/

let todoSubmit = document.querySelector('#todoSubmit');
let todoContainer = document.querySelector('#todo-container');
let completeBtn = document.querySelector('.markDone');

function todoFunc(){

  let title = document.querySelector('#titleInput').value;
  let description = document.querySelector('#descriptionInput').value;
  let importance = document.querySelector('#importance');
  let titleOutput = document.createElement('h5');
  let pOutput = document.createElement('p');
  let todoItem = document.createElement('div');
  let markDoneBtn = document.createElement('button');
  let doneIcon = document.createElement('i')

  doneIcon.classList.add('fas');
  doneIcon.classList.add('fa-times');
  markDoneBtn.classList.add('markDone');
  todoItem.classList.add("todo-item");
  todoItem.classList.add("u-cf");

  markDoneBtn.innerText = "Complete";
  pOutput.innerText = `${description}`;
  titleOutput.innerText = `${title}`;

  markDoneBtn.appendChild(doneIcon);
  markDoneBtn.addEventListener('click', completeFunc);

  todoItem.appendChild(titleOutput);
  todoItem.appendChild(pOutput);
  todoItem.appendChild(markDoneBtn)

  todoContainer.appendChild(todoItem);
  // console.log(importance);
  console.log(todoItem);

}

function completeFunc () {
  let itemCompleted = this.parentElement;
  let doneContainer = document.querySelector('#done-container');

  itemCompleted.classList.add('done-list');

  doneContainer.appendChild(itemCompleted);
}

todoSubmit.addEventListener('click', todoFunc);
completeBtn.addEventListener('click', completeFunc);
