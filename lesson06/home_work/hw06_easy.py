# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math


class Figure:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def side(p1, p2):
        return math.sqrt((p2['x'] - p1['x']) ** 2 + (p2['y'] - p1['y']) ** 2)


class Triangle(Figure):
    def __init__(self, a, b, c):
        Figure.__init__(self, 'Triangle')
        self.a = a
        self.b = b
        self.c = c
        self.a = Figure.side(a, b)
        self.b = Figure.side(b, c)
        self.c = Figure.side(c, a)

    @staticmethod
    def height(a, b, c):
        p = (a + b + c) / 2
        return (math.sqrt(p * (p - a) * (p - b) * (p - c)) / 2) * 2

    @staticmethod
    def side(p1, p2):
        return math.sqrt((p2['x'] - p1['x']) ** 2 + (p2['y'] - p1['y']) ** 2)

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        return (self.a * Triangle.height(self.a, self.b, self.c)) / 2


a = {'x': -2, 'y': 0}
b = {'x': 2, 'y': 0}
c = {'x': 0, 'y': 3}
print('*********************************')
tri = Triangle(a, b, c)
print(tri.type)
print('Area: ', tri.area)
print('Perimeter: ', tri.perimeter)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid(Figure):
    def __init__(self, a, b, c, d):
        Figure.__init__(self, 'Trapezoid')
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = Figure.side(a, b)
        self.bc = Figure.side(b, c)
        self.cd = Figure.side(c, d)
        self.da = Figure.side(d, a)

    @staticmethod
    def side(p1, p2):
        return math.sqrt((p2['x'] - p1['x']) ** 2 + (p2['y'] - p1['y']) ** 2)

    @property
    def equals(self):
        if self.ab == self.cd:
            return self.bc, self.da, self.ab
        elif self.bc == self.da:
            return self.ab, self.cd, self.bc
        else:
            return False

    @property
    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    @property
    def area(self):
        a = self.equals[0]
        b = self.equals[1]
        c = self.equals[2]
        return (a + b) / 4 * math.sqrt(4 * c ** 2 - (a - b) ** 2)


aa = {'x': -2, 'y': 0}
bb = {'x': -1, 'y': 2}
cc = {'x': 1, 'y': 2}
dd = {'x': 2, 'y': 0}
print('*********************************')
tra = Trapezoid(aa, bb, cc, dd)
print(tra.type)
print('Area: ', tra.perimeter)
print('Perimeter: ', tra.area)
