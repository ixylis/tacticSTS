import pygame
from HexGrid import HexGrid, HexLocation
import abc

class Entity(pygame.sprite.Sprite):
    loc: HexLocation
    grid: HexGrid
    def __init__(self, loc: HexLocation, grid: HexGrid):
        super(Entity, self).__init__()
        self.loc = loc
        self.grid = grid

    def setLocation(self, loc: HexLocation):
        self.loc = loc
    def move_to(self, loc: HexLocation):
        self.setLocation(loc)
        self.grid.updateLocations(self)

class Player(Entity):
    surf: pygame.Surface
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
    def get_rect(self):
        return (0, 0)

class Enemy(Entity):
    surf: pygame.Surface
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 0))
    def get_rect(self):
        return (50, 50)
