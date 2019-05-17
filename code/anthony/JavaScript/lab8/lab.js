let canvas = document.querySelector('canvas');
let ctx = canvas.getContext('2d');

let height = document.documentElement.clientHeight;
let width = document.documentElement.clientWidth;


function Ball() {
    this.x = Math.random() * width;
    this.y = Math.random() * height;
    this.radius = 16;
    this.vx = (2 * Math.random() - 1) * 10;
    this.vy = (2 * Math.random() - 1) * 10;
    this.gravity = .8;
    this.bounce = .9;
    this.friction = .01;
    this.color = 'rgb(' + Math.floor(Math.random() * 256) + ',' + Math.floor(Math.random() * 256) + ',' + Math.floor(Math.random() * 256) + ')';

    this.draw = function () {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, false);
        ctx.fillStyle = this.color;
        ctx.fill();
    }

    this.update = function () {
        this.vy += this.gravity;
        this.x += this.vx;
        this.y += this.vy;

        if (this.x - this.radius < 0 || this.x + this.radius > width) {
            this.vx *= -this.bounce;
            if (Math.abs(this.vx) < 1) {
                this.vx = 0;
            }
        } else if (this.y - this.radius < 0) {
            this.vy *= -this.bounce;
        } else if (this.y + this.radius > height) {
            this.y = height - this.radius;
            this.vy *= -this.bounce;
            if (this.vy < 0 && this.vy > -2) {
                this.vy = 0;
            }
        }
        if (this.vx > 0) {
            this.vx -= this.friction;
        } else {
            this.vx += this.friction;
        }

        this.draw();
    }
};

let balls = new Array();
canvas.addEventListener('mousedown', function () {
    balls.push(new Ball());
})


function main_loop() {
    // ctx.clearRect(0, 0, 800, 600);
    ctx.canvas.height = height;
    ctx.canvas.width = width;


    for (let ball of balls) {
        ball.update();
    }


    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);