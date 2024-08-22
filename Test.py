from Backend.Panel_Admin_Back import Cargar_Producto, Mostrar_Productos, Modificar_Productos, Eliminar_Producto

from customtkinter import* 

def funcion():
    txto1.pack_forget()
    txto2.pack_forget()
    txto3.pack_forget()
    boton1.pack_forget()
    boton2.pack_forget()
    
    texto1 = CTkTextbox(root, width=400, height=400, font=('Arial', 12))
    texto1.pack()
    
    datos = Mostrar_Productos()

    for i in range(0, len(datos)):
                for j in range(0, 3):
                    if j == 0:
                        texto1.insert("1.0", f"Nombre: {datos[i][j]}\n\n")
                    elif j == 1:
                        texto1.insert("2.0", f"Precio: {datos[i][j]}\n")
                    elif j == 2:
                        texto1.insert("3.0", f"Stock: {datos[i][j]}\n")
                texto1.insert("4.0", "-"*15)

def funcion_2():
    txto2.pack_forget()
    txto3.pack_forget()

    boton1.pack_forget()
    boton2.pack_forget()
    boton3.pack_forget()
    boton4.pack_forget()
    
    boton5 = CTkButton(root, width=200, height=50, text="Eliminar", command=lambda: Eliminar_Producto(txto1.get()))
    boton5.pack()
root = CTk()
root.title("Inicio")
root.geometry("500x500")

txto1 = CTkEntry(root, width=200, height=50)
txto1.pack()

txto2 = CTkEntry(root, width=200, height=50)
txto2.pack()

txto3 = CTkEntry(root, width=200, height=50)
txto3.pack()

boton1 = CTkButton(root, width=200, height=50, text="Cargar", command=lambda: Cargar_Producto(txto1.get(), txto2.get(), txto3.get()))
boton1.pack(pady=20)

boton2 = CTkButton(root, width=200, height=50, text="mostrar", command= funcion)
boton2.pack(pady=20)

boton3 = CTkButton(root, width=200, height=50, text="modificar", command=lambda: Modificar_Productos(txto1.get(), txto2.get(), txto3.get()))
boton3.pack(pady=20)

boton4 = CTkButton(root, width=200, height=50, text="Eliminar", command= funcion_2)
boton4.pack(pady=20)

root.mainloop()

