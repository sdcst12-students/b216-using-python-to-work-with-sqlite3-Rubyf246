"""
Create a query to create a table to store game information for a league of Provincial/Territory teams
Each entry should list:

id unique integer identifier
home team name
away team name
home team score
away team score

choose appropriate variable types for each field
add the data in the dictionary to your table
"""
scores = {'home': 'NU', 'homeScore': 2, 'away': 'NS', 'awayScore': 2}, {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 2}, {'home': 'NU', 'homeScore': 1, 'away': 'YT', 'awayScore': 3}, {'home': 'NT', 'homeScore': 3, 'away': 'ON', 'awayScore': 1}, {'home': 'NU', 'homeScore': 2, 'away': 'ON', 'awayScore': 1}, {'home': 'BC', 'homeScore': 0, 'away': 'SK', 'awayScore': 3}, {'home': 'SK', 'homeScore': 2, 'away': 'NU', 'awayScore': 0}, {'home': 'MN', 'homeScore': 1, 'away': 'NS', 'awayScore': 3}, {'home': 'ON', 'homeScore': 0, 'away': 'AB', 'awayScore': 1}, {'home': 'MN', 'homeScore': 3, 'away': 'NU', 'awayScore': 2}, {'home': 'NB', 'homeScore': 0, 'away': 'NL', 'awayScore': 1}, {'home': 'BC', 'homeScore': 3, 'away': 'NT', 'awayScore': 2}, {'home': 'ON', 'homeScore': 1, 'away': 'NU', 'awayScore': 3}, {'home': 'NS', 'homeScore': 1, 'away': 'ON', 'awayScore': 1}, {'home': 'NL', 'homeScore': 3, 'away': 'BC', 'awayScore': 1}, {'home': 'NL', 'homeScore': 2, 'away': 'NT', 'awayScore': 1}, {'home': 'NU', 'homeScore': 2, 'away': 'AB', 'awayScore': 3}, {'home': 'MN', 'homeScore': 1, 'away': 'YT', 'awayScore': 1}, {'home': 'BC', 'homeScore': 1, 'away': 'PE', 'awayScore': 0}, {'home': 'QC', 'homeScore': 1, 'away': 'NL', 'awayScore': 0}, {'home': 'NL', 'homeScore': 1, 'away': 'NT', 'awayScore': 3}, {'home': 'BC', 'homeScore': 1, 'away': 'ON', 'awayScore': 0}, {'home': 'SK', 'homeScore': 0, 'away': 'AB', 'awayScore': 1}, {'home': 'YT', 'homeScore': 2, 'away': 'QC', 'awayScore': 2}, {'home': 'NT', 'homeScore': 2, 'away': 'NU', 'awayScore': 3}, {'home': 'NB', 'homeScore': 2, 'away': 'NT', 'awayScore': 2}, {'home': 'PE', 'homeScore': 2, 'away': 'BC', 'awayScore': 0}, {'home': 'PE', 'homeScore': 2, 'away': 'NB', 'awayScore': 0}, {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 0}, {'home': 'NB', 'homeScore': 3, 'away': 'MN', 'awayScore': 2}, {'home': 'AB', 'homeScore': 0, 'away': 'NL', 'awayScore': 2}, {'home': 'QC', 'homeScore': 2, 'away': 'NL', 'awayScore': 1}, {'home': 'SK', 'homeScore': 0, 'away': 'MN', 'awayScore': 0}, {'home': 'QC', 'homeScore': 2, 'away': 'BC', 'awayScore': 3}, {'home': 'NU', 'homeScore': 2, 'away': 'AB', 'awayScore': 2}, {'home': 'NS', 'homeScore': 3, 'away': 'AB', 'awayScore': 3}, {'home': 'QC', 'homeScore': 1, 'away': 'NT', 'awayScore': 1}, {'home': 'SK', 'homeScore': 3, 'away': 'AB', 'awayScore': 0}, {'home': 'NL', 'homeScore': 3, 'away': 'QC', 'awayScore': 1}, {'home': 'NL', 'homeScore': 2, 'away': 'SK', 'awayScore': 1}, {'home': 'YT', 'homeScore': 1, 'away': 'BC', 'awayScore': 3}, {'home': 'NL', 'homeScore': 2, 'away': 'PE', 'awayScore': 2}, {'home': 'YT', 'homeScore': 1, 'away': 'NL', 'awayScore': 1}, {'home': 'NS', 'homeScore': 0, 'away': 'QC', 'awayScore': 1}, {'home': 'BC', 'homeScore': 1, 'away': 'NB', 'awayScore': 3}, {'home': 'NL', 'homeScore': 3, 'away': 'NU', 'awayScore': 1}, {'home': 'QC', 'homeScore': 0, 'away': 'SK', 'awayScore': 0}, {'home': 'NS', 'homeScore': 0, 'away': 'SK', 'awayScore': 0}, {'home': 'AB', 'homeScore': 1, 'away': 'NT', 'awayScore': 2}, {'home': 'YT', 'homeScore': 2, 'away': 'QC', 'awayScore': 2}, {'home': 'YT', 'homeScore': 1, 'away': 'NB', 'awayScore': 3}, {'home': 'NT', 'homeScore': 0, 'away': 'QC', 'awayScore': 2}, {'home': 'ON', 'homeScore': 2, 'away': 'BC', 'awayScore': 2}, {'home': 'BC', 'homeScore': 0, 'away': 'ON', 'awayScore': 1}, {'home': 'MN', 'homeScore': 1, 'away': 'ON', 'awayScore': 3}, {'home': 'SK', 'homeScore': 2, 'away': 'NU', 'awayScore': 1}, {'home': 'MN', 'homeScore': 3, 'away': 'PE', 'awayScore': 1}, {'home': 'NU', 'homeScore': 2, 'away': 'YT', 'awayScore': 3}, {'home': 'AB', 'homeScore': 0, 'away': 'NT', 'awayScore': 0}
print(scores)

