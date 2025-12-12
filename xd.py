from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
<<<<<<< HEAD
from volumen import *
=======



>>>>>>> fc736ebc9b2e5fdb8dbe384c525937e5292855fc

class VentanaPausa(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pausa")
        self.setFixedSize(300, 200)

<<<<<<< HEAD

=======
>>>>>>> fc736ebc9b2e5fdb8dbe384c525937e5292855fc
        boton_continuar = QPushButton("Continuar")
        boton_idioma = QPushButton("Idioma")
        boton_volumen = QPushButton("Volumen")
        boton_salir = QPushButton("Salir")

        layout = QVBoxLayout()
        layout.addWidget(boton_continuar)
        layout.addWidget(boton_salir)
        layout.addWidget(boton_idioma)
        layout.addWidget(boton_volumen)

        self.setLayout(layout)

<<<<<<< HEAD
        boton_continuar.clicked.connect(self.continuar)
        boton_idioma.clicked.connect(self.accept)   
        boton_volumen.clicked.connect(self.abrir_volumen)
        boton_salir.clicked.connect(self.salir)

    def abrir_volumen(self):
        ventana = xdd()
        ventana.exec_()

    def continuar(self):
        self.opcion = "continuar"
        self.accept()

    def salir(self):
        self.opcion = "salir"
        self.reject()
=======
        boton_continuar.clicked.connect(self.accept)
        boton_idioma.clicked.connect(self.accept)
        boton_volumen.clicked.connect(self.abrir_volumen)  # Abre ventana de volumen
        boton_salir.clicked.connect(self.reject)

    def abrir_volumen(self):
        ventana = VentanaVolumen()
        ventana.exec_()   # Abre la ventana de volumen y espera a que se cierre
>>>>>>> fc736ebc9b2e5fdb8dbe384c525937e5292855fc
