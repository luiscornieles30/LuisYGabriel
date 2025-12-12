from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

<<<<<<< HEAD
class VentanaIdioma(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Idiomas")
=======
class VentanaVolumen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Volumen")
>>>>>>> cf849eccece8ffe04674ea6ee651878e69ee324e
        self.setFixedSize(300, 200)

        boton_volver = QPushButton("Volver")

        layout = QVBoxLayout()
        layout.addWidget(boton_volver)
        self.setLayout(layout)

        boton_volver.clicked.connect(self.reject)
