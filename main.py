import pygame, sys
from settings import *
from level import Level
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((screen_width, screen_height))
clock=pygame.time.Clock()
level = Level(screen)
mixer.init()
mixer.music.load('music.ogg')
mixer.music.set_volume(0.7)
mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    if(level.gameover):
        level=Level(screen)
    level.run()

    pygame.display.update()
    clock.tick(60)