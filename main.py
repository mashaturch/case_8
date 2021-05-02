"""Case-study #8_1
Разработчики:
Турчинович М. (50%), Зубарева Т. (55%) , Костылев М. (25%)
"""

from turtle import *
import ru_local

up()
goto(-150, -50)
down()
speed('fastest')


def get_name_fractal():
    '''This function set the main parameters of turtle anf chose the fractal'''
    print('{}'.format(ru_local.MENU))
    print('\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n'.format(ru_local.SQUARE, ru_local.BINTREE,\
                                                                            ru_local.BRANCH, ru_local.KOCH,\
                                                                            ru_local.SNKOCH, ru_local.MINK,\
                                                                            ru_local.ICEFR1, ru_local.ICEFR2,\
                                                                            ru_local.SNICE, ru_local.LEVI,\
                                                                            ru_local.DRAGON))
    name_fractal = int(input('{}'.format(ru_local.PLEASE)))
    get_color()
    if name_fractal == 1:
        main_square()
    elif name_fractal == 2:
        main_bintree()
    elif name_fractal == 3:
        main_branch()
    elif name_fractal == 4:
        main_koch()
    elif name_fractal == 5:
        main_snowflake_koch()
    elif name_fractal == 6:
        main_minkovskiy()
    elif name_fractal == 7:
        main_ice_fractal()
    elif name_fractal == 8:
        main_ice_fractal_2()
    elif name_fractal == 9:
        main_ice_snowflake()
    elif name_fractal == 10:
        main_levi()
    elif name_fractal == 11:
        main_dragon()

def get_color():
    '''Chosing the turtle color'''
    print('{}'.format(ru_local.MENUC))
    print('\n {}\n {}\n {}\n {}\n {}\n {}\n'.format(ru_local.BLACK, ru_local.WHITE,\
                                                    ru_local.YELLOW, ru_local.RED,\
                                                    ru_local.BLUE, ru_local.GREEN))
    name_color = int(input(ru_local.COLOR1))
    name_bg = int(input(ru_local.COLOR2))
    if name_color == 1:
        pencolor('black')
    elif name_color == 2:
        pencolor('white')
    elif name_color == 3:
        pencolor('yellow')
    elif name_color == 4:
        pencolor('red')
    elif name_color == 5:
        pencolor('blue')
    elif name_color == 6:
        pencolor('green')

    if name_bg == 1:
        bgcolor('black')
    elif name_bg == 2:
        bgcolor('white')
    elif name_bg == 3:
        bgcolor('yellow')
    elif name_bg == 4:
        bgcolor('red')
    elif name_bg == 5:
        bgcolor('blue')
    elif name_bg == 6:
        bgcolor('green')


def main_square():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    square(a, n)

def square(a, n):
    '''Drawing fractal square'''
    if a < 20:
        return
    up()
    right(15)
    forward(a / 8)
    down()
    for _ in range(4):
        forward(a)
        right(90)
    up()
    return square(a*0.9, n - 1)

def main_bintree():
    left(90)
    a = int(input(ru_local.TREE))
    n = int(input(ru_local.ANGLE))
    bintree(a, n)

def bintree(a, n):
    if n == 0:
        return
    else:
        forward(a)
        left(45)
        bintree((3/4 * a), n - 1)
        right(90)
        bintree((3/4 * a), n - 1)
        left(45)
        back(a)

def main_branch():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    branch(n, a)

def branch(n, size):
    '''Drawing binary tree'''
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

def main_koch():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    koch(n, a)

# Кривая Коха.
def koch(order, size):
    '''Drawing koch fractal'''
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

def main_snowflake_koch():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    snowflake_koch()

# снежинка Коха
def snowflake_koch():
    up()
    goto(-150,50)
    down()
    for _ in range (3):
        koch(n, a)
        up()
        right(120)
        down()

def main_minkovskiy():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    minkovskiyh(n, a)

def minkovskiy(order,size):
    '''Drawing minkovskiy fractal'''
    if order == 0:
        forward(size)
    else:
        minkovskiy(order - 1, size / 2)
        left(90)
        minkovskiy(order - 1, size / 2)
        right(90)
        minkovskiy(order - 1, size / 2)
        right(90)
        minkovskiy(order - 1, size / 2)
        minkovskiy(order - 1, size / 2)
        left(90)
        minkovskiy(order - 1, size / 2)
        left(90)
        minkovskiy(order - 1, size / 2)
        right(90)
        minkovskiy(order - 1, size / 2)

def main_ice_fractal():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    ice_fractal(n, a)

def ice_fractal(order, size):
    '''Drawing ice fracral (picture 1)'''
    if order == 0:
        forward(size)
    else:
        ice_fractal(order - 1, size / 2)
        left(90)
        ice_fractal(order - 1, size / 4)
        ice_fractal(order - 1, - size / 4)
        right(90)
        ice_fractal(order - 1, size / 2)

def main_ice_fractal_2():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    ice_fractal_2(n, a)


def ice_fractal_2(n, a):
    '''Drawing ice fracral (picture 2)'''
    if n == 0:
        forward(a)
    else:
        ice_fractal_2(n-1, a/2)
        left (120)
        ice_fractal_2(n - 1, a/4)
        left (180)
        ice_fractal_2(n - 1, a/4)
        left(120)
        ice_fractal_2(n - 1, a/4)
        left(180)
        ice_fractal_2(n - 1, a/4)
        left(120)
        ice_fractal_2(n - 1, a /2)

def main_ice_snowflake():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    ice_snowflake(n, a)

def ice_snowflake(n, a):
    '''Drawing snowflake ice fracral'''
    for _ in range (6):
        left(60)
        ice_fractal(n, a)
        right(180)
        ice_fractal(n, a)
        left(60)

def main_levi():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    ice_fractal_2(n, a)

def levi(order, size):
    '''Drawing levi fractal'''
    if order == 0:
        forward(size)
    else:
        left(45)
        levi(order - 1, size / 2)
        right(90)
        levi(order - 1, size / 2)
        left(45)

def main_dragon():
    a = int(input(ru_local.LENGHT))
    n = int(input(ru_local.RECURTION))
    dragon(n, a)

def dragon(n, a):
    '''Drawing dragon fractal'''
    if n == 0:
        forward(a)
    else:
        left(45)
        dragon(n - 1, a / 2)
        right(90)
        dragon_2(n - 1, a / 2)
        left(45)

def dragon_2(n, a):
    if n == 0:
        forward(a)
    else:
        right(45)
        dragon(n - 1, a/2)
        left(90)
        dragon_2(n - 1, a/2)
        right(45)

get_name_fractal()

mainloop()
hideturtle()