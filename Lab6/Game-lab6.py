import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 25
screen = pygame.display.set_mode((1100, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
i = 0
x = randint(100, 1000)
y = randint(100, 500)
r = randint(10, 100)
x1 = randint(100, 1000)
y1 = randint(100, 500)
r1 = randint(10, 100)
x2 = randint(100, 1000)
y2 = randint(100, 500)
r2 = randint(10, 100)
x3 = randint(0, 1000)
y3 = randint(0, 500)
color = COLORS[randint(0, 5)]
color1 = COLORS[randint(0, 5)]
color2 = COLORS[randint(0, 5)]
color3 = COLORS[randint(0, 5)]
dx = randint(-50, 50)
dy = randint(-50, 50)
dx1 = randint(-50, 50)
dy1 = randint(-50, 50)
dx2 = randint(-50, 50)
dy2 = randint(-50, 50)
dx3 = randint(10, 50)
RIGHT = 'run to right'
LEFT = 'run to left'
UP = 'run to up'
DOWN = 'run to down'
direction_x = RIGHT
direction_y = DOWN
direction_x1 = RIGHT
direction_y1 = DOWN
direction_x2 = RIGHT
direction_y2 = DOWN
direction_x3 = RIGHT

rating = {}

'''приветствие'''
print("Привет, стрелок! Как тебя зовут?")
name = input()
print(f'{name}, за работу!')


def new_ball():
    """рисует новый шарик """
    global direction_x, direction_y, x, y, r
    if dx >= 0:
        if x + r >= 1100:
            direction_x = LEFT
        elif x - r <= 0:
            direction_x = RIGHT
        if direction_x == RIGHT:
            x += dx
        else:
            x -= dx
    else:
        if x + r >= 1100:
            direction_x = RIGHT
        elif x - r <= 0:
            direction_x = LEFT
        if direction_x == RIGHT:
            x += dx
        else:
            x -= dx
    if dy >= 0:
        if y + r >= 600:
            direction_y = UP
        elif y - r <= 0:
            direction_y = DOWN
        if direction_y == UP:
            y -= dy
        else:
            y += dy
    else:
        if y + r >= 600:
            direction_y = DOWN
        elif y - r <= 0:
            direction_y = UP
        if direction_y == DOWN:
            y += dy
        else:
            y -= dy

    circle(screen, color, (x, y), r)

#def new_ball1():
    '''рисует новый шарик '''

    #color = COLORS[randint(0, 5)]
    #circle(screen, color, (x1, y1), r1)

#def new_ball2():
    '''рисует новый шарик '''

    #color = COLORS[randint(0, 5)]
    #circle(screen, color, (x2, y2), r2)


def new_ball1():
    """рисует новый шарик """
    global direction_x1, direction_y1, x1, y1, r1
    if dx1 >= 0:
        if x1 + r1 >= 1100:
            direction_x1 = LEFT
        elif x1 - r1 <= 0:
            direction_x1 = RIGHT
        if direction_x1 == RIGHT:
            x1 += dx1
        else:
            x1 -= dx1
    else:
        if x1 + r1 >= 1100:
            direction_x1 = RIGHT
        elif x1 - r1 <= 0:
            direction_x1 = LEFT
        if direction_x1 == RIGHT:
            x1 += dx1
        else:
            x1 -= dx1
    if dy1 >= 0:
        if y1 + r1 >= 600:
            direction_y1 = UP
        elif y1 - r1 <= 0:
            direction_y1 = DOWN
        if direction_y1 == UP:
            y1 -= dy1
        else:
            y1 += dy1
    else:
        if y1 + r1 >= 600:
            direction_y1 = DOWN
        elif y1 - r1 <= 0:
            direction_y1 = UP
        if direction_y1 == DOWN:
            y1 += dy1
        else:
            y1 -= dy1
    circle(screen, color1, (x1, y1), r1)


def new_ball2():
    """рисует новый шарик """
    global direction_x2, direction_y2, x2, y2, r2
    if dx2 >= 0:
        if x2 + r2 >= 1100:
            direction_x2 = LEFT
        elif x2 - r2 <= 0:
            direction_x2 = RIGHT
        if direction_x2 == RIGHT:
            x2 += dx2
        else:
            x2 -= dx2
    else:
        if x2 + r2 >= 1100:
            direction_x2 = RIGHT
        elif x2 - r2 <= 0:
            direction_x2 = LEFT
        if direction_x2 == RIGHT:
            x2 += dx2
        else:
            x2 -= dx2
    if dy2 >= 0:
        if y2 + r2 >= 600:
            direction_y2 = UP
        elif y2 - r2 <= 0:
            direction_y2 = DOWN
        if direction_y2 == UP:
            y2 -= dy2
        else:
            y2 += dy2
    else:
        if y2 + r2 >= 600:
            direction_y2 = DOWN
        elif y2 - r2 <= 0:
            direction_y2 = UP
        if direction_y2 == DOWN:
            y2 += dy2
        else:
            y2 -= dy2
    circle(screen, color2, (x2, y2), r2)


def cube():
    global x3, y3, direction_x3, dx3
    if x3 >= 1000:
        direction_x3 = LEFT
    elif x3 <= 0:
        direction_x3 = RIGHT
    if direction_x3 == RIGHT:
        x3 += dx3
    else:
        x3 -= dx3
    rect(screen, color3, (x3, y3, 100, 100))


def click():
    '''target hit calculation'''
    global i
    target_distance = ((x - event.pos[0]) ** 2
                       + (y - event.pos[1]) ** 2) ** 0.5
    target_distance1 = ((x1 - event.pos[0]) ** 2
                        + (y1 - event.pos[1]) ** 2) ** 0.5
    target_distance2 = ((x2 - event.pos[0]) ** 2
                        + (y2 - event.pos[1]) ** 2) ** 0.5

    if target_distance < r1 or target_distance1 < r1 or target_distance2 < r2:
        i += 1
        return i
    elif x3 < event.pos[0] < (x3 + 100) and y3 < event.pos[1] < (y3 + 100):
        i += 0.5
        return i
    else:
        i -= 1
        return i


def goal():
    global i
    n = str(i)
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render(n, True, RED)
    screen.blit(text1, (10, 50))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    """main loop"""
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rating[name] = i
            with open('ratings', 'a') as out:
                for key, val in rating.items():
                    out.write('{}:{}\n'.format(key, val))
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click()

    new_ball()
    new_ball1()
    new_ball2()
    cube()
    pygame.display.update()
    screen.fill(BLACK)
    goal()


pygame.quit()
