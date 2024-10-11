from PIL import Image
from sys import argv

# Определение самого используемого цвета заключается в том, что мы суммируем значение red, green, blue в каждом отдельном пикселе.
# Наибольшее значение будет самым используемым цветом.

filename = argv[1]
with Image.open(filename) as img:
	all_pixels_data = img.getdata() # получаем данные со всех пикселей
	red, green, blue = 0, 0, 0
	for pixel_data in all_pixels_data: # рассматриваем каждый пиксель и суммируем значения
		red += pixel_data[0]
		green += pixel_data[1]
		blue += pixel_data[2]
	if max(red, green, blue) == red:
		print("Красный самый используемый на данном изображении")
	elif max(red, green, blue) == green:
		print("Зеленый самый используемый на данном изображении")
	elif max(red, green, blue) == blue:
		print("Синий самый используемый на данном изображении")
