from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from HexGrid import HexGrid, HexLocation
import pygame

class Entity(pygame.sprite.Sprite):
    loc: HexLocation
    grid: HexGrid

    def __init__(self, loc: HexLocation, grid: HexGrid):
        super(Entity, self).__init__()
        self.grid = grid
        self.loc = loc
        self.grid.placeEntity(self, loc)

    def setLocation(self, loc: HexLocation):
        self.loc = loc
    
    def getLocation(self):
        return self.loc
    
    def setGrid(self, grid: HexGrid):
        self.grid = grid
    
    def getGrid(self):
        return self.grid

    def move_to(self, loc: HexLocation):
        self.setLocation(loc)
        self.grid.setLocation(loc, self)

class Player(Entity):
    surf: pygame.Surface
    
    def __init__(self, loc: HexLocation, grid: HexGrid):
        super(Player, self).__init__(loc, grid)
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
    
    def get_surf(self):
        return self.surf
    
    def get_rect(self):
        return (0, 0)

class Enemy(Entity):
    surf: pygame.Surface
    
    def __init__(self, loc: HexLocation, grid: HexGrid):
        super(Enemy, self).__init__(loc, grid)
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 0))
    
    def get_surf(self):
        return self.surf
    
    def get_rect(self):
        return (50, 50)
