import customtkinter as ctk

# Función para agregar texto al cuadro de texto
def agregar_texto():
    textbox.insert("1.0", "Este es un texto agregado.\n")  # Agrega texto al inicio del cuadro de texto

# Crear la ventana principal
ventana = ctk.CTk()  # Usar CTk en lugar de Tk
ventana.title("Ejemplo de CTkTextbox")

# Configurar el tema
ctk.set_appearance_mode("light")  # O "dark" para un tema oscuro
ctk.set_default_color_theme("blue")  # Cambiar el color del tema

# Crear un cuadro de texto personalizado
textbox = ctk.CTkTextbox(ventana, width=400, height=200, font=('Arial', 12))
textbox.pack(pady=20, padx=20)

# Crear un botón para agregar texto al cuadro de texto
boton_agregar = ctk.CTkButton(ventana, text="Agregar Texto", command=agregar_texto)
boton_agregar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
