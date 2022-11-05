import pygame as pg
from pygame.draw import *
import sys
import Color

pg.init()

FPS = 30
screen = pg.display.set_mode((400, 570))
pg.display.set_caption("Picture")
screen.fill(Color.THECOLORS['blue4'])
rect(screen, pg.Color(Color.THECOLORS['darkolivegreen4']), (0, 285, 400, 285))
circle(screen, pg.Color(Color.THECOLORS['azure']), (230, 140), 50)
ellipse(screen, pg.Color(Color.THECOLORS['cornsilk3']), (-60, 100, 250, 60))
ellipse(screen, pg.Color(Color.THECOLORS['gray23']), (280, 57, 200, 40))
ellipse(screen, pg.Color(Color.THECOLORS['gray26']), (100, 130, 360, 70))


def man(layer):
    ellipse(layer, pg.Color(Color.THECOLORS['gray99']), (260, 368, 35, 80))
    polygon(layer, pg.Color(Color.THECOLORS['aliceblue']), ((277, 366),
                                                             (300, 341), (249, 328), (267, 366)))
    circle(layer, pg.Color(Color.THECOLORS['aliceblue']), (272, 365), 6)
    circle(layer, pg.Color(Color.THECOLORS['aliceblue']), ((259, 381)), 10)
    circle(layer, pg.Color(Color.THECOLORS['aliceblue']), ((294, 381)), 10)
    ellipse(layer, pg.Color(Color.THECOLORS['gray99']), (244, 387, 13, 25))
    ellipse(layer, pg.Color(Color.THECOLORS['gray99']), (296, 387, 13, 25))
    ellipse(layer, pg.Color(Color.THECOLORS['gray99']), (303, 406, 26, 13))
    ellipse(layer, pg.Color(Color.THECOLORS['gray99']), (232, 409, 26, 13))
    ellipse(layer, pg.Color(Color.THECOLORS['gray99']), (258, 440, 18, 37))
    ellipse(layer, pg.Color(Color.THECOLORS['gray99']), (280, 442, 18, 37))
    circle(layer, pg.Color(Color.THECOLORS['red']), (334, 396), 15)
    circle(layer, pg.Color(Color.THECOLORS['gray99']), (253, 332), 4)
    circle(layer, pg.Color(Color.THECOLORS['gray99']), (297, 344), 4)



"""человек"""

surface_man = pg.Surface((400, 570), pg.SRCALPHA)
surface_man.fill(Color.THECOLORS['transparent'])
surface_man_mirror = pg.Surface((400, 570), pg.SRCALPHA)
surface_man_mini = pg.Surface((400, 570), pg.SRCALPHA)





man(surface_man_mini)
man(surface_man)
man(screen)
man(surface_man_mirror)
surface_man_mini = pg.transform.scale(surface_man_mini, (200, 285))
surface_man_mirror = pg.transform.flip(surface_man_mirror, True, False)
screen.blit(surface_man, (-70, -111))
screen.blit(surface_man_mirror, (20, 60))
screen.blit(surface_man_mini, (-70, 150))


'''Летающая тарелка'''
surface = pg.Surface((400, 570), pg.SRCALPHA)
polygon(surface, pg.Color(Color.THECOLORS['antiquewhite2']),
        ((16, 422), (92, 218), (172, 422)))
screen.blit(surface, (0, 0))
ellipse(screen, pg.Color(Color.THECOLORS['gray73']), (10, 200, 170, 70))
ellipse(screen, pg.Color(Color.THECOLORS['gray53']), (30, 195, 130, 50))
ellipse(screen, pg.Color(Color.THECOLORS['gray99']), (21, 236, 30, 15))
ellipse(screen, pg.Color(Color.THECOLORS['gray99']), (66, 253, 30, 15))
ellipse(screen, pg.Color(Color.THECOLORS['gray99']), (118, 254, 30, 15))
ellipse(screen, pg.Color(Color.THECOLORS['gray99']), (143, 228, 30, 15))









pg.display.update()

clock = pg.time.Clock()
while 1:
    clock.tick(FPS)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if pressed[0]:
        print(pos)
        pg.display.update()


