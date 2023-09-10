import pygame
from abc import ABC, abstractmethod

class Scene(ABC):

    @abstractmethod
    def render(self, screen: pygame.Surface, events: list[pygame.event.Event]):
        pass