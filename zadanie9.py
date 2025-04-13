# Создайте класс Triangle, представляющий треугольник.
# Конструктор этого класса должен принимать на вход 3 числа (длины сторон треугольника).
# Также у этого класса должен быть метод perimeter(), возвращающий периметр.
# Отнаследуйте от класса Triangle класс EquilateralTriangle, представляющий равносторонний треугольник.
# Переопределите конструктор этого класса с использованием конструктора базового класса.
# Конструктор класса EquilateralTriangle должен принимать на вход 1 число (длину стороны).


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c
    
class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

    def perimeter(self):
        return super().perimeter()
    

Triangle1 = Triangle(1, 4, 5)
print(Triangle1.perimeter())
Triangle2 = EquilateralTriangle(2)
print(Triangle2.perimeter())