import os
import json

def cargar_productos(nombre, precio, stock):
    nuevo_producto = {
        "Nombre": nombre,
        "Precio": precio,
        "Stock": stock
    }

    ruta_archivo = "archivo.json"

    # Verificar si el archivo ya existe y tiene contenido
    if os.path.exists(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:
        with open(ruta_archivo, "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = []

    # Agregar el nuevo producto a la lista
    datos.append(nuevo_producto)

    # Guardar los datos en el archivo
    with open(ruta_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def Mostrar_productos():
    with open("archivo.json", "r") as archivo:
        datos = json.load(archivo)
    for producto in datos:
        print(f"Nombre: {producto["Nombre"]}\nPrecio: {producto["Precio"]}\nStock: {producto["Stock"]}\n")

def Modificar_producto(nombre, nuevo_precio, nuevo_stock):
    ruta_archivo = "archivo.json"
    
    with open(ruta_archivo, "r") as archivo:
        datos = json.load(archivo)

    # Buscar y modificar el producto
    for producto in datos:
        if producto["Nombre"] == nombre:
            producto["Precio"] = nuevo_precio
            producto["Stock"] = nuevo_stock
            break

    # Guardar los cambios
    with open(ruta_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def eliminar_producto(nombre):
    ruta_archivo = 'archivo.json'

    # Verificar si el archivo existe y tiene contenido
    if os.path.exists(ruta_archivo) and os.path.getsize(ruta_archivo) > 0:
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)

        # Filtrar la lista para eliminar el producto con el nombre dado
        datos = [producto for producto in datos if producto['Nombre'] != nombre]
            
        # Guardar la lista actualizada en el archivo
        with open(ruta_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

        print(f"Producto '{nombre}' eliminado exitosamente.")
    else:
        print("El archivo JSON no existe o está vacío.")

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
        cargar_productos(nombre, precio, stock)
        input("Presione enter...")
        os.system("cls")
    elif op == 2:
        Mostrar_productos()
        input("Presione enter...")
        os.system("cls")
    elif op == 3:
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        Modificar_producto(nombre, precio, stock)
        input("Presione enter...")
        os.system("cls")
    elif op == 4:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(nombre)
        input("Presione enter...")
        os.system("cls")