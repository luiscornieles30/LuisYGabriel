from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from volumen import *

class VentanaPausa(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pausa")
        self.setFixedSize(300, 200)


        boton_continuar = QPushButton("Continuar")
        boton_idioma = QPushButton("Idioma")
        boton_volumen = QPushButton("Volumen")
        boton_salir = QPushButton("Salir")

        layout = QVBoxLayout()
        layout.addWidget(boton_continuar)
        layout.addWidget(boton_idioma)
        layout.addWidget(boton_volumen)
        layout.addWidget(boton_salir)
        self.setLayout(layout)


        boton_continuar.clicked.connect(self.continuar)
        boton_idioma.clicked.connect(self.abrir_idioma)   
        boton_volumen.clicked.connect(self.abrir_volumen)
        boton_salir.clicked.connect(self.salir)
    def continuar(self):
        self.opcion = "continuar"
        self.accept()

    def salir(self):
        self.opcion = "salir"
        self.reject()

    def abrir_volumen(self):
        ventana = Volumen()
        ventana.exec_()  

    def abrir_idioma(self):
        ventana = Idioma()
        ventana.exec_()   

