from Backend.Panel_Admin_Back import cargar_productos, Modificar_producto, eliminar_producto, Mostrar_productos

from customtkinter import* 

def funcion():
    txto1.pack_forget()
    txto2.pack_forget()
    txto3.pack_forget()
    boton1.pack_forget()
    boton2.pack_forget()
    
    texto1 = CTkTextbox(root, width=400, height=400, font=('Arial', 12))
    texto1.pack()
    
    datos = Mostrar_productos()
    
    for producto in datos:
        texto1.insert("1.0", f"{producto['Nombre']}\n")
        texto1.insert("2.0", f"{producto['Precio']}$\n")
        texto1.insert("3.0", f"{producto['Stock']}\n")
    
root = CTk()
root.title("Inicio")
root.geometry("500x500")

txto1 = CTkEntry(root, width=200, height=50)
txto1.pack()

txto2 = CTkEntry(root, width=200, height=50)
txto2.pack()

txto3 = CTkEntry(root, width=200, height=50)
txto3.pack()

boton1 = CTkButton(root, width=200, height=50, text="aceptar", command=lambda: cargar_productos(txto1.get(), txto2.get(), txto3.get()))
boton1.pack(pady=20)

boton2 = CTkButton(root, width=200, height=50, text="aceptar", command= funcion)
boton2.pack(pady=20)

root.mainloop()

