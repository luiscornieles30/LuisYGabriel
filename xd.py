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
<<<<<<< HEAD
        boton_brillo = QPushButton("Brillo")
=======
>>>>>>> 2c18364ba75c5290fe50e622b5249efdb0d6b478
        boton_salir = QPushButton("Salir")

        layout = QVBoxLayout()
        layout.addWidget(boton_continuar)
<<<<<<< HEAD
        layout.addWidget(boton_idioma)
        layout.addWidget(boton_volumen)
        layout.addWidget(boton_brillo)
        layout.addWidget(boton_salir)
=======
        layout.addWidget(boton_salir)
        layout.addWidget(boton_idioma)
        layout.addWidget(boton_volumen)
>>>>>>> 2c18364ba75c5290fe50e622b5249efdb0d6b478

        self.setLayout(layout)


        boton_continuar.clicked.connect(self.continuar)
        boton_idioma.clicked.connect(self.abrir_idioma)   
        boton_volumen.clicked.connect(self.abrir_volumen)
<<<<<<< HEAD
        boton_brillo.clicked.connect(self.abrir_brillo)
        boton_salir.clicked.connect(self.salir)

=======
        boton_salir.clicked.connect(self.salir)

    def abrir_volumen(self):
        ventana = xdd()
        ventana.exec_()
>>>>>>> 2c18364ba75c5290fe50e622b5249efdb0d6b478

    def continuar(self):
        self.opcion = "continuar"
        self.accept()

    def salir(self):
        self.opcion = "salir"
        self.reject()

<<<<<<< HEAD
    def abrir_volumen(self):
        ventana = Volumen()
        ventana.exec_()  

    def abrir_idioma(self):
        ventana = Idioma()
        ventana.exec_()   

    def abrir_brillo(self):
        ventana = Brillo()
        ventana.exec_()


=======
        boton_continuar.clicked.connect(self.accept)
        boton_idioma.clicked.connect(self.accept)
        boton_volumen.clicked.connect(self.abrir_volumen) 
        boton_salir.clicked.connect(self.reject)

    def abrir_volumen(self):
        ventana = VentanaVolumen()
        ventana.exec_()  

    def abrir_idioma(self):
        ventana = Ventanaidioma()
        ventana.exec_()   

>>>>>>> 2c18364ba75c5290fe50e622b5249efdb0d6b478
