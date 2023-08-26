class Entity:
    loc: HexLocation
    def __init__(self, loc: HexLocation):
        self.loc = loc
    def move_to(self, loc: HexLocation):
        self.loc = loc

class Player(Entity):
    pass

class Enemy(Entity):
    pass
