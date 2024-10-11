from PIL import Image, ImageDraw

for i in range(1,4):
	image = Image.new("RGB",(100,100)) # создаем новую картинку размером 100х100
	draw = ImageDraw.Draw(image)
	draw.rectangle([0,0,100,100], outline=(0, 0, 255), width=5, fill=(255,255,255)) # рисуем синюю рамку размером 5px
	draw.text((33,15), str(i), font_size=60, fill=(255,0,0)) # добавляем цифры на картинки
	image.save(str(i) + "_image.jpg")
	image.show()