import pygame
from pygame.locals import *
from Entity import Entity, Player, Enemy
from HexGrid import HexGrid, HexLocation
import math
pygame.init()
screen = pygame.display.set_mode([1000, 1000])
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

all_sprites = pygame.sprite.Group()

def draw_hexagon(surf: pygame.Surface, center: (float, float), size):
    centerX = center[0]
    centerY = center[1]
    corners = []
    color = (255, 255, 255)
    for i in range(6):
        angle_deg = i*60
        angle_rad = math.pi / 180 * angle_deg
        corners.append((centerX+size*math.cos(angle_rad), centerY+size*math.sin(angle_rad)))
    pygame.draw.polygon(surf, color, corners)
    pygame.draw.polygon(surf, (255, 0, 0), corners, 5)

def draw_grid(grid: HexGrid):
    surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    size = 70
    q, r = grid.get_dimensions()
    cX = SCREEN_WIDTH/2
    cY = size
    hD = 3*size/2
    vD = math.sqrt(3)*size/2

    for i in range(q):
        for j in range(r):
            center = (cX+(hD*i)-(hD*j), cY+(vD*i)+(vD*j))
            draw_hexagon(surf, center, size)
    return surf

hexGrid = HexGrid(3, 3)
hexGridSurface = draw_grid(hexGrid)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    screen.blit(hexGridSurface, (0,0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()

