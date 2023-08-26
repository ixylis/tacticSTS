import pygame
from pygame.locals import *

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
        self.q = 0
        self.r = 0
        self.s = 0
    def move_to(self, coordinates: tuple):

class Player(Character):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = (0, 0)

class Enemy(Character):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 0))
        self.rect = (10, 10)


pygame.init()
screen = pygame.display.set_mode([1000, 1000])
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
enemy1 = Enemy()
all_sprites.add(enemy1)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()

