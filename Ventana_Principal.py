from customtkinter import *
from tkinter import ttk
import tkinter as tk
import os

from Mesas.peidos import pedidos

def main(codigo):
    def mesa_click(numero_mesa):
        archivo = f"mesa{numero_mesa}.txt"

        directorio = os.path.dirname(os.path.abspath(__file__))

        ruta_archivo = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_archivo):
            archivo_pedido = pedidos(numero_mesa)
            
            recuadro_pedido = tk.Listbox(master= frame_pedido, foreground="white", borderwidth=5)
            recuadro_pedido.place(relx=0.5, rely=0.2, anchor="center")
            
            for i in archivo_pedido:
                recuadro_pedido.insert(tk.END, i)
        else:
            texto_titulo = CTkLabel(master=frame_pedido, text="Menu de pedidos", text_color="white")
            texto_titulo.place(relx=0.5, rely=0.2, anchor="center")
            
            boton_crear_pedido = CTkButton(master=frame_pedido, text="Crear", text_color="white")
            boton_crear_pedido.place(relx=0.5, rely=0.4, anchor="center")

    root = CTk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.title("Comanda")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    
    notebook_principal = ttk.Notebook(root)
    notebook_principal.pack(fill='both', expand=True)

    frame_main_mesas = CTkFrame(notebook_principal, corner_radius=0)
    notebook_principal.add(frame_main_mesas, text="Mesas")
    
    frame_mesas = CTkFrame(master=frame_main_mesas, 
                           fg_color="white", 
                           width=width*0.7, 
                           height=height*0.9, 
                           border_width=5, 
                           border_color="black")
    frame_mesas.place(relx=0.002, rely=0.01)
    frame_mesas.pack_propagate(False)  # Evita que el frame cambie de tamaño

    # Crear un grid de mesas (4x5)
    num_filas = 3
    num_columnas = 4
    for i in range(num_filas):
        for j in range(num_columnas):
            numero_mesa = i * num_columnas + j + 1
            mesa = CTkButton(frame_mesas, 
                             text=f"Mesa {numero_mesa}", 
                             width=208, 
                             height=210, 
                             corner_radius=10,
                             fg_color="#4CAF50",  # Color verde
                             hover_color="#45a049",  # Verde más oscuro al pasar el mouse
                             command=lambda n=numero_mesa: mesa_click(n))
            mesa.grid(row=i, column=j, padx=15, pady=10)

    # Configurar el grid para que se expanda y centre las mesas
    for i in range(num_filas):
        frame_mesas.grid_rowconfigure(i, weight=1)
    for j in range(num_columnas):
        frame_mesas.grid_columnconfigure(j, weight=1)

    frame_pedido = CTkFrame(master=frame_main_mesas,
                            fg_color="#929292",
                            height=height*0.9, 
                            width=width*0.26, 
                            border_width=5,
                            border_color="black")
    frame_pedido.place(relx=0.73, rely=0.01)
    
    
    
    root.mainloop()
    

if __name__ == "__main__":
    main("AOE505")