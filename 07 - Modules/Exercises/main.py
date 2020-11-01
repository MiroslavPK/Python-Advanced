import turtle
import snake_game
import time

game = snake_game.Game()

# screen settings
screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False)
screen.title('Snake')
screen.bgcolor('grey')
screen.setup(width=600, height=600)
screen.tracer(0)

# snake_head
snake_head = turtle.Turtle()
snake_head.shape('square')
snake_head.color('green')
snake_head.shapesize(0.5, 0.5)
snake_head.penup()

# food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.shapesize(0.5, 0.5)
food.penup()
food.goto(game.food_position())

# key bindings
screen.listen()
screen.onkeypress(game.go_up, 'Up')
screen.onkeypress(game.go_down, 'Down')
screen.onkeypress(game.go_left, 'Left')
screen.onkeypress(game.go_right, 'Right')

# game over text
game_over = turtle.Turtle()
game_over.clear()
game_over.hideturtle()
game_over.color('red')
game_over.goto(0, 0)

# score
score = 0
h_score = game.high_score()

score_draw = turtle.Turtle()
score_draw.speed(0)
score_draw.shape("square")
score_draw.color("white")
score_draw.penup()
score_draw.hideturtle()
score_draw.goto(0, 260)
score_draw.write(f"Score: 0, High Score: {h_score}", align="center", font=("Courier", 24, "normal"))

delay = 0.065
while True:
    screen.update()
    game.move()

    # snake_body
    snake_body = game.body_position()

    if game.border_check() or (len(snake_body) > 0 and game.body_collision_check()):
        game.restart()
        game.game_over_update()
        game_over.write('GAME OVER', align='center', font=('Courier', 30, 'bold'))
        score = 0
        time.sleep(1)
        game_over.clear()
        score_draw.clear()
        score_draw.write(f"Score: {score}, High Score: {h_score}", align="center", font=("Courier", 24, "normal"))
        game.food_respawn()
        delay = 0.065

    if snake_head.distance(game.food_position()) < 9:
        # increase points and update text
        score += 10
        if score > h_score:
            h_score = score
            game.new_record(h_score)

        score_draw.clear()
        score_draw.write(f"Score: {score}, High Score: {h_score}", align="center", font=("Courier", 24, "normal"))

        # respawn the food at a random point
        game.food_respawn()

        # increase body length
        body_segment = turtle.Turtle()
        body_segment.shape('square')
        body_segment.color('green')
        body_segment.shapesize(0.5, 0.5)
        body_segment.penup()
        game.add_body_segment(body_segment)

        # increase the game speed
        if len(snake_body) >= 5 and delay > 0.001:
            delay -= 0.0025

    for i in range(len(snake_body) - 1, 0, -1):
        x, y = snake_body[i - 1].xcor(), snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)

    if len(snake_body) > 0:
        snake_body[0].goto(snake_head.xcor(), snake_head.ycor())

    snake_head.goto(game.head_position())
    food.goto(game.food_position())

    time.sleep(delay)
