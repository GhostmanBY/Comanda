import os
import random
from datetime import datetime
import sqlite3

ruta_db = os.path.join("DB", "Productos.db")

def Generar_Codigo():    
    lista_Letras = ["A", "B", "C", "D", "E", "F", "G",
                    "H", "I", "J", "K", "L", "M", "N", 
                    "O","P", "Q", "S", "T", "R", "U", 
                    "V", "W", "X", "Y", "Z"]
    codigo = list("AOOE505")
    for i in range(len(lista_Letras)):
            valor_R_letra = random.randint(0, len(lista_Letras)-1)
            if i <= 3:
                codigo[i] = lista_Letras[valor_R_letra]
            elif i <= 6:
                valor_R_numero = random.randint(0, 9)

                codigo[i] = str(valor_R_numero)
            
            if i == 6:
                break
    codigo = ''.join(codigo)

    return codigo

def crear_tablas():

    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Productos(
        Nombre text,
        Precio integer,
        Stock integer)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Usuarios(
        Mozo text,
        Codigo text,
        Plaza integer,
        Ingreso text)"""
    )

    conn.commit()
    conn.close()

def Cargar_Producto(name, precio, stock):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    
    instruccion = f"INSERT INTO Productos VALUES('{name}', {precio}, {stock})"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def Modificar_Productos(name, categoria, nuevo_valor):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"UPDATE Productos SET {categoria} = {nuevo_valor} WHERE Nombre like '{name}'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def Mostrar_Productos():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"SELECT * FROM Productos"
    cursor.execute(instruccion)

    datos = cursor.fetchall()

    conn.commit()
    conn.close()

    return datos

def Eliminar_Producto(name):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    
    instruccion = f"DELETE FROM Productos WHERE Nombre like '{name}'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def Registro_Empleado(name, codigo, Plaza, Fecha):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"INSERT INTO Usuarios VALUES('{name}', '{codigo}', {Plaza}, '{Fecha}')"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def Mostrar_Empleados():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"SELECT * FROM Usuarios"
    cursor.execute(instruccion)

    datos = cursor.fetchall()

    conn.commit()
    conn.close()

    return datos

if __name__ == "__main__":
    crear_tablas()

    po = 0
    while po != 3:
        po = int(input("""
Ingrese la opcion que quiere realizar
1- Carta
2- Personal
3- Salir
RTA: """))

        if po == 1:
            op = 0
            while op != 5:
                op = int(input("""
Ingrese la opcion que quiere realizar:
1- Cargar producto
2- Mostrar producto
3- Modificar producto
4- Eliminar producto
5- Volver
RTA: """))

                if op == 1:
                    nombre = input("Ingrese el nombre del producto: ")
                    precio = int(input("Ingrese el precio del producto: "))
                    stock = int(input("Ingrese el stock del producto: "))
                    Cargar_Producto(nombre, precio, stock)
                    input("Presione enter...")
                    os.system("cls")

                elif op == 2:
                    datos = Mostrar_Productos()
                    for i in range(0, len(datos)):
                        for j in range(0, 3):
                            if j == 0:
                                print(f"Nombre: {datos[i][j]}")
                            elif j == 1:
                                print(f"Precio: {datos[i][j]}")
                            elif j == 2:
                                print(f"Stock: {datos[i][j]}")
                        print("-"*15)
                    input("Preisone Enter...")
                    os.system("cls")

                elif op == 3:
                    nombre = input("Ingrese el nombre del producto: ")
                    categoria = input("Ingrese lo que va a modificar si el preico o el stock: ")
                    valor_nuevo = int(input(f"Ingrese el {categoria} del producto: "))
                    Modificar_Productos(nombre, categoria.capitalize(), valor_nuevo)
                    input("Presione enter...")
                    os.system("cls")

                elif op == 4:
                    nombre = input("Ingrese el nombre del producto a eliminar: ")
                    Eliminar_Producto(nombre)
                    input("Presione enter...")
                    os.system("cls")
        elif po == 2:
            pop = 0
            while pop != 5:
                pop = int(input("""
Ingrese la opciona que quiere realizar:
1- Registrar nuevo empleado
2- Mostrar empleados
3- Modificar empleado
4- Eliminar empleado
5- Volver
RTA: """))
                if pop == 1:
                    name = input("Ingrese el nombre del mozo: ")
                    
                    codigo = Generar_Codigo()

                    Plaza = int(input("Ingrese la plaza a la que va a estar asiganado: "))

                    Fecha = datetime.now().strftime("%H:%M")
        
                    Registro_Empleado(name, codigo, Plaza, Fecha)
                    os.system("cls")
                elif pop == 2:
                    datos = Mostrar_Empleados()
                    for i in range(0, len(datos)):
                        for j in range(0, 4):
                            if j == 0:
                                print(f"Mozo: {datos[i][j]}")
                            elif j == 1:
                                print(f"Codigo: {datos[i][j]}")
                            elif j == 2:
                                print(f"Plaza: {datos[i][j]}")
                            elif j == 3:
                                print(f"Horario: {datos[i][j]}")
                        print("-"*15)
                    input("Preisone Enter...")
                    os.system("cls")
