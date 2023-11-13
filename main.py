import sys

from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
from PyQt5 import uic


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 800)

        self.circles = []

        self.pushButton.clicked.connect(self.new_circle)

    def new_circle(self):
        r = randint(0, 100)
        self.circles.append((randint(0, 1000), randint(0, 1000), r, r))

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for cir in self.circles:
            qp.drawEllipse(*cir)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec_()
