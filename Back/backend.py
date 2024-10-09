# backend.py

import os
import sqlite3

ruta_db = os.path.join("DB", "Panel_admin.db")

# Función para verificar código
def verificar(code, ventana_emergente):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"SELECT * FROM Usuarios WHERE Codigo like '{code}'"
    cursor.execute(instruccion)

    datos = cursor.fetchall()

    conn.commit()
    conn.close()

    if datos:
        if code == datos[0][1]:
            ventana_emergente("Bienvenido")  # Mostrar mensaje de bienvenida
            Cambio_fram(datos[0][1])  # Cambiar de frame al loguearse
        else:
            ventana_emergente("Su código no es correcto")
    else:
        ventana_emergente("Usted no está en el sistema")

def Cambio_fram(Text):
    # Aquí se maneja el cambio de frames y la visualización de UI  
    # Falta implementar esta función
    print(f"Texto del entry: {Text}")