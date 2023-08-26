import abc
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Entity import Entity


"""
Actions are applied to the entities doing the actions through the apply method.

Actions are things like "attack for 1" or "move for 1"
"""
class Action(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apply(self, entity: Entity) -> bool:
        pass


class AndAction(Action):
    a1: Action
    a2: Action

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def apply(self, entity: Entity) -> bool:
        return self.a1.apply(entity) and self.a2.apply(entity)


class OrAction(Action):
    a1: Action
    a2: Action

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def apply(self, entity: Entity) -> bool:
        return self.a1.apply(entity) or self.a2.apply(entity)