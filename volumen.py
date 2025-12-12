from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

<<<<<<< HEAD
class xdd(QDialog):
=======
class VentanaVolumen(QDialog):
>>>>>>> fc736ebc9b2e5fdb8dbe384c525937e5292855fc
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Volumen")
        self.setFixedSize(300, 200)

        boton_volver = QPushButton("Volver")

        layout = QVBoxLayout()
        layout.addWidget(boton_volver)
        self.setLayout(layout)

        boton_volver.clicked.connect(self.reject)
<<<<<<< HEAD
=======

>>>>>>> fc736ebc9b2e5fdb8dbe384c525937e5292855fc
