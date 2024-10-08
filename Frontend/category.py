import customtkinter as ctk

#Desarrollo un menu con las categorias de comida disponibles

class category:
    def ventana (self):
        self.ventana1=ctk.CTk()
        self.ventana1.geometry("1000x800")
        self.ventana1.title("CATEGORIAS")
        self.label1=ctk.CTkLabel()
        self.label1.geometry("999x799")
        self.ventana1.mainloop

categorias=category()        
