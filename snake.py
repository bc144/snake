

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = 'green'

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def color3():
    """Change snake color."""
    randColor = randrange(1, 6)
    color = 'black'
    if randColor == 1:
        color = 'black'
    elif randColor == 2:
        color = 'pink'
    elif randColor == 3:
        color = 'gray'
    elif randColor == 4:
        color = 'cyan'
    elif randColor == 5:
        color = 'lightgreen'
    else:
        color = 'skyblue'
    return color

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    
    snake.append(head)

    global color
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    
        randColor = randrange(1, 6)
        if randColor == 1:
            color = 'green'
        elif randColor == 2:
            color = 'purple'
        elif randColor == 3:
            color = 'orange'
        elif randColor == 4:
            color = 'brown'
        elif randColor == 5:
            color = 'yellow'
        else:
            color = 'blue'
        print(color)
    else:
        snake.pop(0)

    clear()
    
    randNum = randrange(12)
    if randNum == 0:
        food.x -= 10
    elif randrange(100) == 1:
        food.x += 10
    elif randrange(10) == 2:
        food.y -= 10
    elif randrange(100) == 3:
        food.y += 10
        
    for body in snake:
        square(body.x, body.y, 9, color3())

    square(food.x, food.y, 9, color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
