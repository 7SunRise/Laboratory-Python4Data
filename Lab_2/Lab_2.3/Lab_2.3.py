from PIL import Image, ImageFilter, ImageOps

filename = "BeautifulPicture.jpg" # Исходная картинка
mark = "Watermark.jpg" # Будущий водяной знак
with Image.open(mark) as img_mark:
	with Image.open(filename) as img:
		img_mark = img_mark.convert("L") # Переводим водяной знак в черно-белый
		threshold = 130 # граница, чтобы выделить текст и изображение для нашего водянго знака из всего изображения
		img_mark = img_mark.point(lambda x: 255 if x > threshold else 0) # выделяем текст и изображение
		img_mark = img_mark.filter(ImageFilter.CONTOUR) # выделяем контур
		img_mark = img_mark.point(lambda x: 0 if x == 255 else 255) # меняем черный и белый цвета местами
		img_mark = img_mark.filter(ImageFilter.BLUR) # делаем более прозрачным
		img_mark = ImageOps.crop(img_mark, 5) # убираем рамку у водяного знака
		img_mark = img_mark.resize((830, 761)) # расширяем водяной знак на все изображение
		img.paste(img_mark, (0, 0), img_mark) # сливаем два изображения вместе
		img.show()
		img.save("Final_Image.jpg")