from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QSlider
from PyQt5.QtCore import Qt
from pygame import mixer


class Volumen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Volumen")
        self.setFixedSize(300, 200)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(200)
        self.slider.setValue(int(mixer.music.get_volume() * 200))

        boton_volver = QPushButton("Volver")

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(boton_volver)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.cambiar_volumen)

        boton_volver.clicked.connect(self.reject)

    def cambiar_volumen(self, valor):
        mixer.music.set_volume(valor / 100)
class Idioma(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Idioma")
        self.setFixedSize(300, 200)

        boton_volver = QPushButton("Volver")

        layout = QVBoxLayout()
        layout.addWidget(boton_volver)
        self.setLayout(layout)

        boton_volver.clicked.connect(self.reject)
