# frontend.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Back.Login_Back import verificar_login # Importa la función que verifica el código

def maximizar_pantalla():
    root.state("zoom")
# Configuración de la ventana principal
root = CTk()
root.title("Login")
root.geometry("600x400")
root.after(100, maximizar_pantalla)

# Función para maximizar la pantalla
def maximizar_pantalla():
    root.state("zoom")

# Función para mostrar ventana emergente
def ventana_emergente(mensaje):
    messagebox.showinfo("Aviso", f"{mensaje}")

# Frame principal
frame_login = CTkFrame(master=root, width=800, height=768, fg_color="white")
frame_login.grid(row=0, column=0, sticky="ns")

# Imagen del logo
foto = Image.open("Frontend/imagenes/nombre.png")
ft = CTkImage(foto, size=(250, 250))
label1 = CTkLabel(master=frame_login, image=ft, text="")
label1.place(pady=10)

# Campo de texto para el código del usuario
fuente = CTkFont(family="Segoe UI", size=14)
entry_usuario = CTkEntry(master=frame_login, placeholder_text="Ingrese su código", text_color="black", 
                         fg_color="white", border_color="#FF6103", width=200, height=40, font=fuente)
entry_usuario.pack(pady=20)

# Botón de inicio de sesión
fuente = CTkFont(family="Segoe UI Black", size=14)
boton1 = CTkButton(master=frame_login, text="LOG IN", fg_color="#FF6103", 
                   command=lambda: verificar_login(entry_usuario.get()), 
                   width=200, height=40, font=fuente)
boton1.pack(pady=20)

# Frame para separar el espacio de login
frame_tab_opciones = CTkFrame(root, width=900, height=700)

# Configurar filas y columnas para expandir el frame
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Mostrar ventana 
root.mainloop()