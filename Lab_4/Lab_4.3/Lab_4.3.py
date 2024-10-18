import cv2
from pathlib import Path
import sys

path = sys.argv[1] # путь к воспроизводимому файлу
file = cv2.VideoCapture(path)
font = cv2.FONT_HERSHEY_SIMPLEX # выбираем шрифт
coordinates1 = (0,50) # координаты нижнего левого угла строки первого текста
coordinates2 = (0, 100) # координаты нижнего левого угла строки второго текста
font_scale = 1 # множитель шрифта относительно базового размера шрифта
color_text = (255, 255, 255) # цвет текста (в моем случае - белый)
text1 = str(Path(path).name) # первый текст, т.е. название видеофайла
text2 = "FPS: " + str(int(file.get(cv2.CAP_PROP_FPS))) # второй текст, т.е. количество FPS

while file.isOpened():
	ret, video = file.read() # ret - показатель того, что не возникло ошибок при чтении
	if ret:
		video = cv2.putText(video, text1, coordinates1, font, font_scale, color_text) # добавляем первый текст
		video = cv2.putText(video, text2, coordinates2, font, font_scale, color_text) # добавляем второй текст
		cv2.imshow(text1, video)
		cv2.waitKey(int(1000 // int(file.get(cv2.CAP_PROP_FPS)))) # сколько миллисекнуд будет отображаться каждый кадр до его закрытия и показа следующего (здесь значение +- как у оригинального видео)
	else:
		break
file.release()
cv2.destroyAllWindows()