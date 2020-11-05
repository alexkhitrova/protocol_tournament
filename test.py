import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QCompleter
from PyQt5.QtGui import QFont

class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1000, 400)
        self.setWindowTitle('Регистрация')
        self.name = QLabel(self)
        self.name.setText('<b>Название команды</b>')
        self.name.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(250, 50)

        self.ok = QPushButton('OK', self)
        self.ok.clicked.connect(self.ok_f)
        self.ok.move(50, 350)

    def ok_f(self):
        print(type(self.name_input.text()))
        print(type(int(self.name_input.text())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    reg = Registration()
    reg.show()
    sys.exit(app.exec_())