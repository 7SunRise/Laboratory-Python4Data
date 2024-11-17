import json

# Я так понял, что total это общая цена всех товаров. Из за этого пришлось поменять total первого invoice.
print("Введите файл, в который будут вноситься изменения")
old_file = input(str()) # документ до внесения в него нового предмета
print("Введите файл, в который будут записываться данные (можно в тот же файл)")
new_file = input(str()) # документ, в который вносится новый элемент
with open(old_file, "r") as file, open(new_file, "w") as new:
	data = json.load(file) # загружаем исходные данные
	new_invoice = {"id":3, "total":0.0, "items":[]} # создаем новый invoice
	new_item1 = {"name":"new item 1", "quantity":1, "price":100.0} # создаем предметы, которые будем добавлять в invoice
	new_item2 = {"name":"new item 2", "quantity":2, "price":150.0} # создаем предметы, которые будем добавлять в invoice
	new_invoice["items"].append(new_item1) # добавляем предметы в созданный invoice
	new_invoice["items"].append(new_item2) # добавляем предметы в созданный invoice
	for new_item in new_invoice["items"]:
		new_invoice["total"] += new_item["price"] * new_item["quantity"] # пересчитываем total
	data["invoices"].append(new_invoice) # добавляем новый invoice в наши данные
	json.dump(data, new, indent=2) # загружаем данные в файл