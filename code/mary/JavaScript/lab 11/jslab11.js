
let app = new Vue({
    el:'#app',
    data: {
        message: "My To Do List:",
        todo:[],
        item: '',
    },
    methods:{    
        remove(){
                this.todo.pop(this.item)
            },
       
        add(){  
            this.todo.push(this.item)
            this.item=(item.text)
            
        }
    }

})