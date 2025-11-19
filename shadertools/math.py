class Vec2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y


class Vec3(Vec2):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        super().__init__(x, y)
        self.z = z
