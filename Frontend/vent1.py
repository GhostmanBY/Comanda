import customtkinter as ctk

    #Funcion para manejar el evento del boton"Inicio"
def iniciar_sesion():
    codigo = entry_codigo.get()
    print (f"Codigo ingresado:{codigo}") 

    #Aqui se puede agregar la logica para validar el codigo

    #Inicializar CustomTkinter
ctk.set_appearance_mode("System")
    # "Dark","Light" o "System" para usar el modo del sistema
ctk.set_default_color_theme("blue")
    #Tema de color

    #Crear la ventana principal

ventana= ctk.CTk()
ventana.title("Resto")
ventana.geometry("1024x768")

    #Etiqueta que dice "Resto"
label_resto = ctk.CTkLabel(ventana,text="Resto", font=("Arial",18))
label_resto.pack(pady=10)

    #Campo para ingresar el codigo

label_codigo = ctk.CTkLabel(ventana,text="Ingresa tu codigo: ")
label_codigo.pack(pady=5)

entry_codigo = ctk.CTkEntry(ventana)
entry_codigo.pack(pady=5)

    # Boton que dice "Inicio"
boton_inicio = ctk.CTkButton(ventana,text="Inicio", command=iniciar_sesion)
boton_inicio.pack(pady=20)

    #mostrar la ventana

ventana.mainloop()

