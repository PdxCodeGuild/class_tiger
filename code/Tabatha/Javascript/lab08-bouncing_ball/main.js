let width = 1400;
let height = 600;
let g = .5;
let canvas = document.getElementsByTagName("canvas")[0];
let ctx = canvas.getContext("2d");



function draw(){
    counter = 40;  
    for (var i=0; i<balls.length; ++i) {
        var ball = balls[i];
    
        ctx.beginPath();
        ctx.arc(ball.x, ball.y, ball.radius, 0, 2 * Math.PI, false);
        // ctx.fillStyle = 'green';
            counter += 170;
            counter %= 360;
        ctx.fillStyle = "hsl("+counter+",100%,50%)";
        ctx.fill();
    }
}

function update(){
    for (var i=0; i<balls.length; ++i) {
        var ball = balls[i];
    // update the ball's position
        ball.x += ball.vx;
        // check if it hit a boundary
        if (ball.y<(height-ball.radius*2)){
                ball.vy += g;
            }
            ball.y += ball.vy;
            
            if( ball.x<(ball.radius *2)|| ball.x>(width-ball.radius *2)){
                ball.vx=-(ball.vx * .95);
            }
            if( ball.y<(ball.radius *2)|| ball.y>(height-ball.radius *2)) {
                ball.vy=-(ball.vy * .95);}
                // draw the ball
            alpha = .2;
            ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
            ctx.fillRect(0, 0, width, height)
            // ctx.fillStyle = "hsl("+counter+",100%,50%)";
            // ctx.clearRect(0, 0, width, height);
            // ctx.fillRect(ball.x,ball.y, ball.radius*2, ball.radius*2);
            // ctx.fill()
    }
            // for (var j=0; j<balls.length; ++j) {
            //     var cball = balls[j];
            //     if (ball.x + ball.radius + cball.radius > cball.x 
            //         && ball.x < cball.x + ball.radius + cball.radius
            //         && ball.y + ball.radius + cball.radius > cball.y 
            //         && ball.y < cball.y + ball.radius + cball.radius)
            //         {

            // }
            
}
function main_loop() {
    window.requestAnimationFrame(main_loop);
    update()
    draw()
}
window.requestAnimationFrame(main_loop);


let balls = [];
canvas.addEventListener("click", function(){
    let ball = {
        radius: 20,
        x: Math.random()*width,
        y: 50,
        vx: 2,
        vy: 2
        // vx: (2*Math.random()-1)*2,
        // vy: (2*Math.random()-1)*2
    };
    balls.push(ball);
})