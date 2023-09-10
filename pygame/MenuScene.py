import pygame
import pygame_menu
from Scene import Scene
from events import *

class MenuScene(Scene):
    menu: pygame_menu.Menu

    def __init__(self, screen: pygame.Surface):
        SCREEN_WIDTH = screen.get_width()
        SCREEN_HEIGHT = screen.get_height()
        self.menu  = self.start_menu(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)

    def start_menu(self, w: int, h: int) -> pygame_menu.Menu:
        menu: pygame_menu.Menu = pygame_menu.Menu(\
            'Tactics STS', w, h, theme=pygame_menu.themes.THEME_BLUE)

        def new_game():
            pygame.event.post(pygame.event.Event(NEW_GAME_SCENE))

        def quit():
            exit()

        def options():
            pygame.event.post(pygame.event.Event(OPTIONS_SCENE))

        menu.add.button('New Game', new_game)
        menu.add.button('Options', options)
        menu.add.button('Quit', quit)
        menu.center_content()

        return menu

    def render(self, screen: pygame.Surface, events: list[pygame.event.Event]):
        if self.menu.is_enabled():
            self.menu.update(events)
            self.menu.draw(screen)

