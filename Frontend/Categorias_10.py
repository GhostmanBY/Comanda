#OPCIONES DE ENTRADAS


import customtkinter as ctk

# Inicializar CustomTkinter
ctk.set_appearance_mode("System")  # "Dark","Light" o "System" para usar el modo del sistema
ctk.set_default_color_theme("blue")  # Tema de color

# Crear la ventana principal
root = ctk.CTk()
root.title("CATEGORIAS 1")
root.geometry("1024x768")

# Sección para los botones de menú
label_menu = ctk.CTkLabel(master=root,
                          text="SELECCIONE PLATO:",
                          font=("Comic Sans MS",25,"bold"),
                          text_color="white",
                          width=40, height=40,
                          anchor="center" ) 
label_menu.pack(padx=20,pady=20) 


#FRAME SCROLLEABLE
frame_menu = ctk.CTkScrollableFrame(master=root, orientation="vertical") 
frame_menu.pack(expand=True, fill='both', padx=30, pady=20) 

#TAMAÑO DEL FRAME
frame_menu.grid_rowconfigure((0, 1, 2), weight=1)  # Permitir que las filas se expandan
frame_menu.grid_columnconfigure((0, 1, 2 ), weight=1)  # Permitir que las columnas se expandan


#AGRANDAR BOTONES plis

#CREANDO LOS BOTONES CON LAS OPCIONES DE EJEMPLO
boton1=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Picada mixta",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton1.grid(row=0, column=0, padx=1,pady=1, sticky="nsew")

boton2=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Empanadas",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton2.grid(row=0, column=1, padx=1,pady=1, sticky="nsew")

boton3=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Chinchulines",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton3.grid(row=0, column=2, padx=1,pady=1, sticky="nsew")

boton4=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Ensalada mixta",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton4.grid(row=1, column=0, padx=1,pady=1, sticky="nsew")

boton5=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Sopa crema",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton5.grid(row=1, column=1, padx=1,pady=1, sticky="nsew")

boton6=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Provoleta",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton6.grid(row=1, column=2, padx=1,pady=1, sticky="nsew")

boton7=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Fondue 4 quesos",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton7.grid(row=2, column=0, padx=1,pady=1, sticky="nsew")

boton8=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Tortilla de papa",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton8.grid(row=2, column=1, padx=1,pady=1, sticky="nsew")

boton9=ctk.CTkButton(master=frame_menu, font=("Comic Sans MS",30),text="Sandwich miga",height=20, width=20, fg_color="#FF6103", hover_color="#fca975")
boton9.grid(row=2, column=2, padx=1,pady=1, sticky="nsew")


app=root.mainloop()
