# Создайте класс А, в котором определены:
# 1. метод приведения к строке, возвращающий 'A._str_method'
# 2. метод hello(), выводящий на экран строку "Hello'
# Создайте класс В, в котором определены:
# 1. метод приведения к строке, возвращающий 'В.＿str＿method"
# 2. метод good_evening(), выводящий на экран строку 'Good evening'
# Создайте класс С, унаследованный от А и В, который при приведении к строке использует метод класса А 
# (сам класс С не должен содержать методов ＿str＿ или _repr_).
# Создайте класс D, унаследованный от А и В, который при приведении к строке использует метод класса В 
# (сам класс D не должен содержать методов ＿str＿ или _repr_).


class A:
    def __str__(self):
        return 'A._str_method'

    def hello(self):
        print("Hello")


class B:
    def __str__(self):
        return 'B._str_method'

    def good_evening(self):
        print("Good evening")

class C(A, B):
    pass

class D(B, A):
    pass

c = C()
c. hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(c)
print(d)