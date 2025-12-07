from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *


class FinalWin(QWidget):
   def __init__(self):
       ''' la ventana en donde se realizan las preguntas '''
       super().__init__()


       # creando y configurando elementos gráficos
       self.initUI()


       # establece la apariencia de la ventana (etiqueta, tamaño, ubicación)
       self.set_appear()
      
       # inicio:
       self.show()


   def initUI(self):
       ''' crea elementos gráficos '''
       self.workh_text = QLabel(txt_workheart)
       self.index_text = QLabel(txt_index)


       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)        
       self.setLayout(self.layout_line)


   ''' establece la apariencia de la ventana (etiqueta, tamaño, ubicación) '''
   def set_appear(self):
       self.setWindowTitle(txt_finalwin)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)


