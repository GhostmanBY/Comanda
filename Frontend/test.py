from customtkinter import *


def Cambio_fram(Text):
    texto_label.place_forget()
    campo_label.place_forget()
    boton_cambio.place_forget()
    
    print(f"Texto del entry: {Text}")
    
    text_mozo = CTkLabel(frame_tab_opciones, text="Alta mozo", width=100, height=50)
    text_mozo.place(relx = 0.3, rely= 0.1)
    
    entry_mozo = CTkEntry(frame_tab_opciones, width=100, height=50, placeholder_text="nombre")
    entry_mozo.place(relx = 0.3, rely= 0.2)

    
    
    

root = CTk()
root.geometry("1000x500")

frame_tab_opciones = CTkFrame(root, width=250, height=500)
frame_tab_opciones.place(relx = 0, rely= 0)

texto_label = CTkLabel(frame_tab_opciones, width=100, height=50, text="Mesa 1")
texto_label.place(relx = 0.3, rely= 0.1)

campo_label = CTkEntry(frame_tab_opciones, width=100, height=50, placeholder_text="Comensales")
campo_label.place(relx = 0.3, rely= 0.2)

boton_cambio = CTkButton(frame_tab_opciones, width=100, height=50, text="cambio", command=lambda: Cambio_fram(campo_label.get()))
boton_cambio.place(relx = 0.3, rely= 0.4)

root.mainloop()