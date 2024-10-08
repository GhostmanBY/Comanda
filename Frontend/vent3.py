import customtkinter as ctk

#inicializar CustomTkinter 
ctk.set_appearance_mode("System")
#Tema del sistema
ctk.set_default_color_theme("blue")
#tema del color

#crear ventana principal orientada a pantalla de celular

ventana = ctk.CTk()
ventana.title("Mesa")
ventana.geometry("1024x768")
#tamaño tipico de celular

#Numero de la mesa(esto se puede cambiar dinamicamente)
numero_mesa = 1
#cambia este valor segun la mesa seleccionada

#etiqueta que muestra el numero de la mesa

label_mesa=ctk.CTkLabel(ventana,
             text=f"Mesa {numero_mesa}",
             font=("Arial",18))
label_mesa.pack(pady=10)

#campo para indicar la cantidad de comensales
label_comensales=ctk.CTkLabel(ventana,
             text="Comensales:")
label_comensales.pack(pady=5)

entry_comensales =ctk.CTkEntry(ventana,width=100)
entry_comensales.pack(pady=5)

#seccion par indicar si hay niños
label_ninos = ctk.CTkLabel(ventana,
text="Niños:")
label_ninos.pack(pady=5)


check_var_ninos = ctk.BooleanVar()
check_ninos = ctk.CTkCheckBox(ventana,text="¿Hay niños?",
variable=check_var_ninos)
check_ninos.pack(pady=5)

#campo para indicar la cantidad de niños
entry_cantidad_ninos=ctk.CTkEntry(ventana,width=100,placeholder_text="Cantidad de niños")
entry_cantidad_ninos.pack(pady=5)
'''
#Seccion para los botones de menu
label_menu=ctk.CTkLabel(ventana,
text="Selecciona opcion del menu:")
label_menu.pack(pady=10)

#Botones para categorias de menu
frame_menu = ctk.CTkFrame(ventana)
frame_menu.pack(pady=50)

boton_bebidas = ctk.CTkButton(frame_menu,
text="Bebidas",width=100)
boton_bebidas.grid(row=0,column=0,padx=15,pady=15)

boton_aperitivos = ctk.CTkButton(frame_menu,text="Aperitivos",width=100)
boton_aperitivos.grid(row=0,column=1,padx=15,pady=15)

boton_comidas = ctk.CTkButton(frame_menu,
text="Comidas",width=100)
boton_comidas.grid(row=1,column=0,padx=15,pady=15)

boton_platos = ctk.CTkButton(frame_menu,
text="Platos",width=100)
boton_platos.grid(row=1,column=1,padx=25,pady=15)

boton_postres = ctk.CTkButton(frame_menu,
text="Postres", width=100)
boton_postres.grid(row=2,
column=0,columnspan=2,pady=5,padx=15)
'''
ventana.mainloop()
