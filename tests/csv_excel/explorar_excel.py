import pandas as pd

datos = pd.read_excel('CoffeeShopSales.xlsx')

print("---Columas a usar: ---")
print(datos.columns.tolist())

print("---Primeras 5 filas: ---")
print(datos.head())

datos.to_csv('ventas_kaggle_crudas.csv', index=False, encoding='utf-8')
print("Archivo CSV creado exitosamente.")