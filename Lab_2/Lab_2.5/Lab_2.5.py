from PIL import Image
from pathlib import Path
from glob import glob
import os
import sys

# Первый аргумент это путь к папке. Второй аргумент - тип файла. Другая последовательность не предусмотрена. Путь к папке может быть не указан.

if sys.argv[1] == '--ftype': # если путь к папке не указан
	path = Path.cwd()
	type = sys.argv[2]
else: # если путь указан
	path = Path(sys.argv[1])
	type = sys.argv[3]
for file in path.glob('*.' + str(type)): # ищем все файлы из папки с данным нам расширением
	with Image.open(str(path) + "\\" + file.name) as img:
		img.thumbnail((50,50)) # делаем из каждого подходящего файла его эскиз
		img.show()