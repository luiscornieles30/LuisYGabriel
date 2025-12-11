from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout



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
        layout.addWidget(boton_salir)
        layout.addWidget(boton_idioma)
        layout.addWidget(boton_volumen)

        self.setLayout(layout)

        boton_continuar.clicked.connect(self.accept)
        boton_idioma.clicked.connect(self.accept)
        boton_volumen.clicked.connect(self.accept)
        boton_salir.clicked.connect(self.reject)
