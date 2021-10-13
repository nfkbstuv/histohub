from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'black']
cc = choice(colors)
f = 10  # Произвольное число шариков, находящихся на холсте
points = 0


class ball(object):
    """ Класс шариков с:
       х, у - координаты центра шарика, r - радиус шарика, color - цвет

       """

    def __init__(self, x, y, r, color, ax=rnd(2, 5), ay=rnd(2, 5)):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.ax = ax  # Проекция вектора скорости на х
        self.ay = ay  # Проекция вектора скорости на у


balls = []
for i in range(f):
    balls.append(ball(rnd(100, 700), rnd(100, 500), rnd(30, 50), choice(colors)))


def new_ball():
    """ Функция, отрисовывающая новые шарики каждые 2,5 секунд
   х, у - координаты центра шарика, r - радиус шарика

   """
    global ball1, cc
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    cc = choice(colors)
    for i in range(f):
        canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r,
                         balls[i].y + balls[i].r, fill=balls[i].color, width=0)
    root.after(2500, mball)


def mball():
    """ Функция, отвечающая за движение шарика и его отталкивание от стенок
    Просто движение на холсте выполняется прибавление рандомного значения из ax, xy
    Отталкивание от 4 стенок задаётся через размеры холста и радиус шарика

    """
    for i in range(f):
        balls[i].y += balls[i].ay
        balls[i].x += balls[i].ax
        if balls[i].x > 800 - balls[i].r or balls[i].x < 0 + balls[i].r:
            balls[i].ax *= -1
        if balls[i].y > 600 - balls[i].r or balls[i].y < 0 + balls[i].r:
            balls[i].ay *= -1
    canv.delete(ALL)
    for i in range(f):
        canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r,
                         balls[i].y + balls[i].r, fill=balls[i].color,
                         width=0)
    canv.create_text(20, 20, text=str(points), font="Helvetica 36")
    root.after(10, mball)


def click(event):
    """ Функция, задающая ответ клик мыши
   Шарики black - бомбы, которые обнуляют счёт points
   
   """
    global points, x, tekst
    for i in range(f):
        if (event.y - balls[i].y) ** 2 + (event.x - balls[i].x) ** 2 <= balls[i].r ** 2:
            if balls[i].color == 'black':
                points = 0
                x = -1000
                canv.delete(tekst)
            else:
                points += 1
                x = -1000
                canv.delete(tekst)
        tekst = canv.create_text(20, 20, text=str(points), font='Helvetica 36')  # Текст, отображающий текущие points


tekst = canv.create_text(20, 20, text=0, font='Helvetica 36')
new_ball()
canv.bind('<Button>', click)

root.mainloop()
