# Напишите класс Selector. Экземпляр этого класса при инициализации получает список чисел. Вызов
# метода get_odds возвращает нечётные числа из первоначального списка, вызов get_evens —
# чётные.
# Числа должны идти в том же порядке, в котором они были в изначальном списке.


class Selector:
    def __init__(self, numbers):
        self.numbers = numbers  # сохраняем список чисел

    def get_odds(self):
        return [num for num in self.numbers if num % 2 == 1]

    def get_evens(self):
        return [num for num in self.numbers if num % 2 == 0]
