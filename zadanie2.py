# Напишите класс Balance для описания весов с двумя чашами. На левую и правую чашу объекта будут
# добавляться грузы с различным весом, ваша задача определить положение чаш.
# Метод add_right принимает целое число — вес, положенный на правую чашу весов, add_left — на
# левую чашу. Метод result должен возвращать символ =, если вес на чашах одинаковый, R — если
# перевесила правая, L — если перевесила левая.



class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_left(self, weight):
        self.left_weight += weight  # добавляем к левой чаше

    def add_right(self, weight):
        self.right_weight += weight  # добавляем к правой чаше

    def result(self):
        if self.left_weight == self.right_weight:
            return "="  # веса равны
        elif self.left_weight > self.right_weight:
            return "L"  # левая тяжелее
        else:
            return "R"  # правая тяжелее
