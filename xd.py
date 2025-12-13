from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from volumen import *
import volumen
from PyQt5.QtGui import QIcon

class VentanaPausa(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pausa")
        self.setFixedSize(300, 200)
        self.setWindowIcon(QIcon("alfin.bmp"))
        self.setStyleSheet("background-color:#1f3b5b; color:white;")


      
        self.boton_continuar = QPushButton()
        self.boton_idioma = QPushButton()
        self.boton_volumen = QPushButton()
        self.boton_salir = QPushButton()

        layout = QVBoxLayout()
        layout.addWidget(self.boton_continuar)
        layout.addWidget(self.boton_idioma)
        layout.addWidget(self.boton_volumen)
        layout.addWidget(self.boton_salir)
        self.setLayout(layout)
        self.boton_volumen.setStyleSheet("font-family:Verdana; background-color:#163355; color:white; padding:6px;")
        self.boton_salir.setStyleSheet("font-family:Verdana; background-color:##163355; color:white; padding:6px;")
        self.boton_continuar.setStyleSheet("font-family:Verdana; background-color:#163355; color:white; padding:6px;")
        self.boton_idioma.setStyleSheet("font-family:Verdana; background-color:#163355; color:white; padding:6px;")

     
        self.boton_continuar.clicked.connect(self.continuar)
        self.boton_idioma.clicked.connect(self.abrir_idioma)
        self.boton_volumen.clicked.connect(self.abrir_volumen)
        self.boton_salir.clicked.connect(self.salir)

       
        self.actualizar_textos()

    def actualizar_textos(self):
        if volumen.idioma_actual == "es":
            self.boton_continuar.setText("Continuar")
            self.boton_idioma.setText("Idioma")
            self.boton_volumen.setText("Volumen")
            self.boton_salir.setText("Salir")
        elif volumen.idioma_actual == "ru":
            self.boton_continuar.setText("Продолжать")
            self.boton_idioma.setText("Язык")
            self.boton_volumen.setText("Объем")
            self.boton_salir.setText("Выходить")
        elif volumen.idioma_actual == "ch":
            self.boton_continuar.setText("繼續")
            self.boton_idioma.setText("語言")
            self.boton_volumen.setText("體積")
            self.boton_salir.setText("出去")
        else:
            self.boton_continuar.setText("Continue")
            self.boton_idioma.setText("Language")
            self.boton_volumen.setText("Volume")
            self.boton_salir.setText("Exit")

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
        self.actualizar_textos() 
