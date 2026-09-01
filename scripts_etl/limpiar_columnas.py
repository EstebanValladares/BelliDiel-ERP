import csv

# 1. Nombres de tus archivos
archivo_origen = 'ventas_kaggle_crudas.csv' 
archivo_destino = 'bellidiel_productos_limpio.csv'

# 2. Las columnas exactas que pediste
columnas_deseadas = ['product_id', 'unit_price', 'product_category', 'product_type', 'product_detail']

try:
    with open(archivo_origen, mode='r', encoding='utf-8') as archivo_in, \
         open(archivo_destino, mode='w', encoding='utf-8', newline='') as archivo_out:
        
        lector = csv.DictReader(archivo_in)
        escritor = csv.DictWriter(archivo_out, fieldnames=columnas_deseadas)
        
        # Escribimos la cabecera con los 5 nombres en el archivo nuevo
        escritor.writeheader()
        
        filas_procesadas = 0
        
        # 3. Leer el original y extraer solo lo necesario
        for fila in lector:
            # Creamos una nueva fila rescatando solo las 5 columnas que te interesan
            fila_filtrada = {columna: fila.get(columna, '') for columna in columnas_deseadas}
            
            # Guardamos la fila en el nuevo documento
            escritor.writerow(fila_filtrada)
            filas_procesadas += 1

    print(f"¡Éxito! Se procesaron {filas_procesadas} filas.")
    print(f"Revisa el archivo '{archivo_destino}' en esta misma carpeta.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_origen}'. Revisa que esté en la misma carpeta que este script.")