#import sqlite3
#
#file = 'dbase.db'
#connection = sqlite3.connect(file)
#print(connection)
#
#cursor = connection.cursor()
#query = "select sqlite_version();"
#
#query = "drop table if exists scores"
#cursor.execute(query)
#
#query = """create table scores
#( 
#id integer primary key autoincrement, 
#homeTeam tinytext,
#awayTeam tinytext,
#homeTeamScore int,
#awayTeamScore int);
#"""
#cursor.execute(query)
#
#data = [
('NU', 'NS', 2, 2),
('PE', 'YT', 0, 2),
('NU', 'YT', 1, 3),
('NT', 'ON', 3, 1),
('NU', 'ON', 2, 1),
('BC', 'SK', 0, 3),
('SK', 'NU', 2, 0),
('MN', 'NS', 1, 3),
('ON', 'AB', 0, 1),
('MN', 'NU', 3, 2),
('NB', 'NL', 0, 1),
('BC', 'NT', 3, 2),
('ON', 'NU', 1, 3),
('NS', 'ON', 1, 1),
('NL', 'BC', 3, 1),
('NL', 'NT', 2, 1),
('NU', 'AB', 2, 3),
('MN', 'YT', 1, 1),
('BC', 'PE', 1, 0),
('QC', 'NL', 1, 0),
('NL', 'NT', 1, 3),
('BC', 'ON', 1, 0),
('SK', 'AB', 0, 1),
('YT', 'QC', 2, 2),
('NT', 'NU', 2, 3),
('NB', 'NT', 2, 2),
('PE', 'BC', 2, 0),
('PE', 'NB', 2, 0),
('PE', 'YT', 0, 0),
('NB', 'MN', 3, 2),
('AB', 'NL', 0, 2),
('QC', 'NL', 2, 1),
('SK', 'MN', 0, 0),
('QC', 'BC', 2, 3),
('NU', 'AB', 2, 2),
('NS', 'AB', 3, 3),
('QC', 'NT', 1, 1),
('SK', 'AB', 3, 0),
('NL', 'QC', 3, 1),
('NL', 'SK', 2, 1),
('YT', 'BC', 1, 3),
('NL', 'PE', 2, 2),
('YT', 'NL', 1, 1),
('NS', 'QC', 0, 1),
('BC', 'NB', 1, 3),
('NL', 'NU', 3, 1),
('QC', 'SK', 0, 0),
('NS', 'SK', 0, 0),
('AB', 'NT', 1, 2),
('YT', 'QC', 2, 2),
('YT', 'NB', 1, 3),
('NT', 'QC', 0, 2),
('ON', 'BC', 2, 2),
('BC', 'ON', 0, 1),
('MN', 'ON', 1, 3),
('SK', 'NU', 2, 1),
('MN', 'PE', 3, 1),
('NU', 'YT', 2, 3),
('AB', 'NT', 0, 0)
]
#for i in data:
#    query = f"insert into scores (homeTeam, awayTeam, homeTeamScore, awayTeamScore) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}');"
#    cursor.execute(query)
#
#query = "select * from scores"
#cursor.execute(query)
#connection.commit()
#
#result = cursor.fetchall()
#
#for i in result:
#    print(i)
# 
##print (result)