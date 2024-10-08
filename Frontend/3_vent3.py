
import customtkinter as ctk

# Inicializar CustomTkinter 
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Crear ventana principal orientada a pantalla de escritorio
ventana = ctk.CTk()
ventana.title("Mesa")
ventana.geometry("1024x768")

# Cambiar el color de fondo de la ventana
ventana.configure(fg_color="#FF6103")  # Establecer el color de fondo

# Número de la mesa (esto se puede cambiar dinámicamente)
numero_mesa = 1

# Etiqueta que muestra el número de la mesa
label_mesa = ctk.CTkLabel(ventana,
                           text=f"Mesa {numero_mesa}",
                           font=("Segoe UI Black", 24))
label_mesa.pack(pady=20, fill='x')  # Ocupa todo el ancho disponible

# Crear un frame para organizar los elementos
frame = ctk.CTkFrame(ventana, fg_color="#FF6103")  # Establecer el color de fondo del frame
frame.pack(pady=20, fill='both', expand=True)  # Se expande para ocupar toda la pantalla

# Campo para indicar la cantidad de comensales
label_comensales = ctk.CTkLabel(frame,
                                  text="Comensales:")
label_comensales.pack(pady=5, anchor='w')  # Alinear a la izquierda

entry_comensales = ctk.CTkEntry(frame, width=512)  # Ancho de la mitad de la pantalla
entry_comensales.pack(pady=5, fill='x')  # Ocupará la mitad, pero permitirá el llenado

# Sección para indicar si hay niños
label_ninos = ctk.CTkLabel(frame,
                            text="Niños:")
label_ninos.pack(pady=10, anchor='w')  # Alinear a la izquierda

# Etiqueta para indicar si hay niños (moverla arriba)
check_var_ninos = ctk.BooleanVar()
check_ninos = ctk.CTkCheckBox(frame,
                               text="¿Hay niños?",
                               variable=check_var_ninos)
check_ninos.pack(pady=5, anchor='w')  # Alinear a la izquierda y ubicar abajo de la sección "niños"

# Campo para indicar la cantidad de niños
entry_cantidad_ninos = ctk.CTkEntry(frame, width=512, placeholder_text="Cantidad de niños")  # Ancho de la mitad de la pantalla
entry_cantidad_ninos.pack(pady=5, fill='x')  # Ocupará la mitad, pero permitirá el llenado

# Ejecutar el bucle principal
ventana.mainloop()