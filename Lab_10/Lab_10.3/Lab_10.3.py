from docx import Document

document = Document("Word_1.docx") # открываем файл из первого задания

table = document.tables[0] # берем первую (единственную в нашем случае) таюлицу из файла
data = {}
for row in range(1, 4):
    nameOfCharacteristic = table.cell(row, 0).text[1:] # выводим название характеристики
    characteristic = table.cell(row, 2).text[1:] # выводим значение характеристики
    data[nameOfCharacteristic] = characteristic 
print("Данные по ATmega328:")
print(data) # выводим результат