#liberias de diseño 
import tkinter as tk
from customtkinter import *
from Ventana_Principal import main

#define una variable para darle los parametros de las letras
letra = "Arial", 30, "bold"

#Funcion que cierra la ventana del login y llama a la ventana principal
def accion(codigo, ventana):
    ventana.destroy() #destruye la ventana
    main(codigo) #llama a la funcion del archivo Ventana_Principal

#crea la ventana del login
root = CTk() #crea la ventana
root.geometry("500x500") #le da la medidas de la misma
root.title("Inicio") #le da un titulo a la ventana

set_appearance_mode("dark") #setea el tema de la aplicacion al tema oscuro

#crea un frame(un recuadro) donde se le da una ubicacion espesifica con tamaño
frame_decorativo = CTkFrame(master=root,width=350, height=350, fg_color="#0E498A") #le da los parametros
frame_decorativo.place(relx=0.5, rely=0.5, anchor="center") #le da la ubicacion al frame

#crea un recuadro de texto
text_1 = CTkLabel(master=frame_decorativo, text="Ingrese su codigo", font=letra) #se le da los parametros
text_1.place(relx=0.5, rely=0.4, anchor="center") #le da la ubicacion al texto

#crea un campo para escribir 
campo_ingreso = CTkEntry(master=frame_decorativo, placeholder_text="AOE505") #le da los parametros
campo_ingreso.place(relx=0.5, rely=0.5, anchor="center") #le da la ubicacion al campo de texto

"""crea un boton y a su vez pasa los parametros 
y en especifico el parametro command= lambda permite que se le pasen valores a la funcion que usa el boton"""
boton_acept = CTkButton(master=frame_decorativo, text="Ingresar", command= lambda: accion(campo_ingreso.get(), root)) 
boton_acept.place(relx=0.5, rely=0.6, anchor="center") #le da la ubicacion al boton

#mantien en un bucle la ventana para que se muestre
root.mainloop()