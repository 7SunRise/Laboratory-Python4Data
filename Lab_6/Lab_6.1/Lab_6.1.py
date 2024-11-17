from xmlschema import XMLSchema

file = input(str()) # файл, которому требуется проверка (пишется имя файла и его расширение; т.е. например: ex_1.xml)
schema = XMLSchema('schema.xsd') # схема, показывающая как должен выглядеть xml файл
if schema.is_valid(file): # проверяем файл на правильность 
	print("Все в норме")
else:
	print("Что-то не так")