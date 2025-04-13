# Напишите класс Balance для описания весов с двумя чашами. На левую и правую чашу объекта будут
# добавляться грузы с различным весом, ваша задача определить положение чаш.
# Метод add_right принимает целое число — вес, положенный на правую чашу весов, add_left — на
# левую чашу. Метод result должен возвращать символ =, если вес на чашах одинаковый, R — если
# перевесила правая, L — если перевесила левая.



class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_left(self, weight):
        self.left += weight  

    def add_right(self, weight):
        self.right += weight 

    def result(self):
        if self.left == self.right:
            return "=" 
        elif self.left > self.right:
            return "L"  
        else:
            return "R"  


balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result()) # L