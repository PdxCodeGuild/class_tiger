var app = new Vue({
    el: '#app',
    data: {
        message: 'What do you need to do?',
        newtodo: '',
        todos: [
            {'text': 'Dishes', 'checkStyle': "checkOn", "done": true, "undo": false},
            {'text': 'Laundry', 'checkStyle': "checkOn", "done": true, "undo": false}
        ],
        done: [],
    },
    methods: {
        addTodo: function() {
            this.todos.push({'text': `${this.newtodo}`, 'checkStyle': "checkOn", "done": true, "undo": false})
            console.log(this.newtodo)
        },
        finishTodo: function(todo) {
            console.log(todo)
            index = this.todos.indexOf(todo);
            console.log(index)
            this.done.push(todo);
            // todo.checkStyle = "checkOff";
            todo.done = false;
            todo.undo = true;
            this.todos.splice(index, 1);
        },
        deleteTodo: function(todo) {
            index = this.todos.indexOf(todo);
            this.todos.splice(index, 1);
        },
        deleteDone: function(d) {
            index = this.done.indexOf(d);
            this.done.splice(index, 1);
        },
        undoDone(d){
            index = this.done.indexOf(d);
            console.log(index)
            this.todos.push(d);
            // d.checkStyle = "checkOn";
            d.done = true;
            d.undo = false;
            this.done.splice(index, 1);
        }
    },
});

// make on delete function by making one array and using a filter