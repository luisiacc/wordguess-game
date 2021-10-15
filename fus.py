from PyQt5.QtWidgets import *
import qdarkstyle


class wid(QWidget):
    def __init__(self):
        super(wid, self).__init__()

        but = QPushButton('Perfect')
        lay = QVBoxLayout()
        lay.addWidget(but)
        self.setLayout(lay)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    n = wid()
    app.exec_()
