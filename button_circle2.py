import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(600, 500)
        self.btn = QPushButton(self)
        self.btn.setText('Кнопка')
        self.btn.resize(120, 30)
        self.btn.move(240, 360)
        self.f = False
        self.setWindowTitle('Git и желтые окружности')
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.f = True
        self.repaint()

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        for i in range(15):
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            r = random.randint(20, 80)
            x = random.randint(40, 540)
            y = random.randint(40, 440)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
