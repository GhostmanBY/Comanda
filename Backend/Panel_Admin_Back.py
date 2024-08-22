import os
import sqlite3 as sql

ruta_db = os.path.join("D:/Users/Usuario/Documents/GitHub/Comanda/ArchivosDB", "Productos.db")

def crear_tablas():

    conn = sql.connect(ruta_db)
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
        Ingreso integer)"""
    )

    conn.commit()
    conn.close()

def Cargar_Producto(name, precio, stock):
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    
    instruccion = f"INSERT INTO Productos VALUES('{name}', {precio}, {stock})"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def Modificar_Productos(name, categoria, nuevo_valor):
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"UPDATE Productos SET {categoria} = {nuevo_valor} WHERE Nombre like '{name}'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def Mostrar_Productos():
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"SELECT * FROM Productos"
    cursor.execute(instruccion)

    datos = cursor.fetchall()

    conn.commit()
    conn.close()

    return datos

def Eliminar_Producto(name):
    conn = sql.connect(ruta_db)
    cursor = conn.cursor()
    
    instruccion = f"DELETE FROM Productos WHERE Nombre like '{name}'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

#def Registro_Empleado()


if __name__ == "__main__":
    crear_tablas()

    op = 0
    while op != 5:
        op = int(input("""
Ingrese la opcion que quiere realizar:
1- Cargar producto
2- Mostrar producto
3- Modificar producto
4- Eliminar producto
5- Salir
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
