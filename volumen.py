from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSlider
from PyQt5.QtCore import Qt
from pygame import mixer
idioma_actual = "es"



class Volumen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Volumen")
        self.setFixedSize(300, 200)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(200)
        self.slider.setValue(int(mixer.music.get_volume() * 200))

        self.boton_volver = QPushButton()

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.boton_volver)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.cambiar_volumen)

        self.boton_volver.clicked.connect(self.reject)
        self.actualizar_textos()
        

    def cambiar_volumen(self, valor):
        mixer.music.set_volume(valor / 100)
    def actualizar_textos(self):
        if   idioma_actual == "es":
            self.boton_volver.setText("Volver")
        elif idioma_actual == "ru":
            self.boton_volver.setText("Возвращаться")
        elif idioma_actual == "ch":
            self.boton_volver.setText("返回")
        else:
            self.boton_volver.setText("Back")

class Idioma(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Idioma")
        self.setFixedSize(300, 200)

        boton_es = QPushButton("Español")
        boton_en = QPushButton("English")
        boton_ru = QPushButton("русский")
        boton_ch = QPushButton("傳統中文")
        boton_volver = QPushButton("Volver")

        layout = QVBoxLayout()
        layout.addWidget(boton_es)
        layout.addWidget(boton_en)
        layout.addWidget(boton_ru)
        layout.addWidget(boton_ch)
        layout.addWidget(boton_volver)
        self.setLayout(layout)

        boton_es.clicked.connect(self.espanol)
        boton_en.clicked.connect(self.ingles)
        boton_ru.clicked.connect(self.ruso)
        boton_ch.clicked.connect(self.chino)
        boton_volver.clicked.connect(self.reject)

    def espanol(self):
        global idioma_actual
        idioma_actual = "es"
        self.reject()

    def ingles(self):
        global idioma_actual
        idioma_actual = "en"
        self.reject()
    def ruso(self):
        global idioma_actual
        idioma_actual = "ru"
        self.reject()
    def chino(self):
        global idioma_actual
        idioma_actual = "ch"
        self.reject()

