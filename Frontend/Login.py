#liberias de diseño 
import tkinter as tk
from tkinter import messagebox
from customtkinter import *
from Ventana_Principal import main
import sqlite3

ruta_db = os.path.join("DB", "Panel_admin.db")
# Login.py

def ventana_emergente(messege):
    messagebox.showinfo("Aviso", f"{messege}")


def verificar(code):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    
    instruccion = f"SELECT * from Usuarios WHERE Codigo like '{code}'"
    cursor.execute(instruccion)
    
    datos = cursor.fetchall()
    
    conn.commit()
    conn.close()
    
    if datos != []:
        if code == datos[0][1]:
            ventana_emergente("Bienvenido")
        else:
            ventana_emergente("Su codigo no es correcto")
    else:
        ventana_emergente("Usted no esta en el sistema")

#define una variable para darle los parametros de las letras
letra = "Arial", 30, "bold"

#Funcion que cierra la ventana del login y llama a la ventana principal
def accion(codigo, ventana):
    ventana.destroy() #destruye la ventana
    main(codigo) #llama a la funcion del archivo Ventana_Principal

from tkinter import messagebox
from customtkinter import *
from PIL import Image

#def verificación():




root = CTk()
root.title("Login")
root.geometry("400x400")
root.configure(fg_color="#FF6103")


frame1 = CTkFrame(master=root, width=400, height=100, fg_color="white")
frame1.pack(pady=10)

foto = Image.open("nombre.png")
ft = CTkImage(foto, size=(200, 200))  
label1 = CTkLabel(master=frame1, image=ft, text="")
label1.pack(pady=10)


entry_usuario = CTkEntry(master=frame1, placeholder_text="AOE505", fg_color="white", border_color="white", width=100, height=40)
entry_usuario.pack(pady=20)

boton1 = CTkButton(master=frame1,text="LOG IN", fg_color="#FF6103", command=verificar)
boton1.pack(pady=20)

root.mainloop()


