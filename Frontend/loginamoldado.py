import tkinter as tk
from tkinter import messagebox
from customtkinter import *
'''from Ventana_Principal import ventana2'''
from PIL import Image
import sqlite3
import os
import customtkinter as ctk

ruta_db = os.path.join("DB", "Panel_admin.db")

def ventana_emergente(mensaje):
    messagebox.showinfo("Aviso", f"{mensaje}")

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
            ventana_emergente("Su código no es correcto")
    else:
        ventana_emergente("Usted no está en el sistema")

# Estilo de fuente
letra = ("Arial", 30, "bold")

# Función que cierra la ventana del login y llama a la ventana principal
def accion(codigo, ventana):
    ventana.destroy() # destruye la ventana
    main(codigo) # llama a la función del archivo Ventana_Principal
    
def continua():
    root.destroy()
    ventana2()

# Configuración de la ventana principal
root = CTk()
root.title("Login")
root.geometry("1024x768")  # Ajuste a pantalla de escritorio
root.configure(fg_color="#FF6103")
root.resizable(True, True)  # Permite redimensionar la ventana

# Frame principal
frame1 = CTkFrame(master=root, width=400, height=400, fg_color="white")
frame1.pack(pady=20, padx=20, expand=True)  # Uso de 'expand' para que se ajuste mejor en pantallas grandes

# Imagen del logo
foto = Image.open("Frontend/nombre.png")
ft = CTkImage(foto, size=(500, 500))  
label1 = CTkLabel(master=frame1, image=ft, text="")
label1.pack(pady=10)

# Campo de texto para el código del usuario
fuente = ctk.CTkFont(family="Segoe UI ", size=14)  # Definir la fuente
entry_usuario = CTkEntry(master=frame1, placeholder_text="Ingrese su codigo", text_color="black", 
                         fg_color="white", border_color="#FF6103", width=200, height=40,font=fuente)
entry_usuario.pack(pady=20)

# Botón de inicio de sesión
fuente = ctk.CTkFont(family="Segoe UI Black", size=14)  # Definir la fuente
boton1 = CTkButton(master=frame1, text="LOG IN", fg_color="#FF6103", command=continua, width=150, height=40,font=fuente)
boton1.pack(pady=20)

root.mainloop()
