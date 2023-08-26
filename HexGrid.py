from typing import Self
from Entity import Entity, Nothing


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


class Hex:
	loc: HexLocation
	entity: Entity

	def __init__(self, loc: HexLocation, entity: Entity = Nothing()):
		self.loc = loc
		self.entity = entity


class HexGrid:
	hexes: list[list[Hex]]

	def __init__(self, q_dim: int, r_dim: int):
		hexes = [[Hex(HexLocation(q, r, 0-q-r)) for r in range(r_dim)] for q in range(q_dim)]