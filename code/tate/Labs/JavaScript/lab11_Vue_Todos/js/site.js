/*
To do app with Vue
*/

main = new Vue({
    el:'#vue-app',
    data: {
        title: 'Hello',
        name: '',
        incompleteOutput: [],
        completeOutput: []
    },
    methods: {
        greet: function(time) {
            return 'Good ' + time + ' ' + this.name;
        },
        updateName: function(event) {
            console.log('you updated your name')
        },
        submitTodo: function() {
            let todoText =  this.$refs.todoText.value;
            this.name = this.$refs.todoName.value;
            this.incompleteOutput.push({ name: this.name,content: todoText });
            console.log(this.incompleteOutput);
        },
        completeTodo: function() {

        }
    },
    computed: {

    }
});


