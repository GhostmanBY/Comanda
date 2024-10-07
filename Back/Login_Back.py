import os
import sys
import sqlite3
import json

base_dir = os.path.dirname(os.path.abspath(__file__)) #Ruta de donde esta este archivo

ruta_db = os.path.join(base_dir, "../DB/Panel_admin.db") #Ruta para encontrar la DB

def verificar_login(code: int):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"SELECT * from Usuario"
    cursor.execute(instruccion)

    data = cursor.fetchall()

    conn.commit()
    conn.close()
    
    for Mozo in data:
        if code == Mozo[2]: 
            data = {
                "ID": Mozo[0],
                "Nombre": Mozo[1],
            }
            return data
        else:
            return 0

if __name__ == "__main__":
    Verificacion = verificar_login("UEHS065")
    if isinstance(Verificacion, dict) == True:
        print(f"Se a logiado exitosamente señor {Verificacion['Nombre']}") 
    else:
        print(f"Su codigo no es correcto o usted no esta en el sistema")