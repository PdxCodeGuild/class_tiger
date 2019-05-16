let canvas = document.getElementById('bouncingball');
let ctx = canvas.getContext('2d');

let ball = {
    radius: 16,
    px: Math.random() * 800,
    py: Math.random() * 600,
    vx: (2 * Math.random() - 1) * 10,
    vy: (2 * Math.random() - 1) * 10,
    draw: function () {
        ctx.beginPath();
        ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = 'green';
        ctx.fill();
    }
};


ball.draw();

function main_loop() {
    ctx.clearRect(0, 0, 800, 600);
    ball.draw();
    ball.px += ball.vx;
    ball.py += ball.vy;


    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);