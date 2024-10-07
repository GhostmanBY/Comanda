
import tkinter as tk
from tkinter import font

# Crear una ventana principal de Tkinter
ventana = tk.Tk()
ventana.withdraw() # Ocultar la ventana principal

# Obtener todas las fuentes disponibles en el sistema
fuentes_disponibles = list(font.families())

# Mostrar la lista de fuentes
for fuente in fuentes_disponibles:
    print(fuente)

ventana.destroy() # Cerrar la ventana