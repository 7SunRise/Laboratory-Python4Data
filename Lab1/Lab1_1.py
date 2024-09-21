import sys                          # для получения аргументов из консоли
from pathlib import Path            # для получения пути
import os                           # для оценки размера файда
from glob import glob               # для получения списка файлов
import shutil                       # для копирования


if len(sys.argv) == 1:  
    path = Path.cwd()   # если путь к папке не передан, берем папку в которой находимся
else:
    path = sys.argv[1]  # если передан, берем этот путь
path = Path(path)


less_than_2KB = [file for file in path.glob('*') if os.path.getsize(file) < 2048]   # список со всеми файлами меньших 2KB

    
if len(less_than_2KB) > 0:      # проверяем наличие подходящих файлов
    for i in less_than_2KB:
        print(i.name)           # пишем названия файлов в консоли
    Path("small").mkdir(parents=True, exist_ok=True)
    for i in range(len(less_than_2KB)):
        shutil.copy(less_than_2KB[i],"small") # копируем в созданную нами папку (папку small создавал в папке, в которой находится программа)
else:       # если подходящих файлов нет
    print("Файлов меньших 2KB нет в данной папке и папка small не создана")
