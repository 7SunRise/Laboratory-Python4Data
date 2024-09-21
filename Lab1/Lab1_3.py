import sys                          
from pathlib import Path                                                 


if len(sys.argv) == 1: # если путь к папке не указан
    path = Path.cwd()
else:                  # если путь к папке указан
    path = Path(sys.argv[1])


with open('OutDir.txt','r') as file: # открываем файл с отсутствующими файлами
    lines = file.readlines() # считываем эти файлы
    for name in lines:
        new_file = open(str(path) + '\\' + str(name[:-1]), "w+") # поочередно создаем их в папке
