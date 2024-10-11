from pathlib import Path
from skimage import transform, exposure, util, io
import sys
from glob import glob
from random import randrange, uniform


# Первый аргумент - это путь к папке с данными. Второй и последующие - это аугментации, которые нужно применить к каждой фотографии. Обязательно должна быть хотя бы одна аугментация
# В ПАПКЕ train ПОЯВИЛИСЬ ИЗОБРАЖЕНИЯ, ПОЛУЧЕННЫЕ ПРИ ИСПОЛЬЗОВАНИИ АУГМЕНТАЦИЙ -gamma И -noise

def add_zeros(value): # эта функция нужна для того, чтобы измененные изображения сохранялись с именем, состоящим из 4 цифр, т.е. при необходимости добавлять нули к началу 
	additional_zeros = 4
	while value >= 1:
		value = value / 10
		additional_zeros = additional_zeros - 1
	return additional_zeros

all_augmentation = [] # список применяемых аугментаций
path = sys.argv[1] # путь к папке с фотографиями
for i in range(2, len(sys.argv)):
	all_augmentation.append(sys.argv[i])
files = [file for file in Path(path).glob('*.jpg')] # считываем все файлы расширения jpg из папки
images = io.imread_collection(files) 
count = len(images) # подсчитываем количество подходящих файлов/изображений
for image in images:
	if '-resize' in all_augmentation:
		image = transform.resize(image, (500,500)) # делает изображение размером 500х500
	if '-rotate' in all_augmentation:
		image = transform.rotate(image, randrange(90, 360, 90)) # осуществляет поворот на 90, 180,270, 360 случайным образом
	if "-gamma" in all_augmentation:
		image = exposure.adjust_gamma(image, uniform(0.2, 2)) # меняет яркость случайным образом
	if "-ïnvert" in all_augmentation:
		image = util.invert(image) # меняет цвета на противоположные
	if "-noise" in all_augmentation:
		image = util.random_noise(image) # добавляет случайный шум

	io.imsave(path + "\\" + "0" * add_zeros(count) + str(count) + ".jpg", util.img_as_ubyte(image)) # сохраянем аугментированные изображения в ту же папку
	count = count + 1 # добавляем 1 для того, чтобы не было файлов с одинаковыми числовыми значениями в имени
	
