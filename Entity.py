import pygame
from HexGrid import HexGrid, HexLocation

class Entity(pygame.sprite.Sprite):
    loc: HexLocation
    grid: HexGrid
    def __init__(self, loc: HexLocation, grid: HexGrid):
        super(Entity, self).__init__()
        self.loc = loc
        self.grid = grid

    def move_to(self, loc: HexLocation):
        self.loc = loc

class Player(Entity):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = (0, 0)

class Enemy(Entity):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = (50, 50)
