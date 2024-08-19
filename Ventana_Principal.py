from customtkinter import *
from tkinter import ttk
import tkinter as tk
import os

from Mesas.peidos import pedidos

def main(codigo):
    root = CTk()
    screen_height = root.winfo_screenheight()
    taskbar_height = 40
    root.geometry(f"500x{screen_height - taskbar_height}+0+0")

    root.title("Comanda")
    root.resizable(False, True)

    height = root.winfo_screenheight()
    
    notebook_principal = ttk.Notebook(root)
    notebook_principal.pack(fill='both', expand=True)

    frame_main_mesas = CTkFrame(notebook_principal, corner_radius=0)
    notebook_principal.add(frame_main_mesas, text="Mesas") 
    
    frame_pedido = CTkFrame(master=frame_main_mesas,
                            fg_color="#929292",
                            height=height, 
                            width=500, 
                            border_width=5,
                            border_color="black")
    frame_pedido.place(relx=0.5, rely=0.5, anchor="center")
    
    
    
    root.mainloop()
    

if __name__ == "__main__":
    main("AOE505")