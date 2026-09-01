import csv
import psycopg2

try:
    conexion = psycopg2.connect(
        host="localhost",
        port="5432",
        database="bellidiel_db",
        user="postgres",
        password="bellidiel123"
    )
    cursor = conexion.cursor()

    print("Preparando la base de datos de BelliDiel...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS catalogo_menu (
            product_id VARCHAR(50) PRIMARY KEY,
            unit_price NUMERIC(10, 2),
            product_category VARCHAR(100),
            product_type VARCHAR(100),
            product_detail VARCHAR(255)
        );
    """)

    archivo_csv = 'bellidiel_productos_limpio.csv'
    filas_insertadas = 0
    duplicados_ignorados = 0

    print("Inyectando productos...")
    with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            try:

                cursor.execute("""
                    INSERT INTO catalogo_menu (product_id, unit_price, product_category, product_type, product_detail)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (product_id) DO NOTHING;
                """, (
                    fila['product_id'],
                    float(fila['unit_price']),
                    fila['product_category'],
                    fila['product_type'],
                    fila['product_detail']
                ))
                
                if cursor.rowcount == 1:
                    filas_insertadas += 1
                else:
                    duplicados_ignorados += 1
                    
            except ValueError:
                pass

    conexion.commit()
    print(f"¡Éxito! Se subieron {filas_insertadas} productos únicos a la nube.")
    print(f"Se ignoraron {duplicados_ignorados} registros repetidos.")

except Exception as e:
    print("Ocurrió un error de conexión:", e)
finally:
    if 'conexion' in locals() and conexion:
        cursor.close()
        conexion.close()