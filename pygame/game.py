from typing import Tuple
import pygame
from pygame.locals import *
from Entity import Entity, Player, Enemy
from HexGrid import HexGrid, HexLocation
from LevelScene import LevelScene
import math

pygame.init()
screen = pygame.display.set_mode([1000, 1000])
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

levelScene = LevelScene()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    screen.fill((0, 0, 0)) 
    levelScene.render(screen)
    pygame.display.flip()

