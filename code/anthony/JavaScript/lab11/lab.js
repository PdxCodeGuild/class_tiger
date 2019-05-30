let app = new Vue({
    el: '#app',
    data: {
        title: 'Todo List',
        newtodo: '',
        todoList: [],
    },
    methods: {
        addTodo() {
            this.todoList.push({
                title: this.newtodo,
                completed: false,
            });
            this.newtodo = '';
        },
        removeTodo(todo) {
            let index = this.todoList.indexOf(todo);
            this.todoList.splice(index, 1);
        },
    }
})