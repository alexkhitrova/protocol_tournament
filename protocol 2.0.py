import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QCoreApplication


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1000, 400)
        self.setWindowTitle('Регистрация')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration()
    sys.exit(app.exec_())