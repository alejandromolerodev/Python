import sqlite3
import pandas as pd


conn = sqlite3.connect('empresa.db')


#Consultar tablas de la base de datos
query = "SELECT name FROM sqlite_master WHERE type='table';"
df = pd.read_sql_query(query, conn)
print(df)


#Consultar el nombre de los empleados
#query = "SELECT nombre FROM empleados;"
#df = pd.read_sql_query(query, conn)
#print(df)


#Consultar que empleados trabajan en Recursos Humanos
#query = "SELECT nombre FROM empleados WHERE departamento = 'Recursos Humanos';"
#df = pd.read_sql_query(query, conn)
#print(df)

