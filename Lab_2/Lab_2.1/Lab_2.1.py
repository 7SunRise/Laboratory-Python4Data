from PIL import Image

def tile(*images, vertical=False): # для создания одного изображения, содержащего оригинал и разные каналы
	width, height = images[0].width, images[0].height
	tiled_size = ((width, height * len(images))) if vertical else (width * len(images), height)
	tiled_img = Image.new(images[0].mode, tiled_size)
	row, col = 0, 0
	for image in images:
		tiled_img.paste(image, (row, col))
		if vertical:
			col += height
		else:
			row += width
	return tiled_img

filename = "BeautifulPicture.jpg" # исходное изображение, из которого берутся разные каналы
with Image.open(filename) as img:
	red, green, blue = img.split() # разделяем на каналы исходное изображение
	zeroed_band = red.point(lambda _: 0)
	red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band)) # красный канал
	green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band)) # зеленый канал
	blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue)) # синий канал
	final_img = tile(img, red_merge, green_merge, blue_merge) # создаем итоговое изображение
	final_img.save("Final_Image.jpg")
	final_img.show()
