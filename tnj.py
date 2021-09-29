import math

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
s = pygame.display.set_mode((794, 1123))
blue = (125, 210, 228)
green = (111, 192, 98)
ochre = (201, 172, 58)
sy = (226, 199, 90)
gray = (100, 98, 90)
brown = (107, 92, 67)
white = (242, 232, 216)
black = (44, 38, 38)


def main():
 draw_tnj()
 
 
def draw_tnj():
 bg()
 f()
 g()
 dh()
 d()


def bg():
 s.fill(blue)


def f():
 fpoly = pg.Rect(0, 1038, 794, 519)
 rect(s, ochre, fpoly)
 aaline(s, black, [133, 1038], [133, 519])
 aaline(s, black, [266, 1038], [266, 519])
 aaline(s, black, [399, 1038], [399, 519])
 aaline(s, black, [532, 1038], [532, 519])
 aaline(s, black, [665, 1038], [665, 519])
 aaline(s, black, [0, 519], [794, 519])


def g():
 gpoly = pg.Rect(0, 519, 794, 519)
 rect(s, green, gpoly)
 
 
def dh():
 dhdraw()

def dhdraw():
 roof()
 sq()
 ch()

def roof():
 polygon(s, sy, [500, 500], [570, 480], [550, 550])
 aalines(s, black, True, [500, 500], [570, 250], [550, 550])
 polygon(s, sy, [550, 550], [570, 480], [600, 500], [560, 570])
 aalines(s, black, True, [550, 550], [570, 480], [600, 500], [560, 570])

def sq():
 polygon(s, sy, [500, 500], [500, 300], [570, 250], [570, 480])
 aalines(s, black, True, [500, 500], [500, 300], [570, 250], [570, 480])
 polygon(s, sy, [570, 480], [570, 250], [600, 310], [600, 500])
 aalines(s, black, True, [570, 480], [570, 250], [600, 310], [600, 500])
 circle(s, black, (540, 400), 40)

def ch():
 arc(s, gray, (520, 355, 20, 10), 0, 2*math.pi)
 arc(s, gray, (515, 350, 10, 20), 0, 2*math.pi)
 arc(s, gray, (510, 335, 10, 20), 0, 2*math.pi)
 arc(s, gray, (505, 335, 20, 10), 0, 2*math.pi)
 arc(s, gray, (490, 330, 20, 10), 0, 2*math.pi)
 arc(s, gray, (480, 325, 20, 10), 0, 2*math.pi)
 arc(s, gray, (470, 325, 20, 10), 0, 2*math.pi)
  

def d():
 ddraw()

def ddraw():
 body()
 head()

def body():
 corpus()
 legs()

def corpus():
 pass

def legs():
 pass

def head():
 facenears()
 eyes()
 mouth()

def facenears():
 pass

def eyes():
 pass

def mouth():
 pass


main()

pygame.display.update()

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            finished = True

pygame.quit()

 
 
 
 
