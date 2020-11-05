import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCompleter


class GiveIn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1000, 400)
        self.setWindowTitle('Сдача задачи')
        self.name = QLabel(self)
        self.name.setText('<b>Название команды</b>')
        self.name.move(50, 50)

        self.name_input = QLineEdit(self)
        self.name_input.move(250, 50)
        completer = QCompleter(('a', 'x', 'c'), self.name_input)
        self.name_input.setCompleter(completer)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    give = GiveIn()
    give.show()
    sys.exit(app.exec_())