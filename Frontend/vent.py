import tkinter as tk

#Crear la ventana principal

ventana = tk.Tk()
ventana.title("Login")

#Titulo de la ventana

#Establecer tamaño de la ventana

ventana.geometry("300x500")

#Crear la etiqueta con el texto "Inicio de sesión"

label = tk.Label(ventana, text="Inicio de sesion", font=("Arial", 18))
label.pack(pady=20)
#Empacar la etiqueta con algo de espacio vertical

#Mostrar la ventana
ventana.mainloop()