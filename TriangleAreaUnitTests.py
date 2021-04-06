# Тесты модуля TriangleAreaUnit
# НУЛЕВЫЕ КООРДИНАТЫ
# 0 0 0 0 0 0
# ValueError Exception
# ПРОИЗВОЛЬНЫЙ ТРЕУГОЛЬНИК
# 0 0 3 5 8 0
# area = 20
# ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК
# 0 0 0 6 7 0
# area = 21
# РАВНОБЕДРЕННЫЙ ТРЕУГОЛЬНИК
# 0 0 5 3 10 0
# area = 15
# РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК
# 0 0 0.5 0.867 1 0
# area = 0.4335

import math
import unittest

import TriangleAreaUnit as Calc  # тестируемый модуль


class TestCalc(unittest.TestCase):
    # нулевые координаты
    def test_get_area_exception(self):
        p1 = Calc.Point(0, 0)
        p2 = Calc.Point(0, 0)
        p3 = Calc.Point(0, 0)
        triangle = Calc.Triangle(p1, p2, p3)
        with self.assertRaises(ValueError):
            triangle.get_area()
            
    # произвольный треугольник
    def test_get_area(self):
        p1 = Calc.Point(0, 0)
        p2 = Calc.Point(3, 5)
        p3 = Calc.Point(8, 0)
        triangle = Calc.Triangle(p1, p2, p3)
        # self.assertEqual(triangle.get_square(), 20)
        assert math.isclose(triangle.get_area(), 20, abs_tol=0.0001)

    # прямоугольный треугольник
    def test_get_area_rectangular(self):
        p1 = Calc.Point(0, 0)
        p2 = Calc.Point(0, 6)
        p3 = Calc.Point(7, 0)
        triangle = Calc.Triangle(p1, p2, p3)
        # self.assertEqual(triangle.get_square(), 21)
        assert math.isclose(triangle.get_area(), 21, abs_tol=0.0001)

    # равнобедренный треугольник
    def test_get_area_isosceles(self):
        p1 = Calc.Point(0, 0)
        p2 = Calc.Point(5, 3)
        p3 = Calc.Point(10, 0)
        triangle = Calc.Triangle(p1, p2, p3)
        # self.assertEqual(triangle.get_square(), 15)
        assert math.isclose(triangle.get_area(), 15, abs_tol=0.0001)

    # равносторонний треугольник
    def test_get_area_equilateral(self):
        p1 = Calc.Point(0, 0)
        p2 = Calc.Point(0.5, 0.867)
        p3 = Calc.Point(1, 0)
        triangle = Calc.Triangle(p1, p2, p3)
        # self.assertEqual(triangle.get_square(), 0.4335)
        assert math.isclose(triangle.get_area(), 0.4335, abs_tol=0.00001)


if __name__ == "__main__":
    unittest.main()
