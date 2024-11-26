import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class GitAndYellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitAndYellowCircles()
    ex.show()
    sys.exit(app.exec())
