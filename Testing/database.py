import sqlite3

conn= sqlite3.connect('booksrecommender.db')

print("Opened database successfully")

#conn.execute("DROP TABLE Authentication;")

# conn.execute('''CREATE TABLE User
#             (ID INT PRIMARY KEY NOT NULL,
#             Name    TEXT    NOT NULL,
#             Preferences TEXT    NULL);''')

# conn.execute('''CREATE TABLE Authentication
#             (UserID INTEGER PRIMARY KEY   AUTOINCREMENT,
#             UserName    TEXT    NOT NULL,
#             Password TEXT    NOT NULL);''')

aa = "chitra"
cursor = conn.cursor()
for row in aa:
    cursor.execute("SELECT UserID FROM Authentication WHERE UserName = ?", (aa,))
    data = cursor.fetchall()
if len(data) == 0:
    print("No username available you need to sign up!")
else:
    print("Welcome")

print("Table created successfully")
conn.close()