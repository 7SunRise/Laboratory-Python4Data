import openpyxl
from openpyxl import Workbook

wb = Workbook() # создаем пустую таблицу Excel
sheet = wb.active # выбираем в ней активный (т.е. первый) лист

# Основные данные вносимые в таблицу (другие данные будут вычисляться из этих данных)
data = [
        [
            { 'Таб. номер': '0002', 'ФИО': 'Петров П.П.', 'Отдел': 'Бухгалтерия', 'Сумма по окладу, руб.': 3913.04, 'Сумма по надбавкам, руб.': 2608.70 },
            { 'Таб. номер': '0005', 'ФИО': 'Васин В. В.', 'Отдел': 'Бухгалтерия', 'Сумма по окладу, руб.': 5934.78, 'Сумма по надбавкам, руб.': 913.04 }
        ],
        [
            { 'Таб. номер': '0001', 'ФИО': 'Иванов И.И.', 'Отдел': 'Отдел кадров', 'Сумма по окладу, руб.': 6000.00, 'Сумма по надбавкам, руб.': 4000.00 },
            { 'Таб. номер': '0003', 'ФИО': 'Сидоров С.С.', 'Отдел': 'Отдел кадров', 'Сумма по окладу, руб.': 5000.00, 'Сумма по надбавкам, руб.': 4500.00 },
            { 'Таб. номер': '0006', 'ФИО': 'Львов Л.Л.', 'Отдел': 'Отдел кадров', 'Сумма по окладу, руб.': 4074.07, 'Сумма по надбавкам, руб.': 2444.44 },
            { 'Таб. номер': '0007', 'ФИО': 'Волков В.В.', 'Отдел': 'Отдел кадров', 'Сумма по окладу, руб.': 1434.78, 'Сумма по надбавкам, руб.': 1434.78 },
        ],
        [
            { 'Таб. номер': '0004', 'ФИО': 'Мишин М.М.', 'Отдел': 'Столовая', 'Сумма по окладу, руб.': 5500.00, 'Сумма по надбавкам, руб.': 3500.00 }
        ]
] 
columns = ["Таб. номер", "ФИО", "Отдел", "Сумма по окладу, руб.", "Сумма по надбавкам, руб.", "Сумма зарплаты, руб.", "НДФЛ, %", "Сумма НДФЛ, %", "Сумма к выдаче, руб."] # заголовки колонок
sheet.append(columns) # добавляем колонки в пустую таблицу
allTotal1, allTotal2, allTotal3, allTotal4, allTotal5 = 0, 0, 0, 0, 0 #общий итог по сумме по окладам, надбавкам, зарплатам, сумме НДФЛ и сумме к выдаче соответственно
for department in data: # проходимся по всем отделам поочередно
    nameOfDepartment, total1, total2, total3, total4, total5 = "", 0, 0, 0, 0, 0 # название отдела и итоги для данного отдела
    for worker in department: # проходимя по сотрудникам отдела
        nameOfDepartment = worker['Отдел']  # название отдела
        # используем функцию round() для того, чтобы дробная часть суммы правильно считалась
        worker['Сумма по окладу, руб.'] = round(worker['Сумма по окладу, руб.'], 2) # округляем
        worker['Сумма по надбавкам, руб.'] = round(worker['Сумма по надбавкам, руб.'], 2) # округляем
        worker['Сумма зарплаты, руб.'] = round(worker['Сумма по окладу, руб.'] + worker['Сумма по надбавкам, руб.'], 2) # считаем сумму зарплаты
        worker['НДФЛ, %'] = 13 # фиксированный процент НДФЛ
        worker['Сумма НДФЛ, %'] = round(worker['Сумма зарплаты, руб.'] * worker['НДФЛ, %'] / 100, 2) # считаем сумму НДФЛ
        worker['Сумма к выдаче, руб.'] = round(worker['Сумма зарплаты, руб.'] - worker['Сумма НДФЛ, %'], 2) # считаем сумму к выдаче
        total1 += worker['Сумма по окладу, руб.'] # добавляем к итоговой сумме по окладу для отдела
        total2 += worker['Сумма по надбавкам, руб.'] # добавляем к итоговой сумме по надбавкам для отдела
        total3 += worker['Сумма зарплаты, руб.'] # добавляем к итоговй сумме по зарплатам для отдела
        total4 += worker['Сумма НДФЛ, %'] # добавляем к итоговой сумме по НДФЛ для отдела
        total5 += worker['Сумма к выдаче, руб.'] # добавляем к итоговой сумме к выдаче для отдела 
        row = list(worker.values()) # значения соответствующих колонок для сотрудника
        sheet.append(row) # добавляем сотрудника в таблицу
    allTotal1 += total1; allTotal2 += total2; allTotal3 += total3; allTotal4 += total4; allTotal5 += total5 # добавляем значения к общему итогу
    sheet.append(["", "", nameOfDepartment + " Итог", total1, total2, total3, "", total4, total5]) # добавляем строку итогов для каждого из отделов
sheet.append(["", "", "Общий итог", allTotal1, allTotal2, allTotal3, "", allTotal4, allTotal5]) # добавляем строку общего итога
wb.save("spreadsheet1.xlsx") # сохраняем таблицу