# Нужно написать программу для имитации работы файловой системы.
# Она должна выполнять следующие команды
# 1. Создать директорию с указанным именем. Должно быть возможным создание вложенных диреторий, то есть, 
# "aaа", "aaa/bbb", "aаа/ссс", "aaа/bbb/ccс". Причём "aaа/ссс", "aaа/bbb/cсс" - это разные диретории.
# 2. Вывести список файлов и поддиректорий в директории с указанным именем.
# 3. Записать строку в файл с указанным именем. При первой записи файл создаётся. 
# При последующих перезаписывается содержимое файла. Файлы "1.txt", "aaа/1.txt". "aaa/bbb/1.txt" разные, 
# так как находятся в разных директориях.
# 4. Прочесть содержимое ранее созданного файла.
# Имена файлов и директорий указываются относительно общей корневой директории. 
# В качестве разделителя между компонентами пути в файловой системе удобнее всего использовать символ "/".
# Старайтесь проектировать программу так, чтобы у вас не было общего списка или словаря всех файлов в файловой системе, 
# и директории хранили свои поддиректории и файлы, как в настоящих файловых системах.
# так же напиши код на питоне, добавь комментарии, пиши так, будто ты студент, 
# который изучает данный язык программирования, не используй дополнительные библиотеки


# Класс файл
class File:
    def __init__(self, name):
        self.name = name
        self.content = ""  # содержимое файла

# Класс директория
class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}  # словарь: имя -> Directory
        self.files = {}           # словарь: имя -> File

# Класс файловая система
class FileSystem:
    def __init__(self):
        self.root = Directory("/")  # корневая директория

    # Вспомогательная функция: находит директорию по пути
    def traverse(self, path):
        parts = [p for p in path.strip("/").split("/") if p]
        current = self.root
        for part in parts:
            if part not in current.subdirectories:
                return None
            current = current.subdirectories[part]
        return current

    # Вспомогательная: создать путь, включая промежуточные папки
    def _create_path(self, path):
        parts = [p for p in path.strip("/").split("/") if p]
        current = self.root
        for part in parts:
            if part not in current.subdirectories:
                current.subdirectories[part] = Directory(part)
            current = current.subdirectories[part]
        return current

    # Команда 1: создать директорию (включая вложенные)
    def create_directory(self, path):
        self._create_path(path)
        print(f" Директория '{path}' создана.")

    # Команда 2: вывести содержимое директории
    def list_directory(self, path):
        dir_obj = self._traverse(path)
        if dir_obj is None:
            print(f" Директория '{path}' не найдена.")
            return
        print(f"\n Содержимое директории '{path}':")
        print("Папки:")
        for name in dir_obj.subdirectories:
            print("  ", name)
        print("Файлы:")
        for name in dir_obj.files:
            print("  ", name)

    # Команда 3: записать в файл (создать или перезаписать)
    def write_file(self, path, content):
        parts = path.strip("/").split("/")
        file_name = parts[-1]
        dir_path = "/".join(parts[:-1])

        dir_obj = self._create_path(dir_path)  # создаём путь, если не существует

        if file_name not in dir_obj.files:
            dir_obj.files[file_name] = File(file_name)

        dir_obj.files[file_name].content = content
        print(f" Файл '{path}' записан.")

    # Команда 4: прочитать содержимое файла
    def read_file(self, path):
        parts = path.strip("/").split("/")
        file_name = parts[-1]
        dir_path = "/".join(parts[:-1])

        dir_obj = self._traverse(dir_path)
        if dir_obj is None or file_name not in dir_obj.files:
            print(f" Файл '{path}' не найден.")
            return

        print(f"\n Содержимое файла '{path}':")
        print(dir_obj.files[file_name].content)



def main():
    fs = FileSystem()

    while True:
        print("\nДоступные команды:")
        print("1. mkdir <путь> — создать директорию")
        print("2. ls <путь> — показать содержимое директории")
        print("3. write <путь_к_файлу> — записать в файл")
        print("4. read <путь_к_файлу> — прочитать файл")
        print("5. exit — выход\n")

        command = input("Введите команду: ").strip()
        if command == "exit":
            break

        parts = command.split(maxsplit=1)
        if not parts:
            continue

        cmd = parts[0]

        if cmd == "mkdir" and len(parts) > 1:
            fs.create_directory(parts[1])
        elif cmd == "ls" and len(parts) > 1:
            fs.list_directory(parts[1])
        elif cmd == "write" and len(parts) > 1:
            path = parts[1]
            content = input("Введите содержимое файла: ")
            fs.write_file(path, content)
        elif cmd == "read" and len(parts) > 1:
            fs.read_file(parts[1])
        else:
            print(" Неизвестная команда или отсутствует путь.")

if __name__ == "__main__":
    main()
