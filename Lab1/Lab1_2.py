import sys                          
from pathlib import Path                                     
from glob import glob
import os


files_not_in_dir = list() # список отсутствующих файлов
files_in_dir = list()  # список имеющихся в папке файлов


if sys.argv[3] == '--files':  # если dirpath и files указаны
    path = Path(sys.argv[2])
    i = 4 # аргумент, с которого начинаются названия файлов
    while len(sys.argv[i]) > 1 and i < len(sys.argv) - 1: # добавление всех файлов в список на проверку
        files_not_in_dir.append(sys.argv[i])
        i += 1
    files_not_in_dir.append(sys.argv[i]) # добавляем последний файл, т.к в while он не попадает

    
elif sys.argv[1] == '--files':     # если указан только files
    path = Path.cwd()
    i = 2  # аргумент, с которого начинаются названия файлов
    while len(sys.argv[i]) > 1 and i < len(sys.argv) - 1: # добавление всех файлов в список на проверку
        files_not_in_dir.append(sys.argv[i])
        i += 1
    files_not_in_dir.append(sys.argv[i]) # добавляем последний файл, т.к. в while он не попадает

    
elif sys.argv[1] == '--dirpath':    # если указан только dirpath
    path = Path(sys.argv[1])

    
else:                               # если ничего не указано
    path = Path.cwd()


if len(files_not_in_dir) > 0: # если files были указаны
    for file in path.glob('*'):
        if file.name in files_not_in_dir: # если совпадают, переносим из первоначального списка в список имеющихся файлов
            files_in_dir.append(file.name)
            files_not_in_dir.remove(file.name)


    print('Файлы, присутствующие в папке:', files_in_dir) # выводим в коносоль имеющиеся файлы
    print('Файлы, отсутствующие в папке:', files_not_in_dir) # выводим в консоль отсутствующие файлы


    In_Dir_File = open("InDir.txt","w+") # добавляем имеющиеся файлы в соответствующий файл
    for i in files_in_dir:
        In_Dir_File.write(i + '\n')
    In_Dir_File.close()


    Out_Dir_File = open("OutDir.txt","w+") # добавляем отсутствующие файлы в соответствующий файл
    for i in files_not_in_dir:
        Out_Dir_File.write(i + '\n')
    Out_Dir_File.close()

    
else:           # если files не были указаны
    size = 0    # обьем файлов в байтах
    amount = 0  # количество файлов
    files = list(path.glob('*'))
    for file in files:
        amount += 1
        size += os.path.getsize(file)
    print('Количество файлов:', amount)
    print('Обьем файлов в байтах:', size)
