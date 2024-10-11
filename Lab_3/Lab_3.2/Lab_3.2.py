from skimage import color, exposure, io
from PIL import Image
import matplotlib.pyplot as plt
import sys

path = sys.argv[1] # путь к изображению
all_colors_brightness = []
all_brightness = []
with Image.open(path) as img:
	all_colors_brightness = img.histogram() # возвращает 768 элементов, где каждый элемент - это количество пикселей определенной яркости и цвета.
							 # Т.е. первые 256 элементов - это количество пикселей разной яркости красного цвета. Потом идут 256 аналогичных для зеленых и 256 для синих
for i in range(0,256):
	all_brightness.append(all_colors_brightness[i] + all_colors_brightness[i + 256] + all_colors_brightness[i + 512]) # используем для вывода гистограммы нашего изображения
img = io.imread(path)
for_color_histogram = exposure.histogram(img, channel_axis=2) # используем для вывода гистограммы отдельных цветов

original_img = plt.subplot2grid((4,2), (0,0), rowspan=4) # создаем "таблицу", состоящую из 4 строк и 2 столбцов. Помещаем исходное изображение в 1 столбце
original_img.imshow(img) # вставляем исходное изображение
original_img.axis("off") # убираем координатные оси для исходного изображения

hist = plt.subplot2grid((4,2),(0,1)) # помещаем в 2 столбец, 1 строку общую гистограмму изображения
hist.stairs(all_brightness, fill=True, color=(0,0,0)) # вставляем гистограмму

red = plt.subplot2grid((4,2), (1,1)) # помещаем в 2 столбец, 2 строку гистограмму для красного цвета
red.stairs(for_color_histogram[0][0], fill=True, color=(1,0,0)) # вставляем гистограмму

green = plt.subplot2grid((4,2), (2,1)) # помещаем в 2 столбец, 3 строку гистограмму для зеленого цвета
green.stairs(for_color_histogram[0][1], fill=True, color=(0,1,0)) # вставляем гистограмму

blue = plt.subplot2grid((4,2), (3,1)) # помещаем в 2 столбец, 4 строку гистограмму для синего цвета
blue.stairs(for_color_histogram[0][2], fill=True, color=(0,0,1)) # вставляем гистограмму

plt.show() # отображаем полученную таблицу



