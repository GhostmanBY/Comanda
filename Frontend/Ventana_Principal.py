'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

numero_de_mesas = [f"Mesa{i+1}" for i in range(5)]

def funciona_mesas(mesa):
    print(f"mesa número {mesa[4]}")

def main(codigo):
    app = QApplication(sys.argv)

    # Crear la ventana principal
    window = QMainWindow()
    window.setWindowTitle("Como ser gay")
    screen_height = app.desktop().screenGeometry().height()
    taskbar_height = 80
    window.setGeometry(0, 0, 500, screen_height - taskbar_height)
    
    # Crear el widget central y su layout
    central_widget = QWidget()
    layout = QVBoxLayout()
    central_widget.setLayout(layout)
    window.setCentralWidget(central_widget)
    
    # Crear y agregar el QComboBox al layout
    combo_box = QComboBox()
    combo_box.addItems(numero_de_mesas)
    combo_box.setFixedWidth(350)  # Ajustar el ancho del QComboBox
    combo_box.setStyleSheet("font-size: 16px;")  # Cambiar el estilo del combo box
    layout.addWidget(combo_box, alignment=Qt.AlignCenter)
    
    # Crear y agregar el botón al layout
    button = QPushButton("ok")
    button.setFixedSize(50,30)#(x,y)
    button.setStyleSheet("font-size: 25px;")
    button.clicked.connect(lambda: funciona_mesas(combo_box.currentText()))
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main("AOE505")
'''
from customtkinter import *

def ventana2():
    root2=CTk()
    root2.title("MESAS")
    root2.geometry("400x400")
    root2.configure(fg_color="white")
    mesas = ["MESA 01", "MESA 02", "MESA 03"]

    menu_desplegable = CTkComboBox(root2, values=mesas,fg_color="#FF6103",border_color="#FF6103")
    menu_desplegable.place(rely=0.1,relx=0.3)

    boton1=CTkButton(root2,text="CONTINUAR",fg_color="#FF6103")
    boton1.place(rely=0.7,relx=0.3)

    root2.mainloop()