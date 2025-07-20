import sqlite3

connection=sqlite3.connect("students.db")

cursor=connection.cursor()


TABLE_INFO='''
CREATE TABLE students (NAME varchar(30), CLASS varchar(20), Section varchar(25), marks int);'''

cursor.execute(TABLE_INFO)

cursor.execute("INSERT INTO students (name, class, section, marks) VALUES ('John Doe', '10', 'A', 85)")
cursor.execute("INSERT INTO students (name, class, section, marks) VALUES ('Priya Sharma', '9', 'B', 91)")
cursor.execute("INSERT INTO students (name, class, section, marks) VALUES ('Amit Patel', '10', 'C', 78)")
cursor.execute("INSERT INTO students (name, class, section, marks) VALUES ('Sneha Mehta', '8', 'A', 88)")
cursor.execute("INSERT INTO students (name, class, section, marks) VALUES ('Ravi Verma', '9', 'C', 82)")

data=cursor.execute('''select * from students;''')

print("the inserted records are")

for row in data:
    print(row)

connection.commit()
connection.close()
