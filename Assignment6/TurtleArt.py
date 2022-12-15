import turtle
import math
tr = turtle.Turtle()

l = 20
tr.lt(150)
for x in range(3,13):
    points = [
        (l * (x-1) * math.cos(k * 2 * math.pi / x),
         l * (x-1) * math.sin(k * 2 * math.pi /x))
        for k in range(1,x+1)
    ]
    tr.penup()
    tr.goto(*points[-1])
    tr.pendown()
    for tx, ty in points:
        tr.goto(tx,ty)
turtle.done()
