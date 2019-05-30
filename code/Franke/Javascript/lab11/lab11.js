
const app = new Vue({
  el: '#app',
  data: {
    title: 'My To Do APP',
      // first store a single item types use this to store in list
    newtodo: '',
      // store all users input
    todos: []
  },
  methods: {
      // push an object into list/array
    addtodo() {
      this.todos.push({title: this.newtodo, done: false});
            // clearout the value of the newtodo because it's bound
      this.newtodo = '';
    },
    removetodo(todo) {
        // to remove we need the index of element
      const todoIndex = this.todos.indexOf(todo);
       // splice removes the index like pop first arg is index of elt to pop next is how many
      this.todos.splice(todoIndex, 1);
    },
    // alldone() {
    //   this.todos.forEach(todo => {
    //     todo.done = true;
    //   });
    // }
  }
});
