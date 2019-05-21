let app = new Vue({
  el: '#app',
  data: {
    message: 'Hello World',
    hover: 'Hello again!',
    things: true,
    stuff: false,
    todos: [
      { text: 'Do things'},
      { text: 'Do stuff'},
      { text: 'Do whatever'}
    ]
  },
  methods: {
    reverseMessage: function() {
      this.message = this.message.split('').reverse().join('');
    }
  }
});