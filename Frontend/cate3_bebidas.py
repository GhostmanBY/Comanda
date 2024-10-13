#OPCIONES DE BEBIDAS


import customtkinter as ctk

# Inicializar CustomTkinter
ctk.set_appearance_mode("System")  # "Dark","Light" o "System" para usar el modo del sistema
ctk.set_default_color_theme("blue")  # Tema de color

# Crear la ventana principal
root = ctk.CTk()
root.title("CATEGORIAS 3")
root.geometry("1024x768")

# Sección para los botones de menú
label_menu = ctk.CTkLabel(root,
                           text="SELECCIONE BEBIDA:",
                           #fg_color="darkorange",
                           font=( "Comic Sans MS",25,"bold"),
                           text_color="white",
                           width=40, height=40,
                           anchor="center"
                           )  ########################## ACA LOCO
label_menu.pack(padx=20,pady=20) 


#FRAME SCROLLEABLE
frame_menu = ctk.CTkScrollableFrame(master=root, orientation="vertical") 
frame_menu.pack(expand=True, fill='both', padx=20, pady=10) 

#TAMAÑO DEL FRAME
frame_menu.grid_rowconfigure((0, 1, 2, 3), weight=1)  # Permitir que las filas se expandan
frame_menu.grid_columnconfigure((0, 1, 2 ), weight=1)  # Permitir que las columnas se expandan

#CREANDO LOS BOTONES CON LAS OPCIONES DE EJEMPLO
boton1=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Coca-Cola 1.5L",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton1.grid(row=0, column=0, padx=1,pady=1, sticky="nsew")

boton2=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Sprite 1.5L",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton2.grid(row=0, column=1, padx=1,pady=1, sticky="nsew")

boton3=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Fanta 1.5L",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton3.grid(row=0, column=2, padx=1,pady=1, sticky="nsew")

boton4=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Pepsi 1.5L",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton4.grid(row=1, column=0, padx=1,pady=1, sticky="nsew")

boton5=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Agua mineral 600ml",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton5.grid(row=1, column=1, padx=1,pady=1, sticky="nsew")

boton6=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Agua saborizada 1.5L",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton6.grid(row=1, column=2, padx=1,pady=1, sticky="nsew")

boton7=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Exprimido frutilla",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton7.grid(row=2, column=0, padx=1,pady=1, sticky="nsew")

boton8=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Exprimido naranja",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton8.grid(row=2, column=1, padx=1,pady=1, sticky="nsew")

boton9=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Licuado banana",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton9.grid(row=2, column=2, padx=1,pady=1, sticky="nsew")


app=root.mainloop()
