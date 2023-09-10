from typing import Tuple
import pygame
from pygame.locals import *
from Entity import Entity, Player, Enemy
from HexGrid import HexGrid, HexLocation
from Scene import Scene
from LevelScene import LevelScene
from MenuScene import MenuScene
import math
from events import *

pygame.init()
screen = pygame.display.set_mode([1000, 1000])
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

levelScene = LevelScene()
menuScene = MenuScene(screen)

scenes = [menuScene, levelScene]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

currentScene: Scene = menuScene
while running:
    changed = True
    events = pygame.event.get()
    for event in events:
        if event.type == MENU_SCENE:
            currentScene = menuScene
        elif event.type == NEW_GAME_SCENE:
            currentScene = levelScene
        elif event.type == OPTIONS_SCENE:
            currentScene = menuScene
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                currentScene = menuScene
        else:
            changed = False

    if changed:
        screen.fill([0,0,0])
        currentScene.render(screen, events)
        pygame.display.flip()

