"""David Antonio Zarate Villaseñor A01665896
Christopher Gordillo Dominguez A01666339
"""
"""Paint, for drawing shapes.

Exercises

1. Add a color.  (Yellow)
2. Complete circle. 
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector
import math

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def makecircle(start, end):
    """Draw circle from start to end."""
    up()
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5  
    goto(start.x, start.y - radius) 
    down()
    begin_fill()
    circle(radius)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up ()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)

    end_fill()

def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    goto(end.x, start.y)  # Base del triángulo
    goto((start.x + end.x) / 2, end.y)  # Vértice superior
    goto(start.x, start.y)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Store value in state at key."""
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')  
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', makecircle), 'c')  
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

