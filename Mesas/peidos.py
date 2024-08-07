from customtkinter import *
import tkinter as tk

def pedidos(numero_mesa):
    try:
        with open(f"Mesa{numero_mesa}.txt", "r") as archivo:
            texto = archivo.readline()
            return texto
    except FileNotFoundError:
        pass # Manejar el error si el archi text_wvo no exist