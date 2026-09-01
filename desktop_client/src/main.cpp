#include <iostream>
#include "sqlite3.h"

int main() {
    std::cout << "========================================\n";
    std::cout << "  Iniciando BelliDiel ERP (Terminal)\n";
    std::cout << "  Motor Offline-First preparado.\n";
    std::cout << "========================================\n\n";

    sqlite3* base_datos;
    char* mensaje_error = nullptr;

    int resultado = sqlite3_open("bellidiel_local.db", &base_datos);

    if (resultado != SQLITE_OK) {
        std::cerr << "Error al conectar con SQLite: " << sqlite3_errmsg(base_datos) << std::endl;
        return 1;
    } else {
        std::cout << "[EXITO] Conectado a la base de datos local.\n";
    }

    const char* sql_crear_tabla = 
        "CREATE TABLE IF NOT EXISTS menu_local ("
        "product_id TEXT PRIMARY KEY, "
        "unit_price REAL, "
        "product_category TEXT, "
        "product_type TEXT, "
        "product_detail TEXT);";

    resultado = sqlite3_exec(base_datos, sql_crear_tabla, nullptr, 0, &mensaje_error);

    if (resultado != SQLITE_OK) {
        std::cerr << "Error al crear la tabla: " << mensaje_error << std::endl;
        sqlite3_free(mensaje_error);
    } else {
        std::cout << "[EXITO] Tabla 'menu_local' lista para trabajar.\n";
    }

    sqlite3_close(base_datos);

    return 0;
}