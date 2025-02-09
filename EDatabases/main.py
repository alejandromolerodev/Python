import sqlite3
import pandas as pd
import os

# Conectar a la base de datos SQLite
conn = sqlite3.connect('empresa.db')
c = conn.cursor()

# Definir la ruta del archivo CSV
file = "../datas/empleados.csv"

# Inicializar 'data' como None
data = ""

# Cargar el archivo CSV si existe
if os.path.exists(file):
    data = pd.read_csv(file)
    print(data)

    # Inserción de datos en la tabla 'empleados'
    for index, row in data.iterrows():
        query = """
        INSERT INTO empleados (id, nombre, edad, salario, departamento)
        VALUES (?, ?, ?, ?, ?)
        """
        c.execute(
            query,
            (
                row["id"],
                row["nombre"],
                row["edad"],
                row["salario"],
                row["departamento"],
            ),
        )

    # Confirmar cambios en la base de datos
    conn.commit()

    print("Datos introducidos correctamente")

    # Recuperar y mostrar los datos de la tabla empleados
    df = pd.read_sql_query("SELECT * FROM empleados", conn)
    print(df)

# Cerrar la conexión a la base de datos
conn.close()
