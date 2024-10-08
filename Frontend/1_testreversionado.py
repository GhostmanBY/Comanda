from customtkinter import *
from PIL import Image, ImageTk
import os
import sqlite3
from tkinter import messagebox  # Asegúrate de importar messagebox si lo usas

ruta_db = os.path.join("DB", "Panel_admin.db")

def maximizar_pantalla():
    root.state("zoom")

# Función para mostrar ventana emergente
def ventana_emergente(mensaje):
    messagebox.showinfo("Aviso", f"{mensaje}")

# Función para verificar código
def verificar(code):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    instruccion = f"SELECT * FROM Usuarios WHERE Codigo like '{code}'"
    cursor.execute(instruccion)

    datos = cursor.fetchall()

    conn.commit()
    conn.close()

    if datos != []:
        if code == datos[0][1]:
            ventana_emergente("Bienvenido")
            Cambio_fram(datos[0][1])  # Cambiar de frame al loguearse
        else:
            ventana_emergente("Su código no es correcto")
    else:
        ventana_emergente("Usted no está en el sistema")

# Configuración de la ventana principal
root = CTk()
root.title("Login")
root.geometry("600x400")
root.after(100,maximizar_pantalla)
#root.configure(fg_color="#FF6103")

# Frame principal
frame_login = CTkFrame(master=root, width=800, height=768, fg_color="white")
frame_login.grid(row=0, column=0, sticky="ns")


# Imagen del logo
foto = Image.open("Frontend/nombre.png")
ft = CTkImage(foto, size=(250, 250))
frame_image = CTkFrame(frame_login)
label1 = CTkLabel(master=frame_login, image=ft, text="")
label1.pack(pady=10)

# Campo de texto para el código del usuario
fuente = CTkFont(family="Segoe UI", size=14)
entry_usuario = CTkEntry(master=frame_login, placeholder_text="Ingrese su código", text_color="black", 
                         fg_color="white", border_color="#FF6103", width=200, height=40, font=fuente)
entry_usuario.pack(pady=20)

# Botón de inicio de sesión
fuente = CTkFont(family="Segoe UI Black", size=14)
boton1 = CTkButton(master=frame_login, text="LOG IN", fg_color="#FF6103", command=lambda: verificar(entry_usuario.get()), width=200, height=40, font=fuente)
boton1.pack(pady=20)

# Parte del código original
def Cambio_fram(Text):
    # Ocultar elementos originales
    # Se supone que estas variables están definidas previamente
    try:
        texto_label.place_forget()
        campo_label.place_forget()
        boton_cambio.place_forget()
    except Exception as e:
        print("Error al ocultar elementos:", e)

    print(f"Texto del entry: {Text}")

    # Mostrar el frame con el fondo de la imagen
    frame_tab_opciones.place(relx=0.25, rely=0, relwidth=0.75, relheight=1)

# Configurar la imagen de fondo

    background = Image.open("C:/Users/PC6/Documents/GitHub/Comanda/Frontend/lol.png")  # la ruta de la imagen
    print("cargando")
    background = background.resize((800, 700))  # Ajustar el tamaño
    bg_image = ImageTk.PhotoImage(background)

    # Crear un Label con la imagen de fondo
    bg_label = CTkLabel(master=frame_tab_opciones, image=bg_image,text="asddsa")
    bg_label.image = bg_image  # Mantener una referencia
    bg_label.place(relwidth=1, relheight=1)  # Hacer que ocupe todo el frame

    text_mozo = CTkLabel(frame_tab_opciones, text="Alta mozo", width=100, height=50)
    text_mozo.place(relx=0.3, rely=0.1)

    entry_mozo = CTkEntry(frame_tab_opciones, width=100, height=50, placeholder_text="nombre")
    entry_mozo.place(relx=0.3, rely=0.2)



# Frame para separar el espacio de login
frame_tab_opciones = CTkFrame(root, width=900, height=700)

# Configurar filas y columnas para expandir el frame
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Mostrar ventana 
root.mainloop()