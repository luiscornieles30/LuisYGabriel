from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

class xdd(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Volumen")
        self.setFixedSize(300, 200)

        boton_volver = QPushButton("Volver")

        layout = QVBoxLayout()
        layout.addWidget(boton_volver)
        self.setLayout(layout)

        boton_volver.clicked.connect(self.reject)
