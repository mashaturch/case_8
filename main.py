from turtle import *

# Кривая Коха.
def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)

# снежинка Коха
def snowflake_koch():
    up()
    goto(-150,50)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    for _ in range (3):
        koch(n, a)
        up()
        right(120)
        down()


def square (a):
    if a < 20:
        return
    up()
    right (15)
    forward(a / 8)
    down()
    for _ in range (4):
        forward(a)
        right(90)
    up()
    return square(a * 0.9)

# Фрактал "Ветка"
def branch(n, size):
    if n == 0:
        left(180)
        return

    x = size/(n+1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        right(135)

    forward(x)
    left(180)
    forward(size)
up()
goto(0,-100)
left(90)
down()
branch(5,400)


square(120)


speed(100)
mainloop()
hideturtle()