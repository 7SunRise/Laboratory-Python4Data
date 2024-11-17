import json

file = input(str()) # файл, из которого извлекается телефонная книга
with open(file) as file:
	data = json.load(file) # загружаем данные из json файла
	phone_book = {}
	for user in data["employees"]:
		phone_book[user["name"]] = [user["phoneNumber"]] # добавляем телефонные номера по ключу (т.е. по имени)
	print(phone_book) # выводим итоговую книгу