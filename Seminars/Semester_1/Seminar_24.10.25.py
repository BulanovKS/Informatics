class Complex:
    def __init__(self, re = 0, im = 0):
        self.re = re
        self.im = im
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)
    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)
    def __str__(self):
        return f"{self.re} + {self.im}i"
    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5
c1 = Complex(re = 1, im = 2)
c2 = Complex(re = 2, im = 3)
print(c1)
print(c1 + c2, " ", c1 * c2)
print(abs(c1))