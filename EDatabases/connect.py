import sqlite3

conn = sqlite3.connect('empresa.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    salario REAL NOT NULL,
    departamento TEXT NOT NULL
)
''')

conn.commit()
conn.close()