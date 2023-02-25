import sqlite3

connection = sqlite3.connect('basetemp.sl3', 5)
cursor = connection.cursor()

cursor.execute("INSERT INTO temperature(temperature, date_and_time) VALUES ('+2', '24.02.23:17.00');")

connection.commit()
connection.close()
