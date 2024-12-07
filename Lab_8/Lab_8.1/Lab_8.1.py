import sqlite3 as sqlite

conn = sqlite.connect("deliveryOrder.db") # создаем обьект connection и создаем новый файл deliveryOrder.db
cur = conn.cursor() # создаем обьект cursor для того, чтобы делать SQL-запросы к базе
cur.execute("""
			CREATE TABLE IF NOT EXISTS courier(
			id INT PRIMARY KEY,
			surname TEXT,
			name TEXT,
			secondName TEXT,
			passportNumber TEXT,
			dateOfBirth TEXT,
			dateOfEmployment TEXT,
			clockInTime TEXT,
			clockOutTime TEXT,
			city TEXT,
			street TEXT,
			houseNumber TEXT,
			apartmentNumber TEXT,
			phoneNumber TEXT
			);
			""") # создаем таблицу курьеров
conn.commit() # сохраняем изменения для обьекта соединения
cur.execute("""
			CREATE TABLE IF NOT EXISTS transport(
			number INT PRIMARY KEY,
			carBrand TEXT,
			dateOfRegistration TEXT,
			colour TEXT
			);
			""") # создаем таблицу транспорта курьеров
conn.commit() # сохраняем изменения для обьекта соединения
cur.execute("""
			INSERT INTO courier(id, surname, name, secondName, passportNumber, dateOfBirth, dateOfEmployment,clockInTime, clockOutTime, city, street, houseNumber, apartmentNumber, phoneNumber)
			VALUES("1", "Ivanov", "Ivan", "Ivanovich","000000","11.11.2000", "05.10.2024", "8:00", "15:00", "Vladivostok", "Glavnaya", "5", "14", "88005553535");
			""") # создаем новую запись в таблице курьеров
conn.commit() # сохраняем изменения для обьекта соединения
cur.execute("""
			INSERT INTO transport(number, carBrand, dateOfRegistration, colour)
			VALUES("A000AA", "Subaru", "12.12.2022", "white");
			""") # создаем новую запись в таблице транспорта курьеров
conn.commit() # сохраняем изменения для обьекта соединения
cur.execute("""
			UPDATE transport SET colour = "black" WHERE carBrand = "Subaru";
			""")  # заменяем значение некоторых полей у определенных записей в таблице транспорта курьеров
conn.commit() # сохраняем изменения для обьекта соединения
conn.close() # закрываем соединение