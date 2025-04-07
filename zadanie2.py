# Определите класс Point. При инициализации экземпляру передаются координаты x и y.
# При сравнении двух экземпляров оператор == должен возвращать True, если координаты точек равны, и False — если нет.
# При сравнении оператором != должно возвращаться True, если координаты точек не равны, и False — если равны.


class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
p1 = Point(1, 2)
p2 = Point(5, 6)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")