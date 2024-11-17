import xml.etree.ElementTree as ET

file = input(str()) # файл, в который вносятся изменения
tree = ET.parse(file) # парсим файл
root = tree.getroot()
new_item = ET.Element("Item") # создаем новый Item
elements_of_item = ["ArtName", "Barcode", "QNT", "QNTPack", "Unit", "SN1", "SN2", "QNTRows"] # подэлементы нового Item
data_for_new_element = ["Сыр Чеддер", "2000000000120", "230,3", "230,3", "шт", "00000015", "31.01.2021", "20"] # данные, которые будут записаны в соответствующие подэлементы Item
for i in range(0, len(elements_of_item)): # вносим данные
	ET.SubElement(new_item, elements_of_item[i]).text = data_for_new_element[i]
root.find("Detail").append(new_item) # добавляем Item в xml файл
ET.indent(tree, "    ") # добавляем отступ для нового Item
summ, summrows = 0, 0 # пересчитываем значения SumM и SummRows
for item in root.findall("Detail/Item"):
	summ += float(item.find("QNT").text.replace(",", "."))
	summrows += int(item.find("QNTRows").text)
root.find("Summary/Summ").text = str(summ).replace(".", ",")
root.find("Summary/SummRows").text = str(summrows)
tree.write("new.xml", encoding="UTF-8", xml_declaration=True) # создаем переделанный файл
