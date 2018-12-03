class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, multiplier):
        if isinstance(multiplier, (int, float)):
            return Vector(self.x * multiplier, self.y * multiplier)
        elif isinstance(multiplier, Vector):
            return self.x * multiplier.x + self.y * multiplier.y
        else:
            raise Exception("Wrong argument")

    def __str__(self):
        return "<%s, %s>" % (self.x, self.y)
