# Unit для расчета площади треугольника по координатам трёх точек
# Площадь рассчитывается по координатам X/Y трёх точек
# Поддержка прямоугольных треугольников
# Поддержка равнобедренных треугольников
# Поддержка равносторонних треугольников
# Поддержка произвольных треугольников

# ФОРМУЛЫ
# |AB| = math.sqrt((x2 − x1) ** 2 + (y2 − y1) ** 2)
# |BC| = math.sqrt((x3 − x2) ** 2 + (y3 − y2) ** 2)
# |AC| = math.sqrt((x3 − x1) ** 2 + (y3 − y1) ** 2)
# Полупериметр p = (AB + BC + AC) / 2
# Площадь area = math.sqrt(p*(p-AB)*(p-BC)*(p-AC))

import math


class Point:
    """"Used to create a point based on coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    """"Used to create a triangle based on points and calculate its area"""
    def __init__(self, point_1, point_2, point_3):
        self.ab = self.get_side(point_1, point_2)
        self.bc = self.get_side(point_2, point_3)
        self.ac = self.get_side(point_1, point_3)

    """"Create a triangle"""
    @staticmethod
    def create_from_input():
        x1, y1, x2, y2, x3, y3 = list(map(int, input("Enter coordinates of 3 points (x1 y1 x2 y2 x3 y3)\n").split()))
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)
        return Triangle(p1, p2, p3)

    """"Calculate the sides of a triangle"""
    @staticmethod
    def get_side(p1, p2):
        side = math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        if side != 0:
            return side
        else:
            raise ValueError("Side of a triangle cannot be 0")

    """"Calculate the area of a triangle"""
    def get_area(self):
        p = (self.ab + self.bc + self.ac) / 2
        print("Half-perimeter of a triangle = ", p)

        area = math.sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ac))
        print("Area of a triangle = ", area)

        return area


if __name__ == "__main__":
    triangle = Triangle.create_from_input()
    triangle.get_area()
