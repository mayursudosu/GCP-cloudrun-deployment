from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Neon Snake Game</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, Helvetica, sans-serif;
        }

        body{
            background:#050510;
            overflow:hidden;
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
            color:white;
        }

        .container{
            text-align:center;
        }

        h1{
            font-size:3rem;
            color:#00ffcc;
            text-shadow:
                0 0 10px #00ffcc,
                0 0 20px #00ffcc,
                0 0 40px #00ffcc;
            margin-bottom:15px;
        }

        canvas{
            border:3px solid #00ffcc;
            box-shadow:
                0 0 20px #00ffcc,
                0 0 50px #00ffcc;
            background:#0b0b1a;
            border-radius:12px;
        }

        .score{
            margin:15px;
            font-size:1.5rem;
            color:#ff00ff;
            text-shadow:
                0 0 10px #ff00ff,
                0 0 20px #ff00ff;
        }

        .game-over{
            position:absolute;
            top:50%;
            left:50%;
            transform:translate(-50%, -50%) scale(0);
            font-size:4rem;
            color:#ff004c;
            text-shadow:
                0 0 15px #ff004c,
                0 0 40px #ff004c,
                0 0 80px #ff004c;
            opacity:0;
            transition:0.5s ease;
        }

        .show{
            transform:translate(-50%, -50%) scale(1);
            opacity:1;
        }

        .restart{
            margin-top:15px;
            padding:10px 20px;
            border:none;
            border-radius:10px;
            background:#00ffcc;
            color:black;
            font-weight:bold;
            cursor:pointer;
            box-shadow:
                0 0 15px #00ffcc,
                0 0 30px #00ffcc;
            transition:0.2s;
        }

        .restart:hover{
            transform:scale(1.05);
        }

    </style>
</head>
<body>

<div class="container">
    <h1>NEON SNAKE</h1>

    <div class="score">Score: <span id="score">0</span></div>

    <canvas id="game" width="500" height="500"></canvas>

    <br>

    <button class="restart" onclick="restartGame()">
        Restart
    </button>
</div>

<div class="game-over" id="gameOver">
    GAME OVER
</div>

<script>

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const box = 20;

let snake = [
    {x: 10 * box, y: 10 * box}
];

let direction = "RIGHT";

let food = {
    x: Math.floor(Math.random() * 24) * box,
    y: Math.floor(Math.random() * 24) * box
};

let score = 0;
let game;

document.addEventListener("keydown", changeDirection);

function changeDirection(event){

    if(event.key === "ArrowLeft" && direction !== "RIGHT")
        direction = "LEFT";

    else if(event.key === "ArrowUp" && direction !== "DOWN")
        direction = "UP";

    else if(event.key === "ArrowRight" && direction !== "LEFT")
        direction = "RIGHT";

    else if(event.key === "ArrowDown" && direction !== "UP")
        direction = "DOWN";
}

function collision(head, array){

    for(let i = 0; i < array.length; i++){

        if(head.x === array[i].x && head.y === array[i].y){
            return true;
        }
    }

    return false;
}

function draw(){

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Grid glow
    for(let i = 0; i < 25; i++){

        ctx.strokeStyle = "rgba(0,255,255,0.08)";

        ctx.beginPath();
        ctx.moveTo(i * box, 0);
        ctx.lineTo(i * box, canvas.height);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(0, i * box);
        ctx.lineTo(canvas.width, i * box);
        ctx.stroke();
    }

    // Snake
    for(let i = 0; i < snake.length; i++){

        ctx.fillStyle = i === 0 ? "#00ffcc" : "#00cc88";

        ctx.shadowBlur = 20;
        ctx.shadowColor = "#00ffcc";

        ctx.fillRect(snake[i].x, snake[i].y, box, box);
    }

    // Food
    ctx.fillStyle = "#ff00ff";
    ctx.shadowBlur = 30;
    ctx.shadowColor = "#ff00ff";

    ctx.beginPath();
    ctx.arc(food.x + 10, food.y + 10, 8, 0, Math.PI * 2);
    ctx.fill();

    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    if(direction === "LEFT") snakeX -= box;
    if(direction === "UP") snakeY -= box;
    if(direction === "RIGHT") snakeX += box;
    if(direction === "DOWN") snakeY += box;

    // Eat food
    if(snakeX === food.x && snakeY === food.y){

        score++;
        document.getElementById("score").innerText = score;

        food = {
            x: Math.floor(Math.random() * 24) * box,
            y: Math.floor(Math.random() * 24) * box
        };

    } else {

        snake.pop();
    }

    let newHead = {
        x: snakeX,
        y: snakeY
    };

    // Game over
    if(
        snakeX < 0 ||
        snakeY < 0 ||
        snakeX >= canvas.width ||
        snakeY >= canvas.height ||
        collision(newHead, snake)
    ){

        clearInterval(game);

        document
            .getElementById("gameOver")
            .classList.add("show");

        return;
    }

    snake.unshift(newHead);
}

function restartGame(){

    snake = [
        {x: 10 * box, y: 10 * box}
    ];

    direction = "RIGHT";

    score = 0;

    document.getElementById("score").innerText = score;

    food = {
        x: Math.floor(Math.random() * 24) * box,
        y: Math.floor(Math.random() * 24) * box
    };

    document
        .getElementById("gameOver")
        .classList.remove("show");

    clearInterval(game);

    game = setInterval(draw, 100);
}

game = setInterval(draw, 100);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    # INTENTIONAL BUG FOR INCIDENT RESPONSE PHASE
    1 / 0
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)