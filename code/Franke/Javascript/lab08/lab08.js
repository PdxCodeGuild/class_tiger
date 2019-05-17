var canvas = document.querySelector("canvas");
// var width = canvas.width;
// var height = canvas.height;
// to set the canvas size to be the full page add css body margin 0
canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

///passing 2d to be able to draw etc
let ctx = canvas.getContext('2d');
// 1 color of the rect comes before the rect
// ctx.fillStyle = 'green';
// create a rectangle
// ctx.fillRect(10, 10, 100, 100);

//2 lines
// ctx.beginPath();
//where line start in x coordinate and y
// ctx.moveTo(50,300);
//where line stops in x coordinate and y
// ctx.lineTo(300, 100);
///to color the line add strokestyle for lines
// ctx.strokeStyle = "#fa34a3";
//we need stroke method for it to show on the screen
// ctx.stroke();

///3 lets make an arc or circle
// ctx.beginPath();
// //Radius is how wide we want the circle. start angle where to start drawing end angle how long to draw
// //pi*2 is a full circle
// ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
// ctx.fillStyle = 'green';
// //we need fill method for it to show on the screen
// ctx.stroke();

/// 4 to get multiple circles put above code for circle in a for loop
///before we gotta make sure we have different position on canvas for each
// circle otherwise it's circle on top of each other
// for (var i =0; i< 10; i++){
// // to make sure we have different s y position use math.random
// // (random only picks from 0 to 1) for it to make sense multiply by length of canvas
// // if canvas is full webpage length multiply by innerWidth & innerHeight
//     var x =Math.random()* width;
//     var y =Math.random()* height;
//     radius = 30;
// ctx.beginPath();
// ctx.arc(x, y, radius, 0, 2 * Math.PI, false);
// ctx.strokeStyle = getRandomColor();
// ctx.stroke();
// }

///5  get random colors
// function getRandomColor() {
//   var letters = '0123456789ABCDEF';
//   var color = '#';
//   for (var i = 0; i < 6; i++) {
//     color += letters[Math.floor(Math.random() * 16)];
//   }
//   return color;
// }



/// 6 making our circles move around with a function that calls itself
// this will refresh non stop and create animation
// each time the function refreshes change location
// velocity is how fast things move. or increment on the x y position

// var x =Math.random()* innerWidth;
// var y =Math.random()* innerHeight;
// // randomize velocity since random goes from 0 to 1 subtracting .5
// // ensures we get
// var dx = (Math.random() - 0.5)*8;
// var dy = (Math.random() - 0.5)*8;
// var radius = 30;
// function animate() {
//     requestAnimationFrame(animate);
// // we get connected circles unless we clear the canvas each refresh
//     ctx.clearRect(0,0,innerWidth,innerHeight);
//     ctx.beginPath();
//     ctx.arc(x, y, radius, 0, 2 * Math.PI, false);
//     ctx.strokeStyle = 'blue';
//     ctx.stroke();
//     // add  to x so it moves each refresh ad positive and negative
//     // so it goes left and right
//     // we want it to be when the circle radius goes beyong not center
//    if (x + radius > innerWidth || x - radius < 0){
//        // dx will change direction when full width is reached
//        dx = -dx;
//    }
//    //same with y go opposite until e
//     if (y + radius > innerHeight || y - radius < 0){
//         // dx will change direction when full width is reached
//        dy = -dy;
//    }
//     x += dx;
//     y += dy;
// }
// animate();

// 7-e add interactivity 1 word eventlisteners
// we need to get thedistance between our mouse position and circle
var mouse = {x:undefined, y : undefined}; //var with multiple points
var maxRadius = 40;
var colorArray= ['#323E40','#F2AB27','#D97D0D','#732002',
'#D94D1A',];
window.addEventListener('mousemove',function(event){
    // console.log(event); this will give log of each mouse move
    ///let's get the mouse position
    mouse.x = event.x;
    mouse.y = event.y;
});
/// for whenevr the browser is resized
window.addEventListener('resize',function(){
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
});

// 7) make multiple circles with each its position, velocity, radius and animate
//this requires a class Capital C in JS
function Circle(x,y,dx,dy,radius) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;
    this.minRadius = radius;
    this.color = colorArray[Math.floor(Math.random()* colorArray.length)];
    this.draw = function () {
    ctx.beginPath();
    ctx.arc(this.x,this.y, this.radius , 0, 2 * Math.PI, false);
    // ctx.strokeStyle = 'blue';
    ctx.fillStyle = this.color;
    ctx.stroke();
    ctx.fill();
    };
    this.update = function () {
         if (this.x + this.radius > innerWidth || this.x  - this.radius< 0){
       this.dx = -this.dx;
   }
         if (this.y + this.radius > innerHeight || this.y - this.radius < 0){
       this.dy = -this.dy;
   }
    this.x  += this.dx;
    this.y += this.dy;
    ///interactivity increase size if distance between mouse
        // position and circle is say 50px
    if (mouse.x - this.x < 50 && mouse.x - this.x > -50
        && mouse.y - this.y < 50 && mouse.y - this.y > -50) {
        // add one to radius if its size less than 40
        if(this.radius<maxRadius){
            this.radius += 1;
        } //otherwise decrease size until it's original size
    }else if (this.radius > this.minRadius){
        this.radius -= 1;
    }
    // we call this draw function to draw after changing coordinates
    this.draw();
    }
}

var circleArray = []; // create array to store all the circles

function init() {
    circleArray = [];
    for (var i = 0; i< 800; i++){

    var radius = Math.random()*10 +1;
    var x =Math.random()* (innerWidth - radius *2) + radius; //- radius*2 makes them not exceed
    var y =Math.random()* (innerHeight - radius*2) + radius;
    var dx = (Math.random() - 0.5);
    var dy = (Math.random() - 0.5);

    circleArray.push(new Circle(x,y,dx,dy,radius))
}
}

// 7- b get randomization
// var x =Math.random()* innerWidth;
// var y =Math.random()* innerHeight;
// // randomize velocity since random goes from 0 to 1 subtracting .5
// // ensures we get
// var dx = (Math.random() - 0.5)*8;
// var dy = (Math.random() - 0.5)*8;
// var radius = 30;

// 7-c multiply instances say 100 times
// var circleArray = []; // create array to store all the circles
// for (var i = 0; i< 800; i++){
//     ///use randomize value to create unique parameters
//     var radius = Math.random()*3 +1;
//     var x =Math.random()* (innerWidth - radius *2) + radius; //- radius*2 makes them not exceed
//     var y =Math.random()* (innerHeight - radius*2) + radius;
//     var dx = (Math.random() - 0.5);
//     var dy = (Math.random() - 0.5);
//     // var radius = 30; // static radius for now
// // this loop goes a 100 times creates new instance and stores in array
//     circleArray.push(new Circle(x,y,dx,dy,radius))
// }

// 7-d) now animate each circle since they have each their own param
//so use the class in function
function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, innerWidth, innerHeight);
    // this loop whithin funct will run function update for eache
    for (var i = 0;i< circleArray.length; i++ ) {
        circleArray[i].update();
    }
}
init();
animate();


