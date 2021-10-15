# Requerimientos :
# - Python 3.6+
# - PyQt5

from PyQt5.QtWidgets import (QApplication, QWidget, QProxyStyle, QPushButton, QHBoxLayout,
QVBoxLayout)
from PyQt5.QtCore import QRect, Qt
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(QRect(400, 500, 500, 500))
        self.setWindowTitle('Test')

        self.yellowB = QPushButton('Yellow', pressed=lambda:self.setBackground('yellow'))
        self.RedB = QPushButton('Red', pressed=lambda:self.setBackground('red'))
        self.GreenB = QPushButton('Green', pressed=lambda:self.setBackground('green'))

        self.lay = QHBoxLayout (self)
        self.lay.addWidget(self.yellowB, alignment=Qt.AlignTop)
        self.lay.addWidget(self.GreenB, alignment=Qt.AlignTop)
        self.lay.addWidget(self.RedB, alignment=Qt.AlignTop)

    def setBackground(self, color):
        self.setStyleSheet(f'background: {color}')

if __name__ == '__main__':
    app = QApplication([sys.argv])
    app.setStyle(QProxyStyle('Fusion'))
    w = Window()
    w.show()
    app.exec_()
