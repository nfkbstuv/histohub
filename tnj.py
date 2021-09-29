import pygame as pg
from pg.draw import *

pg.init()

FPS = 30
s = pg.display.set_mode((794,1123))
blue=(125,210,228)
green=(111,192,98)
ochre=(201,172,58)
sy=(226,199,90)  # stands for selective yellow
gray=(100,98,90)
brown=(107,92,67)
white=(242,232,216)
black=(44,38,38)


def main():
 draw_tnj()  # whole picture constructor
 
 
def draw_tnj():
 bg()  # stands for background
 f()  # stands for fence
 g()  # stands for grass
 dh()  # stands for doghouse
 d()  # stands for dog


def bg():
 s.fill(blue)

def f():
 fpoly=pg.Rect(0,1038,794,519)
 rect(s,ochre,fpoly)
 aaline(s,black,[133,1038],[133,519])
 aaline(s,black,[266,1038],[266,519])
 aaline(s,black,[399,1038],[399,519])
 aaline(s,black,[532,1038],[532,519])
 aaline(s,black,[665,1038],[665,519])
 aaline(s,black,[0,519],[794,519])

def g():
 pass

def dh():
 pass

def d():
 pass

main()

pg.display.update()

clock = pg.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()

 
 
 
 
