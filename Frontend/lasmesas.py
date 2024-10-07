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
    mesas_por_fila = 5  # Cantidad de mesas por fila
    
    frame_mesas = ctk.CTkScrollableFrame(ventana, width=900, height=600)  # Scrollable frame para las mesas
    frame_mesas.pack(pady=20, padx=20, fill="both", expand=True)
    
    for i in range(num_mesas):
        fila = i // mesas_por_fila  # Calcular la fila actual
        columna = i % mesas_por_fila  # Calcular la columna actual
        
        boton_mesa = ctk.CTkButton(frame_mesas, text=f"Mesa {i+1}", width=150, height=100)
        boton_mesa.grid(row=fila, column=columna, padx=20, pady=20)

# Llamar a la función para mostrar las mesas
mostrar_mesas()
#Simular varias mesas con botones


#mostrar ventana 
ventana.mainloop()