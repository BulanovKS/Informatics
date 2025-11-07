class Vector():
    def __init__(self, stroke):
        stroke = stroke.replace("{", "").replace("}", "").replace(",","")
        self.x, self.y, self.z = map(float, stroke.split())

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Vector(f"{{{self.x + other.x}, {self.y + other.y}, {self.z + other.z}}}")
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(f"{{{self.x + other}, {self.y + other}, {self.z + other}}}")
        else:
            return None

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(f"{{{self.x + other.x}, {self.y + other.y}, {self.z + other.z}}}")
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(f"{{{self.x + other}, {self.y + other}, {self.z + other}}}")
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(f"{{{self.x - other.x}, {self.y - other.y}, {self.z - other.z}}}")
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(f"{{{self.x - other}, {self.y - other}, {self.z - other}}}")
        else:
            return None

    def __rsub__(self, other):
        if isinstance(other, Vector):
            return Vector(f"{{{other.x - self.x}, {other.y - self.y}, {other.z - self.z}}}")
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(f"{{{other - self.x}, {other - self.y}, {other - self.z}}}")
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(f"{{{self.x * other.x}, {self.y * other.y}, {self.z * other.z}}}")
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(f"{{{self.x * other}, {self.y * other}, {self.z * other}}}")
        else:
            return None

    def __rmul__(self, other):
        if isinstance(other, Vector):
            return Vector(f"{{{self.x * other.x}, {self.y * other.y}, {self.z * other.z}}}")
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(f"{{{self.x * other}, {self.y * other}, {self.z * other}}}")
        else:
            return None

    def __str__(self):
        return f'{{{self.x}, {self.y}, {self.z}}}'

v1 = Vector("{2.56, 5, 6.0}")
print(v1)