import customtkinter as ctk

#mesas

#Inicializar CustomTkinter
ctk.set_appearance_mode("System")
#Tema del sistema
ctk.set_default_color_theme("blue")
#tema del color
#Crear ventana principal orientada a pantall de celular

ventana = ctk.CTk()
ventana.title("Restaurante")
ventana.geometry("1024x768")

#tamaño tipico del celular

#barra de busqueda (similar a la de google)
entry_busqueda = ctk.CTkEntry(ventana,
                              placeholder_text="Buscar mesa...",width=340)
entry_busqueda.pack(pady=10)


# Función para generar las mesas distribuidas horizontalmente
def mostrar_mesas():
    num_mesas = 30  # Número de mesas
    mesas_por_fila = 7  # Cantidad de mesas por fila
    
    frame_mesas = ctk.CTkScrollableFrame(ventana, width=900, height=600)  # Scrollable frame para las mesas
    frame_mesas.pack(pady=20, padx=20, fill="both", expand=True)
  # Especificar la fuente
    fuente = ctk.CTkFont(family="Segoe UI Black", size=14)  # Definir la fuente
    for i in range(num_mesas):
        fila = i // mesas_por_fila  # Calcular la fila actual
        columna = i % mesas_por_fila  # Calcular la columna actual
        
        boton_mesa = ctk.CTkButton(frame_mesas, 
         text=f"Mesa {i+1}", 
         width=150,
         height=100, 
         fg_color="#FF6103",
         font=fuente,
         hover_color="gray")
        
        boton_mesa.grid(row=fila, column=columna, padx=20, pady=20)


# Función para buscar y mostrar la mesa correspondiente
def buscar_mesa(botones_mesa):
    numero_mesa = entry_busqueda.get()  # Obtener el texto de la barra de búsqueda
    
    # Limpiar el color de todos los botones
    for boton in botones_mesa:
        boton.configure(fg_color="gray")  # Restablecer el color original (gris)
    
    # Resaltar la mesa correspondiente
    if numero_mesa.isdigit():  # Verificar que sea un número
        numero_mesa = int(numero_mesa)
        if 1 <= numero_mesa <= len(botones_mesa):  # Verificar que el número esté dentro del rango
            botones_mesa[numero_mesa - 1].configure(fg_color="green")  # Resaltar la mesa en verde

# Llamar a la función para mostrar las mesas y obtener los botones
botones_mesa = mostrar_mesas()

# Vincular la función de búsqueda al evento de entrada en la barra de búsqueda
entry_busqueda.bind("<Return>", lambda event: buscar_mesa(botones_mesa))

#mostrar ventana 
ventana.mainloop()