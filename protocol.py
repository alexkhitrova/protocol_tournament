import sys
from orm_operations import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QCompleter
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class GiveIn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1000, 400)
        self.setWindowTitle('Сдача задачи')

        self.upload = QPushButton(self)
        self.upload.move(800, 40)
        self.upload.setText('Загрузить команды')
        self.upload.clicked.connect(self.complete)
        #self.upload.clicked.connect(self.make_dict)
        self.upload.clicked.connect(self.upload.hide)

        self.name = QLabel(self)
        self.name.setText('<b>Название команды</b>')
        self.name.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(250, 48)
        self.name_input.textChanged.connect(self.set_enable)

        self.num = QLabel(self)
        self.num.move(50, 100)
        self.num.setText('<b>Номер задачи</b>')
        self.num_input = QLineEdit(self)
        self.num_input.move(250, 98)
        self.num_input.textChanged.connect(self.set_enable)

        self.result = QLabel(self)
        self.result.move(50, 170)
        self.result.setText('<b>Результат</b>')
        self.result_plus = QPushButton(self)
        self.result_plus.setGeometry(250, 145, 70, 70)
        self.result_plus.setText('+')
        self.result_plus.setFont(QFont('Times', 20))
        self.result_plus.clicked.connect(self.plus)
        self.result_minus = QPushButton(self)
        self.result_minus.setGeometry(340, 145, 70, 70)
        self.result_minus.setText('-')
        self.result_minus.setFont(QFont('Times', 20))
        self.result_minus.clicked.connect(self.minus)

    def set_enable(self):
        self.result_plus.setEnabled(True)
        self.result_minus.setEnabled(True)

    def plus(self):
        start_points = point[int(self.num_input.text()) - 1]
        give_point(self.name_input.text(), int(self.num_input.text()), start_points)
        self.result_plus.setEnabled(False)
        self.result_minus.setEnabled(False)

    def minus(self):
        start_points = -1
        give_point(self.name_input.text(), int(self.num_input.text()), start_points)
        self.result_plus.setEnabled(False)
        self.result_minus.setEnabled(False)

    def complete(self):
        completer = QCompleter(teams, self.name_input)
        self.name_input.setCompleter(completer)


   # def make_dict(self):
   #     for i in range(len(teams)):
   #         teams_problems[teams[i]] = {}
   #         teams_problems[teams[i]]['attempts'] = 0
   #         teams_problems[teams[i]]['solved'] = False


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1000, 400)
        self.setWindowTitle('Регистрация')

        self.team_exists = QLabel(self)
        self.team_exists.setText('<b style="color: rgb(250, 55, 55);">Такая команда уже зарегистрирована</b>')
        self.team_exists.move(350, 350)
        self.team_exists.setVisible(False)
        self.invalid_class = QLabel(self)
        self.invalid_class.setText('<b style="color: rgb(250, 55, 55);">Некорректный номер класса</b>')
        self.invalid_class.move(350, 350)
        self.invalid_class.setVisible(False)

        self.name = QLabel(self)
        self.name.setText('<b>Название команды</b>')
        self.name.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(250, 50)
        self.name_input.textChanged.connect(self.check)

        self.people = QLabel(self)
        self.people.setText('<b>Состав команды</b>')
        self.people.move(50, 100)

        self.one = QLabel(self)
        self.one.setText('1: Фамилия, имя')
        self.one.move(250, 100)
        self.one_input = QLineEdit(self)
        self.one_input.move(380, 98)
        self.two = QLabel(self)
        self.two.setText('2: Фамилия, имя')
        self.two.move(250, 150)
        self.two_input = QLineEdit(self)
        self.two_input.move(380, 148)
        self.three = QLabel(self)
        self.three.setText('3: Фамилия, имя')
        self.three.move(250, 200)
        self.three_input = QLineEdit(self)
        self.three_input.move(380, 198)
        self.four = QLabel(self)
        self.four.setText('4: Фамилия, имя')
        self.four.move(250, 250)
        self.four_input = QLineEdit(self)
        self.four_input.move(380, 248)

        self.one_class = QLabel(self)
        self.one_class.setText('Класс')
        self.one_class.move(600, 100)
        self.one_class_input = QLineEdit(self)
        self.one_class_input.move(650, 98)
        self.one_class_input.textChanged.connect(self.check)
        self.two_class = QLabel(self)
        self.two_class.setText('Класс')
        self.two_class.move(600, 150)
        self.two_class_input = QLineEdit(self)
        self.two_class_input.move(650, 148)
        self.two_class_input.textChanged.connect(self.check)
        self.three_class = QLabel(self)
        self.three_class.setText('Класс')
        self.three_class.move(600, 200)
        self.three_class_input = QLineEdit(self)
        self.three_class_input.move(650, 198)
        self.three_class_input.textChanged.connect(self.check)
        self.four_class = QLabel(self)
        self.four_class.setText('Класс')
        self.four_class.move(600, 250)
        self.four_class_input = QLineEdit(self)
        self.four_class_input.move(650, 248)
        self.four_class_input.textChanged.connect(self.check)

        self.ok = QPushButton('OK', self)
        self.ok.clicked.connect(self.team_people)
        self.ok.move(50, 350)

        self.ready = QPushButton('READY', self)
        self.ready.clicked.connect(self.send)
        self.ready.clicked.connect(self.give_in)
        self.ready.clicked.connect(self.hide)
        self.ready.move(850, 350)

    def send(self):
        for i in list(teams_people.keys()):
            teams.append(i)

    def give_in(self):
        give.show()

    def team_people(self):
        teams_people[self.name_input.text()] = ((self.one_input.text(), self.one_class_input.text()),
                                                (self.two_input.text(), self.two_class_input.text()),
                                                (self.three_input.text(), self.three_class_input.text()),
                                                (self.four_input.text(), self.four_class_input.text()))
        people = [self.one_input.text(), self.two_input.text(), self.three_input.text(), self.four_input.text()]
        classes = [self.one_class_input.text(), self.two_class_input.text(), self.three_class_input.text(),
                   self.four_class_input.text()]
        if '-' in people:
            people.remove('-')
        if '-' in classes:
            classes.remove('-')
        register_team(self.name_input.text(), ', '.join(people), ', '.join(classes), max(classes))

        self.name_input.setText('')
        self.one_input.setText('')
        self.one_class_input.setText('')
        self.two_input.setText('')
        self.two_class_input.setText('')
        self.three_input.setText('')
        self.three_class_input.setText('')
        self.four_input.setText('')
        self.four_class_input.setText('')

    def check(self):
        if self.name_input.text() in teams_people.keys():
            self.ok.setEnabled(False)
            self.team_exists.setVisible(True)
            self.invalid_class.setVisible(False)
        elif self.one_class_input.text() not in possible_classes or \
                self.two_class_input.text() not in possible_classes or \
                self.three_class_input.text() not in possible_classes or \
                self.four_class_input.text() not in possible_classes:
            self.ok.setEnabled(False)
            self.invalid_class.setVisible(True)
            self.team_exists.setVisible(False)
        else:
            self.ok.setEnabled(True)
            self.team_exists.setVisible(False)
            self.invalid_class.setVisible(False)

teams_people = {}
teams_problems = {}
possible_classes = ('5', '6', '7', '8', '9', '-')
teams = []
point = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    reg = Registration()
    reg.show()
    give = GiveIn()
    sys.exit(app.exec_())