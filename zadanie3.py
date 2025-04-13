# Напишите класс Selector. Экземпляр этого класса при инициализации получает список чисел. Вызов
# метода get_odds возвращает нечётные числа из первоначального списка, вызов get_evens —
# чётные. Числа должны идти в том же порядке, в котором они были в изначальном списке.


class Selector:
    def __init__(self, numbers):
        self.numbers = numbers 

    def get_odds(self):
        return [num for num in self.numbers if num % 2 == 1]

    def get_evens(self):
        result = []
        for num in self.numbers:
            if num % 2 == 0:
                result.append(num)
        return result


values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))