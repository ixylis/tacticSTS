import pygame
from HexGrid import HexGrid, HexLocation
from Entity import Entity, Player, Enemy
import math

class LevelScene:
    grid: HexGrid
    player: Player
    screen: pygame.Surface

    def __init__(self):
        self.grid = HexGrid(3, 3)
        startingLocation = HexLocation(0, 0, 0)
        self.player = Player(startingLocation, self.grid)
        
    def render(self, screen: pygame.Surface):
        self.screen = screen
        SCREEN_WIDTH = screen.get_width()
        SCREEN_HEIGHT = screen.get_height()
        size = 70
        q, r = self.grid.get_dimensions()
        cX = SCREEN_WIDTH/2
        cY = size
        hD = 3*size/2
        vD = math.sqrt(3)*size/2
        for i in range(q):
            for j in range(r):
                center = (cX+(hD*i)-(hD*j), cY+(vD*i)+(vD*j))
                self.draw_hexagon(center, size)
                if self.grid.entities[i][j]:
                    pygame.draw.circle(screen, (0, 255, 0), center, size/2)
    def draw_hexagon(self, center, size):
        centerX = center[0]
        centerY = center[1]
        corners = []
        color = (255, 255, 255)
        for i in range(6):
            angle_deg = i*60
            angle_rad = math.pi / 180 * angle_deg
            corners.append((centerX+size*math.cos(angle_rad), centerY+size*math.sin(angle_rad)))
        pygame.draw.polygon(self.screen, color, corners)
        pygame.draw.polygon(self.screen, (255, 0, 0), corners, 5)
    

