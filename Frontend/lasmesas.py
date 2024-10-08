
import customtkinter as ctk

# Inicializar CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Crear ventana principal orientada a pantalla de celular
ventana = ctk.CTk()
ventana.title("Restaurante")
ventana.geometry("1024x768")

# Barra de búsqueda (similar a la de Google)
entry_busqueda = ctk.CTkEntry(ventana, placeholder_text="Buscar mesa...", width=340)
entry_busqueda.pack(pady=10)

# Función para generar las mesas distribuidas horizontalmente
def mostrar_mesas():
    num_mesas = 30  # Número de mesas
    mesas_por_fila = 7  # Cantidad de mesas por fila
    
    frame_mesas = ctk.CTkScrollableFrame(ventana, width=900, height=600)  # Scrollable frame para las mesas
    frame_mesas.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Especificar la fuente
    fuente = ctk.CTkFont(family="Segoe UI Black", size=14)  # Definir la fuente
    botones_mesa = []  # Lista de botones
    
    for i in range(num_mesas):
        fila = i // mesas_por_fila  # Calcular la fila actual
        columna = i % mesas_por_fila  # Calcular la columna actual
        
        boton_mesa = ctk.CTkButton(frame_mesas, 
            text=f"Mesa {i+1}", 
            width=150,
            height=100, 
            fg_color="#FF6103",
            font=fuente,
            hover_color="#fca975")
        
        boton_mesa.grid(row=fila, column=columna, padx=20, pady=20)
        botones_mesa.append(boton_mesa)  # Agregar botón a la lista
    
    return botones_mesa  # Retornar la lista de botones

# Función para buscar y mostrar la mesa correspondiente
def buscar_mesa(botones_mesa):
    numero_mesa = entry_busqueda.get()  # Obtener el texto de la barra de búsqueda
    
    # Limpiar la interfaz de las mesas
    for boton in botones_mesa:
        boton.grid_forget()  # Ocultar todas las mesas
    
    # Verificar el número ingresado
    if numero_mesa.isdigit():  # Verificar que sea un número
        numero_mesa = int(numero_mesa)
        if 1 <= numero_mesa <= len(botones_mesa):  # Verificar que el número esté dentro del rango
            botones_mesa[numero_mesa - 1].grid(row=0, column=0)  # Volver a mostrar solo la mesa seleccionada
            botones_mesa[numero_mesa - 1].configure(fg_color="#FF6103")  # Resaltar la mesa en verde

# Llamar a la función para mostrar las mesas y obtener los botones
botones_mesa = mostrar_mesas()

# Vincular la función de búsqueda al evento de liberar tecla en la barra de búsqueda
entry_busqueda.bind("<KeyRelease>", lambda event: buscar_mesa(botones_mesa))

# Mostrar ventana 
ventana.mainloop()