
# №17 (2 балла)
# Вам нужно написать программу для планирования выступлений на конференциях. Её
# функциональность должна быть следующей: можно создавать выступление, задавать его тему,
# время его начала и длительность.
# Программа должна следить за тем, чтобы доклады не перекрывались во времени и предупреждать
# пользователя, если это произошло, выводить суммарное время доклада, время самого
# продолжительного перерыва между докладами и так далее.
# Надо реализовать два класса: «доклад» и «конференция». Как распределить между ними
# функциональность, решать Вам. Программа должна иметь хороший интерфейс с подсказками, что нужно вводить.


class Talk:
    def __init__(self, title: str, start_time_str: str, duration: int):
        self.title = title
        self.start_minutes = self._time_str_to_minutes(start_time_str)
        self.duration = duration
        self.end_minutes = self.start_minutes + self.duration

    def _time_str_to_minutes(self, time_str: str) -> int:
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes

    def _minutes_to_time_str(self, minutes: int) -> str:
        return f"{minutes // 60:02d}:{minutes % 60:02d}"

    def __str__(self):
        start = self._minutes_to_time_str(self.start_minutes)
        end = self._minutes_to_time_str(self.end_minutes)
        return f"{self.title} ({start} - {end})"

class Conference:
    def __init__(self):
        self.talks = []

    def add_talk(self, talk: Talk):
        for existing in self.talks:
            if self._overlaps(talk, existing):
                print(f"⚠️ Пересечение с докладом: '{existing.title}'")
                return
        self.talks.append(talk)
        print(f"✅ Доклад '{talk.title}' добавлен")

    def _overlaps(self, t1: Talk, t2: Talk) -> bool:
        return t1.start_minutes < t2.end_minutes and t2.start_minutes < t1.end_minutes

    def show_schedule(self):
        print("\n📅 Расписание:")
        for talk in sorted(self.talks, key=lambda t: t.start_minutes):
            print(f"  - {talk}")

    def total_talk_time(self):
        total = sum(talk.duration for talk in self.talks)
        print(f"\n🕓 Общее время докладов: {total} минут")

    def longest_break(self):
        if len(self.talks) < 2:
            print("\nℹ️ Недостаточно докладов для перерывов.")
            return

        sorted_talks = sorted(self.talks, key=lambda t: t.start_minutes)
        max_break = 0

        for i in range(1, len(sorted_talks)):
            gap = sorted_talks[i].start_minutes - sorted_talks[i-1].end_minutes
            if gap > max_break:
                max_break = gap

        print(f"\n🛋️ Самый длинный перерыв между докладами: {max_break} минут")

def main():
    conf = Conference()
    print("🔧 Планировщик конференции")
    
    while True:
        title = input("\nВведите тему доклада (или 'выход'): ")
        if title.lower() == 'выход':
            break

        start = input("Время начала (чч:мм): ")
        duration = int(input("Длительность (в минутах): "))
        
        talk = Talk(title, start, duration)
        conf.add_talk(talk)

    conf.show_schedule()
    conf.total_talk_time()
    conf.longest_break()

if __name__ == "__main__":
    main()

