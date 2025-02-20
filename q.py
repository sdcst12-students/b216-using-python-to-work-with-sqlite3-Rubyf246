#!python3

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "select * from npc where level <5 limit 5;"
cursor.execute(query)
result = cursor.fetchall()

print(result[1])
for i in result:
    id = i[0]
    strength = i[1]
    intelligence = i[2]
    print(f"Character with ID {id} has stergnth of {strength}")
print(result)