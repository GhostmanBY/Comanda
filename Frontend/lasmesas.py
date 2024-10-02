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

#Crear un Frame con scroll para las mesas

frame_con_scroll = ctk.CTkScrollableFrame(ventana,
                       width=340, height=500)
frame_con_scroll.pack(pady=10,
                      padx=10, fill="both",
                      expand=True)

#Simular varias mesas con botones

for i in range (1, 21):
    #Creamos 20 mesas (puedes agregar mas si es necesario)
    boton_mesa = ctk.CTkButton(frame_con_scroll,
                  text=f"Mesa {i}",width=150,height=80)
    boton_mesa.grid(row=(i-1)//2,column=(i-1)%2,padx=10,pady=10)

#mostrar ventana
ventana.mainloop()