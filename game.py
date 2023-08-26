import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([1000, 1000])
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

