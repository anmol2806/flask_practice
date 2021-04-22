import sqlite3
conn = sqlite3.connect('employee.db')
print ("Opened database successfully")
conn.execute('CREATE TABLE Student1 (	"Name"	TEXT,	"address"	TEXT,	"email"	TEXT,	"id"	INTEGER NOT NULL UNIQUE,PRIMARY KEY("id" AUTOINCREMENT));')
print ("Table created successfully")
conn.close()