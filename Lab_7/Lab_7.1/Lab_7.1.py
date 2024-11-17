from jsonschema import validate
import json

print("Введите файл на проверку:")
file = input(str()) # вводим путь к файлу для проверки
print("Введите схему:")
schema = input(str()) # вводим схему для проверки
with open(file) as json_file, open(schema) as schema:
	try:
		validate(json.load(json_file), json.load(schema)) # проверим на правильность
		print("Все в норме")
	except:
		print("Что-то не так")
