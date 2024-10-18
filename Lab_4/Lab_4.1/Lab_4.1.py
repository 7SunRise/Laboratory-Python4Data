from moviepy.editor import VideoFileClip
import sys

path = sys.argv[1] # путь к видеофайлу (параметр 1)
begin = sys.argv[2] # время начала вырезаемого файла в секундах (параметр 2)
end = sys.argv[3] # время конца вырезаемого файла в секундах(параметр 3)
name = sys.argv[4] # названия видеофайла, который был вырезан из оригинального видеофайла (параметр 4)

videofile = VideoFileClip(path)
result_videofile = videofile.subclip(begin, end)
result_videofile.write_videofile(str(name))
videofile.close()