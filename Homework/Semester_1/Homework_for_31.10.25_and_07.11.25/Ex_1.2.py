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

def area(v1, v2, v3):
    a = abs(v1 - v2)
    b = abs(v1 - v3)
    c = abs(v2 - v3)
    return 0.25 * ((a + b + c) * (a + b - c)* (b + c - a) * (a + c - b)) ** 0.5

def trian_area(a):
    max_trian_area = 0
    for i in range(len(a)):
        print(max_trian_area)
        for j in range(len(a)):
            print(max_trian_area)
            for k in range(len(a)):
                print(max_trian_area)
                if area(a[i], a[j], a[k]) > max_trian_area: max_trian_area = area(a[i], a[j], a[k])
    return max_trian_area

X = list(map(float, input().split()))
Y = list(map(float, input().split()))
Z = list(map(float, input().split()))

points = [f"{{{X[i]}, {Y[i]}, {Z[i]}}}" for i in range(len(X))]
Vector_points = [Vector(points[i]) for i in range(len(points))]

print(trian_area(Vector_points))