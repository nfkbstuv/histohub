import math

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
s = pygame.display.set_mode((794, 1123))
blue = (119, 186, 208)
green = (102, 197, 121)
dgreen = (70, 90, 63)
ochre = (195, 172, 77)
fline = (103, 90, 40)
sy = (195, 172, 77)
oroof = (205, 172, 57)
gray = (109, 103, 83)
chgray = (12, 25, 15)
brown = (108, 103, 85)
white = (250, 250, 250)
black = (0, 0, 0)


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
 fpoly = pygame.Rect((0, 175, 794, 463))
 rect(s, ochre, fpoly)
 aaline(s, fline, [50, 175], [50, 638])
 aaline(s, fline, [113, 175], [113, 638])
 aaline(s, fline, [178, 175], [178, 638])
 aaline(s, fline, [234, 175], [234, 638])
 aaline(s, fline, [293, 175], [293, 638])
 aaline(s, fline, [345, 175], [345, 638])
 aaline(s, fline, [396, 175], [396, 638])
 aaline(s, fline, [450, 175], [450, 638])
 aaline(s, fline, [506, 175], [506, 638])
 aaline(s, fline, [553, 175], [553, 638])
 aaline(s, fline, [608, 175], [608, 638])
 aaline(s, fline, [668, 175], [668, 638])
 aaline(s, fline, [719, 175], [719, 638])
 aaline(s, fline, [763, 175], [763, 638])
 aaline(s, dgreen, [0, 638], [794, 638])


def g():
 gpoly = pygame.Rect((0, 638, 794, 485))
 rect(s, green, gpoly)
 
 
def dh():
 dhdraw()

def dhdraw():
 roof()
 sq()
 ch()

def roof():
 polygon(s, oroof, [[503, 680], [643, 714], [578, 586]])
 aalines(s, black, True, [[503, 680], [643, 714], [578, 586]])
 polygon(s, oroof, [[578, 586], [643, 714], [687, 669], [626, 560]])
 aalines(s, black, True, [[578, 586], [643, 714], [687, 669], [626, 560]])

def sq():
 polygon(s, sy, [[503, 680], [503, 824], [643, 897], [643, 714]])
 aalines(s, black, True, [[503, 680], [503, 824], [643, 897], [643, 714]])
 polygon(s, sy, [[643, 714], [643, 897], [687, 800], [687, 669]])
 aalines(s, black, True, [[643, 714], [643, 897], [687, 800], [687, 669]])
 circle(s, black, (562, 779), 45)

def ch():
 arc(s, chgray, (525, 810, 25, 11), 0, 2*math.pi)
 ellipse(s, gray, (515, 811, 17, 20), 0, 2*math*pi)
 arc(s, chgray, (515, 811, 17, 20), 0, 2*math.pi)
 arc(s, chgray, (503, 824, 25, 20), 0, 2*math.pi)
 arc(s, chgray, (489, 839, 26, 10), 0, 2*math.pi)
 arc(s, chgray, (482, 845, 14, 13), 0, 2*math.pi)
 arc(s, chgray, (450, 851, 39, 13), 0, 2*math.pi)
 arc(s, chgray, (433, 856, 20, 10), 0, 2*math.pi)
 arc(s, chgray, (408, 855, 30, 5), 0, 2*math.pi)
 arc(s, chgray, (399, 849, 17, 18), 0, 2*math.pi)
 arc(s, chgray, (381, 861, 25, 7), 0, 2*math.pi)
 arc(s, chgray, (366, 866, 27, 13), 0, 2*math.pi)
  

def d():
 ddraw()

def ddraw():
 body()
 head()

def body():
 corpus()
 legs()

def corpus():
 ellipse(s, brown, (209, 803, 112, 70))
 ellipse(s, browm, (91, 819, 169, 97))

def legs():
 leg1()
 leg2()
 leg3()
 leg4()

def leg1():
 ellipse(s, brown, (68, 852, 55, 111))
 ellipse(s, brown, (55, 959, 58, 21))

def leg2():
 ellipse(s, brown, (160, 892, 56, 98))
 ellipse(s, brown, (147, 987, 52, 19))

def leg3():
 ellipse(s, brown, (212, 803, 40, 74))
 ellipse(s, brown, (254, 869, 18, 49))
 ellipse(s, brown, (227, 916, 40, 18))
 
def leg4():
 ellipse(s, brown, (278, 835, 72, 97))
 ellipse(s, brown, (323, 885, 18, 64))
 ellipse(s, brown, (295, 946, 41, 20))

def head():
 facenears()
 eyes()
 mouth()

def facenears():
 polygon(s, brown, [[80, 777], [81, 893], [187, 893], [187, 777]])
 aalines(s, black, True, [[80, 777], [81, 893], [187, 893], [187, 777]])
 ellipse(s, brown, (63, 779, 30, 35))
 arc(s, black, (63, 779, 30, 35), 0, 2*math.pi)
 ellipse(s, brown, (171, 778, 30, 35))
 arc(s, black, (171, 778, 30, 35), 0, 2*math.pi)

def eyes():
 ellipse(s, white, (100, 818, 23, 9))
 arc(s, black, (100, 818, 23, 9), 0, 2*math.pi)
 ellipse(s, black, (106, 818, 9, 7))
 ellipse(s, white, (143, 818, 23, 9))
 arc(s, black, (143, 818, 23, 9), 0, 2*math.pi)
 ellipse(s, black, (149, 818, 9, 7))

def mouth():
 arc(s, black, (100, 858, 67, 20), 0, math.pi)
 polygon(s, white, [[105, 868], [113, 861], [108, 850]])
 aalines(s, black, True, [[105, 868], [113, 861], [108, 850]])
 polygon(s, white, [[151, 862], [160, 869], [156, 851]])
 aalines(s, black, True, [[151, 862], [160, 869], [156, 851]])


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

 
 
 
 
