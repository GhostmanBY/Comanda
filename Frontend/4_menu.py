
import customtkinter as ctk

# Inicializar CustomTkinter
ctk.set_appearance_mode("System")  # "Dark","Light" o "System" para usar el modo del sistema
ctk.set_default_color_theme("blue")  # Tema de color

# Crear la ventana principal
root = ctk.CTk()
root.title("Menu")
root.geometry("1024x768")

# Sección para los botones de menú
label_menu = ctk.CTkLabel(root,
                           text="Seleccione categoría:",
                           #fg_color="darkorange",
                           font=( "Comic Sans MS",25,"bold"),
                           text_color="white",
                           width=40, height=40,
                           anchor="center"
                           )  ########################## ACA LOCO
label_menu.pack(padx=20,pady=20) 

# Botones para categorías de menú
frame_menu = ctk.CTkFrame(master=root)  # Crear el frame que contendrá los botones
frame_menu.pack(expand=True, fill='both', padx=20, pady=20)  # Expandir para ocupar espacio

# Configurar las filas y columnas para que se expandan
frame_menu.grid_rowconfigure((0, 1, 2, 3), weight=1)  # Permitir que las filas se expandan
frame_menu.grid_columnconfigure((0, 1, 2 ), weight=1)  # Permitir que las columnas se expandan


# Creamos 9 botones con distintas categorias del menú

boton_entra=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="ENTRADAS",fg_color="#FF6103", hover_color="#fca975")
boton_entra.grid(row=0, column=0, padx=1,pady=1, sticky="nsew")

boton_princi=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="PLATOS PRINCIPALES",fg_color="#FF6103", hover_color="#fca975")
boton_princi.grid(row=0, column=1, padx=1,pady=1, sticky="nsew")

boton_bebi=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="BEBIDAS",fg_color="#FF6103", hover_color="#fca975")
boton_bebi.grid(row=0, column=2, padx=1,pady=1, sticky="nsew")

boton_infan=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="INFANTIL",fg_color="#FF6103", hover_color="#fca975")
boton_infan.grid(row=1, column=0, padx=1,pady=1, sticky="nsew")

boton_post=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="POSTRES",fg_color="#FF6103", hover_color="#fca975")
boton_post.grid(row=1, column=1, padx=1,pady=1, sticky="nsew")

boton_vegan=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="VEGANA",fg_color="#FF6103", hover_color="#fca975")
boton_vegan.grid(row=1, column=2, padx=1,pady=1, sticky="nsew")

boton_cafe=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="CAFETERÍA",fg_color="#FF6103", hover_color="#fca975")
boton_cafe.grid(row=2, column=0, padx=1,pady=1, sticky="nsew")

boton_especial=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="ESPECIALIDADES",fg_color="#FF6103", hover_color="#fca975")
boton_especial.grid(row=2, column=1, padx=1,pady=1, sticky="nsew")

boton_minu=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),height=20, width=20, text="MINUTAS",fg_color="#FF6103", hover_color="#fca975")
boton_minu.grid(row=2, column=2, padx=1,pady=1, sticky="nsew")


# Mostrar ventana
root.mainloop()

#Vamos mejorando Dios mediante :)
