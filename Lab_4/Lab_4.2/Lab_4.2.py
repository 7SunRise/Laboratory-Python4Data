import sys
from moviepy.editor import VideoFileClip

# В папке output находятся кадры при использовании параметров: "small-cat-angry-cat.mp4 0 7 output 2"

path_to_read = sys.argv[1] # путь к входному видеофайлу (параметр 1)
begin = sys.argv[2] # время начала выделяемого файла в секундах (параметр 2)
end = sys.argv[3] # время конца выделяемого файла в секундах (параметр 3)
path_to_write = sys.argv[4] # путь к папке, куда нужно записывать извлеченные кадры (параметр 4)
if len(sys.argv) == 6: # если шаг извлечения кадров указан, то берем указанный шаг (параметр 5)
	step = int(sys.argv[5])
else: # если шаг извлечения кадров не был указан, присваиваем стандартный шаг равный 10 кадрам
	step = 10

videofile = VideoFileClip(path_to_read) 
videofile = videofile.resize(width=250) # ставим 250 пикселей по горизонтали
number_of_frames = 1 # порядковый номер взятого кадра
time = int(begin) # время начала выделенного фрагмента 
time_end = int(end) # время конца выделенного фрагмента
while time < time_end:
	videofile.save_frame(path_to_write + "\\" + str(number_of_frames) + ".jpg", time) # сохраняем кадр на секундке "time" по заданному пути
	time += step # прибавляем шаг для получения времени следующего кадра
	number_of_frames += 1 # увеличиваем порядковый номер кадра
videofile.close()