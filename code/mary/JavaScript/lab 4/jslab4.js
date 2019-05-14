let submit = document.getElementById("sub");
let input = document.getElementById("input");

submit.addEventListener("click", function(){
    let list = document.createElement("li");                
    let new_input = document.createTextNode(input.value);  
    let checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.name = "name";
    checkbox.value = "value";
    checkbox.id = "checkbox";   
    let remove = document.createElement('button')
    remove.type ="button";
    remove.name="remove";
    remove.value="remove";
    remove.id="delete";
    remove.style.margin="10px";
    remove.innerHTML= 'Delete';
    list.appendChild(checkbox);
    list.appendChild(new_input); 
    list.appendChild(remove);                           
    document.getElementById("list").appendChild(list);
    remove.addEventListener("click", function(){
        list.removeChild(new_input);
        list.removeChild(checkbox);
        list.removeChild(remove);
    });
    checkbox.addEventListener("change", function(){
        let done = document.createElement("li");
        list.removeChild(checkbox);
        list.removeChild(remove);
        done.appendChild(new_input);
        document.getElementById("done").appendChild(done);
    })
});



