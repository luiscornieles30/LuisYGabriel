from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

class Volumen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Volumen")
        self.setFixedSize(300, 200)

        boton_volver = QPushButton("Volver")

        layout = QVBoxLayout()
        layout.addWidget(boton_volver)
        self.setLayout(layout)

        boton_volver.clicked.connect(self.reject)
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
class Brillo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Brillo")
        self.setFixedSize(300, 200)

        boton_volver = QPushButton("Volver")

        layout = QVBoxLayout()
        layout.addWidget(boton_volver)
        self.setLayout(layout)

        boton_volver.clicked.connect(self.reject)

