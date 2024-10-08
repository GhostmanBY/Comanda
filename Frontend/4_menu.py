
import customtkinter as ctk

# Inicializar CustomTkinter
ctk.set_appearance_mode("System")  # "Dark","Light" o "System" para usar el modo del sistema
ctk.set_default_color_theme("blue")  # Tema de color

# Crear la ventana principal
root = ctk.CTk()
root.title("Menu")
root.geometry("1024x768")

# Sección para los botones de menú
label_menu = ctk.CTkLabel(root, text="Selecciona opción del menú:")
label_menu.pack(pady=10)

# Botones para categorías de menú
frame_menu = ctk.CTkFrame(root)  # Crear el frame que contendrá los botones
frame_menu.pack(expand=True, fill='both', padx=20, pady=20)  # Expandir para ocupar espacio

# Configurar las filas y columnas para que se expandan
frame_menu.grid_rowconfigure((0, 1, 2), weight=1)  # Permitir que las filas se expandan
frame_menu.grid_columnconfigure((0, 1), weight=1)  # Permitir que las columnas se expandan

# Crear botones con colores personalizados
boton_bebidas = ctk.CTkButton(frame_menu, text="Bebidas", width=100, fg_color="#FF6103", hover_color="#fca975")
boton_bebidas.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")  # sticky para llenar

boton_aperitivos = ctk.CTkButton(frame_menu, text="Aperitivos", width=100, fg_color="#FF6103", hover_color="#fca975")
boton_aperitivos.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")  # sticky para llenar

boton_comidas = ctk.CTkButton(frame_menu, text="Comidas", width=100, fg_color="#FF6103", hover_color="#fca975")
boton_comidas.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")  # sticky para llenar

boton_platos = ctk.CTkButton(frame_menu, text="Platos", width=100, fg_color="#FF6103", hover_color="#fca975")
boton_platos.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")  # sticky para llenar

boton_postres = ctk.CTkButton(frame_menu, text="Postres", width=100, fg_color="#FF6103", hover_color="#fca975")
boton_postres.grid(row=2, column=0, columnspan=2, pady=5, padx=15, sticky="nsew")  # sticky para llenar

# Mostrar ventana
root.mainloop()