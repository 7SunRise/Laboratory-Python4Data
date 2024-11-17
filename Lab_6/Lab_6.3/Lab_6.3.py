import xml.etree.ElementTree as ET

file = input(str()) # файл, в котором нужно вывести товар
tree = ET.parse(file) # парсим xml файл
root = tree.getroot()
for item in root.findall("Документ/ТаблСчФакт/СведТов"): # выводим нужные значения товаров
	print(" Товар:", item.get("НаимТов"), " Количество:", item.get("КолТов"), " Цена:", item.get("ЦенаТов"))