let canvas=document.getElementById("canvas");
let ctx=canvas.getContext("2d")
let height=500;
let width=800;
let friction = 0.99;
let gravity = 0.75;


let ball = {
    radius: 30,
    px: Math.random()*800,
    py: Math.random()*500,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,
    draw(){
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'blue';
    ctx.fill();
}
}

ball.draw();

function main_loop() {
    ctx.clearRect(0, 0, 800,600);
    ball.px +=ball.vx;
    ball.py+=ball.vy;
    if (ball.px >width -ball.radius){
        ball.vx*=-1 * friction;
    }
    if (ball.py >height -ball.radius){
        ball.vy*=-1 * friction;
    }
    if (ball.px<=0+ball.radius){
        ball.vx*=-1 * friction;
    }
    if (ball.py<=0+ball.radius){
        ball.vy*=-1 * friction;
    }  
    ball.draw();
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);