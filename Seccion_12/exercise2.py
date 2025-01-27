import pandas as pd
import os

file = "../datas/data.csv"
data = ""

if os.path.exists(file):
    data = pd.read_csv(file)


df = pd.DataFrame(data)

# 1. Calcular las ventas totales por producto
vtpp = df.groupby('producto')['ventas'].sum()
print(vtpp)


# 2. Producto más vendido en términos de cantidad

pmv = df.groupby('producto')['ventas'].sum().idxmax()
print(f"El producto más vendido es: {pmv}")




