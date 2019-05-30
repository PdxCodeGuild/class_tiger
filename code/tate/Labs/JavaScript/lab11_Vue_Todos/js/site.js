/*
To do app with Vue

*/

main = new Vue({
    el:'#vue-app',
    data: {
        title: 'Hello',
        name: '',
        todoItemList: [],
    },
    methods: {
        greet: function(time) {
          return 'Good ' + time + ' ' + this.name;
        },
        updateName: function(event) {
          console.log('you updated your name');
        },
        submitTodo: function() {
          let todoText =  this.$refs.todoText.value;
          let isComplete = false;
          this.name = this.$refs.todoName.value;
          this.todoItemList.push({ name: this.name, content: todoText , complete: isComplete });
        },
        completeTodo: function(index) {
          this.todoItemList[index].complete = true;
        },

        markIncompleteTodo: function(index) {
          this.todoItemList[index].complete = false;
        },
        deleteTodo: function(index) {
          this.todoItemList.splice(index,1);
        }
    },
    computed: {

    }
});
