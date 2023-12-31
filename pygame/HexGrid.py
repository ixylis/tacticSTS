from __future__ import annotations
from typing import Optional, Self, TYPE_CHECKING
if TYPE_CHECKING:
    from Entity import Entity


class HexLocation:
    q: int
    r: int
    s: int

    def __init__(self, q: int, r: int, s: int):
        self.q = q
        self.r = r
        self.s = s

    def distance(self, loc: Self):
        return min(abs(self.q-loc.q), abs(self.r-loc.r), abs(self.s-loc.s))


class HexGrid:
    q_dim: int
    r_dim: int
    entities: list[list[Optional[Entity]]]

    def __init__(self, q_dim: int, r_dim: int):
        self.entities = [[None for r in range(r_dim)] for q in range(q_dim)]
        self.q_dim = q_dim
        self.r_dim = r_dim

    def setLocation(self, loc:HexLocation, entity: Optional[Entity]):
        self.entities[loc.q][loc.r] = entity
    
    def get_dimensions(self):
        return (self.q_dim, self.r_dim)
    
    def placeEntity(self, entity: Entity, loc: HexLocation):
        assert self.validLocation(loc)
        entity.setGrid(self)
        entity.setLocation(loc)
        self.setLocation(loc, entity)

    def validLocation(self, loc: HexLocation):
        return loc.q >= 0 and loc.q < self.q_dim and loc.r >= 0 and loc.r < self.r_dim
