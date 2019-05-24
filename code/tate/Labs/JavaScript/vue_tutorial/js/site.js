
Vue.component('greeting', {
    template:'<p> Hey there, i am a reusable {{name}} <button v-on:click="changeName">change name</button></p>',
    data: function () {
        return {
            name: "Yoshi"
        }
    },
    methods: {
        changeName: function() {
            this.name = 'Mario'
        }
    }
})

var main = new Vue({
    el:'#vue-app',
    data: {
        title: 'Hello',
        name: 'whomever',
        age: 25,
        website: 'http://www.tateshep.com',
        websiteTag: '<a href="http://www.tateshep.com">View my website</a>',
        x: 0,
        y: 0,
        a: 0,
        b: 0,
        available:false,
        nearby: false,
        error: false,
        success: false,
        characters: ['Mario','Luigi','Yoshi','Bowser'],
        ninjas: [
            { name: 'Ryu',age:25 },
            { name: 'Yoshi',age:35 },
            { name: 'Ken',age:55 },

        ]

    },
    methods: {
        greet: function(time) {
            return 'Good ' + time + ' ' + this.name;
        },
        add: function(inc) {
            this.age+= inc;
        },
        subtract: function(dec) {
            this.age-= dec;
        },
        updateXY: function(event) {
            this.x = event.offsetX;
            this.y = event.offsetY;
        },
        logAge: function(event){
            console.log('you entered your age');
        },
        logName: function(event){
            console.log('you entered your name');
        }
       
    },
    computed: {
        addToA: function() {
            return this.a + this.age;
        },
        addToB: function() {
            return this.b + this.age;
        },
        compClasses: function() {
            return{
                available: this.available,
                nearby: this.nearby
            }
        }
    }
});

var section2 = new Vue ({
    el:'#section2',
    data: {
        title: 'Section 2'
    },
    methods: {
        test: function () {
            console.log('test');
        }
    },
    computed: {
        greet: function() {
            return 'hello from section2';
        }
    }
});

var section3 = new Vue ({
    el:'#section3',
    data: {
        title: 'Section 3'
    },
    methods: {
        changeTitle: function() {
            section2.title = "Title changed";
        }
    },
    computed: {
        greet: function() {
            return 'hello from section3';
        }
    }
});


var section4 = new Vue ({
    el:'#section4',
    data: {
        title: "section 4",
        output: "Your fav food"

    },
    methods: {
        test: function() {
            console.log('section4')
        },
        readRefs: function() {
            console.log(this.$refs.input.value);
            this.output = this.$refs.input.value;
            console.log(this.$refs.test.innerText);
        }
    },
    computed: {

    }
})