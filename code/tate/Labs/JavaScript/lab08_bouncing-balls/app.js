/*
Bouncing Balls
*/

let cnv = document.getElementById('canvas');
let ctx = cnv.getContext('2d');

let height = document.getElementById('canvas').height;
let width = document.getElementById('canvas').width;
let myRadius = 5;
let friction = 0.98;
let gravity = 0.05;



class Ball {
  constructor(radius=40,px=40,py=40,vx=1,vy=1){
    this.radius = radius;
    this.px = px;
    this.py = py;
    this.vx = vx;
    this.vy = vy;
  }
};

function randomColor() {
  let myColors = ['cyan ','white','black'];
  let myColor = myColors[Math.floor(Math.random()*myColors.length)];
  return myColor
}

// random positions
// Math.random()*(width - 2 * myRadius)+myRadius,
// Math.random()*(height - 2* myRadius)+myRadius,

function createBall() {
  let myColor = randomColor();
  let ball = new Ball(
    myRadius,
    (width/2),
    100,
    (2*Math.random()-1)*10,
    (2*Math.random()-1)*5
  );

  function main_loop() {
    // updatethe ball's position
    ctx.beginPath();
    ctx.fillStyle = '#333';

    // ctx.clearRect(ball.px - ball.radius - 1, ball.py - ball.radius - 1, ball.radius * 2 + 2, ball.radius * 2 + 2)
    ctx.globalAlpha = 0.9;
    ctx.fillRect(ball.px - ball.radius - 1, ball.py - ball.radius - 1, ball.radius * 2 + 2, ball.radius * 2 + 20);
    ctx.closePath();
    ctx.fillStyle = myColor;
    ctx.globalAlpha = 1;

    if (ball.py < (height - ball.radius)){
      ball.vy = ball.vy + gravity;
    }else if (ball.py == (height - ball.radius)) {
      ball.vy = 0;
      ball.py = height-ball.radius;

    }

    ball.px += ball.vx;
    ball.py += ball.vy;

    // check if hits boundary
    if (ball.py <= (0 + ball.radius) || ball.py >= (height-ball.radius) ){
      ball.vy = ball.vy*(-1);
      ball.vx = ball.vx * friction;
      ball.vy = ball.vy * friction;

    };
    if (ball.px <= (0 + ball.radius) || ball.px >= (width-ball.radius) ) {
      ball.vx *= -1;
      ball.vx = ball.vx * friction;
      ball.vy = ball.vy * friction;
    };
    // draw the Balls
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0 , 2 * Math.PI, false);
    ctx.fillStyle = myColor;
    ctx.fill();

    window.requestAnimationFrame(main_loop);
  }
  window.requestAnimationFrame(main_loop);
}
// random velocities
// (1*Math.random()-1)*1,
// (1*Math.random()-1)*1



for (let i = 0; i <1000;i++){
  createBall();
}
