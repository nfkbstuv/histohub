from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'blue', 'green']


def new_ball():
    global x, y, r, ball
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    ball = canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
    root.after(2000, new_ball)


def click(event):
    global points, x, tekst
    if (event.y - y)**2 + (event.x - x)**2 < r**2:
        points += 1
        x = -1000
        canv.delete(tekst)
        canv.delete(ball)
        tekst = canv.create_text(20, 20, text=str(points), font='Helvetica 36')
    else:
        points += 0
        x = -1000


def wclick(event):
    global points, x, tekst
    if sth:   # Найди функцию для щарика
        points += 1
        x = -1000
        canv.delete(tekst)
        canv.delete(ball)   # найди, что вычесть
        tekst = canv.create_text(20, 20, text=str(points), font='Helvetica 36')
    else:
        points += 0
        x = -1000


tekst = canv.create_text(20, 20, text=0, font='Helvetica 36')
points = 0
new_ball()
canv.bind('<Button>', click)
canv.bind('<Button>', wclick)

root.mainloop()
