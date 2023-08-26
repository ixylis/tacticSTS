class Entity:
	def isNothing(self):
		return False


class Nothing(Entity):
	def isNothing(self):
		return True