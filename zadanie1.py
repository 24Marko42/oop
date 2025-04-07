# Напишите класс BigBell, который при вызове метода sound печатает попеременно слова ding и dong,
# начиная c ding.

class BigBell:
    f = 0
    def sound(self):
        if not self.f :
            print('ding')
            self.f = 1
        else:
            print('dong')
            self.f = 0

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()