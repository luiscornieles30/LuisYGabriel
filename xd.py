from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout



class VentanaPausa(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pausa")
        self.setFixedSize(300, 200)

        boton_continuar = QPushButton("Continuar")
        boton_salir = QPushButton("Salir")

        layout = QVBoxLayout()
        layout.addWidget(boton_continuar)
        layout.addWidget(boton_salir)

        self.setLayout(layout)

        boton_continuar.clicked.connect(self.accept)
        boton_salir.clicked.connect(self.reject)
