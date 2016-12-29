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

aa = "hello"
bb = "bye"
cursor = conn.cursor()
cursor.execute("INSERT INTO Authentication VALUES (NULL, ?, ? )", (aa,bb));
conn.commit()
print("Table created successfully")
conn.close()