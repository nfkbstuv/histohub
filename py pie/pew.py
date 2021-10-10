from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'black']
ax = rnd(-10, 10)
ay = rnd(-10, 10)
b = set()
points = 0


def new_ball():
    global x, y, r, ball, cc
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    cc = choice(colors)
    ball = canv.create_oval(x-r, y-r, x+r, y+r, fill=cc, width=0)
    root.after(2500, new_ball)


def click(event):
    global points, x, tekst
    if (event.y - y)**2 + (event.x - x)**2 < r**2:
        if cc == 'black':
            points = 0
            x = -1000
            canv.delete(ALL)
        else:
            points += 1
            x = -1000
            canv.delete(tekst)
            canv.delete(ball)
        tekst = canv.create_text(20, 20, text=str(points), font='Helvetica 36')


tekst = canv.create_text(20, 20, text=0, font='Helvetica 36')
new_ball()
canv.bind('<Button>', click)

root.mainloop()
