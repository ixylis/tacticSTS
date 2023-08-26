from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from Entity import Entity
    from Action import Action

class TurnQueue:
    turns: list[Turn]

    def __init__(self):
        self.turns = []

    def addTurn(self, entity: Entity, action: Optional[Action]):
        self.turns.append(Turn(entity, action))

    def setAction(self, turnIdx: int, action: Action):
        assert turnIdx >= 0
        assert turnIdx < len(self.turns)
        self.turns[turnIdx].setAction(action)

    def deleteAction(self, turnIdx: int):
        assert turnIdx >= 0
        assert turnIdx < len(self.turns)
        self.turns[turnIdx].deleteAction()

    def applyNext(self):
        assert len(turns) > 0
        assert turns[0].action
        self.turns[0].apply()
        self.turns = self.turns[1:]

    def swapTurns(self, ia: int, ib: int):
        assert ia >= 0
        assert ia < len(self.turns)
        assert ib >= 0
        assert ib < len(self.turns)

        ta = self.turns[ia]
        self.turns[ia] = self.turns[ib]
        self.turns[ib] = ta


class Turn:
    entity: Entity
    action: Optional[Action]

    def __init__(self, entity: Entity, action: Optional[Action]):
        self.entity = entity
        self.action = action

    def setAction(self, action: Action):
        self.action = action

    def deleteAction(self):
        self.action = None

    def apply(self) -> bool:
        assert self.action
        return self.action.apply(self.entity)