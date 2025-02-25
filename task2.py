#!python

"""
Create a query to create a table to store pets information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (dog, cat)
pet breed (collie, beagle, persian, etc)
pet age
pet gender
pet neutered or spayed
owner ID

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            species         breed           age  gender     spayed/neutered?    ownerID
Fluffy          dog             Pomeraniam      5    m          true                101
Benjamin        cat             Siberian        8    m          true                103
Casey           cat             Siberian        8    m          true                103
Friend          cat             Domestic        4    m          false               102
Copper          dog             Beagle          12   m          true                104
"""


import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "select sqlite_version();"
query = """create table veterinarian 
( 
id integer primary key autoincrement, 
name tinytext, 
species tinytext,
breed tinytext, 
age int,
s/n tinytext,
id int); """

data = [
('Fluffy', 'dog', 'Pomeraniam', 5, 'm', 'true', 101),
('Benjamin', 'cat', 'Siberian', 8, 'm', 'true', 103), 
('Casey', 'cat', 'Siberian', 8, 'm', 'true', 103 ),
('Friend', 'cat', 'Domestic', 4, 'm', 'false', 102),
('Copper', 'dog', 'Beagle', 12, 'm', 'true', 104)
]
for i in data:
    query = f"insert into veterinarian (name, species, breed, age, s/n, id) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]});"

connection.commit()
query = "select * from veterinarian"
cursor.execute(query)
result = cursor.fetchall()

for i in result:
    print(i)
