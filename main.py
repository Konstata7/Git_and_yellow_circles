import sys

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow


class GitAndYellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.drawn = False

    def button_clicked(self):
        from random import randrange
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(255, 247, 0))
        painter.setPen(pen)

        painter.drawEllipse(21, 101, randrange(22, 780), randrange(102, 681))
        painter.end()
        self.drawn = True
        self.label.setPixmap(canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitAndYellowCircles()
    ex.show()
    sys.exit(app.exec())
