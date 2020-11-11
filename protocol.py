import sys
from orm_operations import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QCompleter, QMessageBox
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtCore import QCoreApplication, QRegExp


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1000, 400)
        self.setWindowTitle('Регистрация')

        self.team_exists = QLabel(self)
        self.team_exists.setText('<b style="color: rgb(250, 55, 55);">Такая команда уже зарегистрирована</b>')
        self.team_exists.move(370, 350)
        self.team_exists.hide()
        self.name_space = QLabel(self)
        self.name_space.setText('<b style="color: rgb(250, 55, 55);">Введите название команды</b>')
        self.name_space.move(370, 350)
        self.name_space.hide()
        self.noname_person = QLabel(self)
        self.noname_person.setText('<b style="color: rgb(250, 55, 55);">Введите имя участника</b>')
        self.noname_person.move(370, 350)
        self.noname_person.hide()
        self.invalid_class = QLabel(self)
        self.invalid_class.setText('<b style="color: rgb(250, 55, 55);">Некорректный номер класса</b>')
        self.invalid_class.move(370, 350)
        self.invalid_class.hide()

        self.name = QLabel(self)
        self.name.setText('<b>Название команды</b>')
        self.name.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(250, 50)
        self.name_input.textChanged.connect(self.check)
        rx = QRegExp('[\S][\S\s]*')
        validator = QRegExpValidator(rx, self)
        self.name_input.setValidator(validator)
        rx_names = QRegExp('[\D]*')
        validator_names = QRegExpValidator(rx_names, self)
        rx_nums = QRegExp('[\d]*')
        validator_nums = QRegExpValidator(rx_nums, self)

        self.people = QLabel(self)
        self.people.setText('<b>Состав команды</b>')
        self.people.move(50, 100)

        self.one = QLabel(self)
        self.one.setText('1: Фамилия, имя')
        self.one.move(250, 100)
        self.one_input = QLineEdit(self)
        self.one_input.move(380, 98)
        self.one_input.setValidator(validator_names)
        self.one_input.textChanged.connect(self.check)
        self.two = QLabel(self)
        self.two.setText('2: Фамилия, имя')
        self.two.move(250, 150)
        self.two_input = QLineEdit(self)
        self.two_input.move(380, 148)
        self.two_input.setValidator(validator_names)
        self.two_input.textChanged.connect(self.check)
        self.three = QLabel(self)

        self.one_class = QLabel(self)
        self.one_class.setText('Класс')
        self.one_class.move(600, 100)
        self.one_class_input = QLineEdit(self)
        self.one_class_input.move(650, 98)
        self.one_class_input.textChanged.connect(self.check)
        self.one_class_input.setValidator(validator_nums)
        self.two_class = QLabel(self)
        self.two_class.setText('Класс')
        self.two_class.move(600, 150)
        self.two_class_input = QLineEdit(self)
        self.two_class_input.move(650, 148)
        self.two_class_input.textChanged.connect(self.check)
        self.two_class_input.setValidator(validator_nums)
        self.three_class = QLabel(self)

        self.ok = QPushButton('OK', self)
        self.ok.clicked.connect(self.team_people)
        self.ok.move(50, 350)

        self.ready = QPushButton('READY', self)
        self.ready.clicked.connect(self.finish_reg)
        self.ready.move(850, 350)

    def send(self):
        for i in list(teams_people.keys()):
            teams.append(i)

    def give_in(self):
        give.show()

    def team_people(self):
        teams_people[self.name_input.text()] = ((self.one_input.text(), self.one_class_input.text()),
                                                (self.two_input.text(), self.two_class_input.text()))
        people = [self.one_input.text(), self.two_input.text()]
        classes = [self.one_class_input.text(), self.two_class_input.text()]
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

    def check(self):
        self.name_space.hide()
        self.team_exists.hide()
        self.noname_person.hide()
        self.invalid_class.hide()
        if self.name_input.text() == '':
            self.ok.setEnabled(False)
            self.name_space.show()
        elif self.name_input.text() in teams_people.keys():
            self.ok.setEnabled(False)
            self.team_exists.show()
        elif self.one_input.text() == '' or self.two_input.text() == '':
            self.ok.setEnabled(False)
            self.noname_person.show()
        elif self.one_class_input.text() not in possible_classes or \
                self.two_class_input.text() not in possible_classes:
            self.ok.setEnabled(False)
            self.invalid_class.show()
        else:
            self.ok.setEnabled(True)
            self.team_exists.hide()
            self.invalid_class.hide()
            self.name_space.hide()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Вы точно хотите выйти?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def finish_reg(self, event):
        reply = QMessageBox.question(self, 'Message', "Вы точно хотите завершить регистрацию?\n"
                                                      "Количество команд: " + str(len(teams_people.keys())),
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.send()
            self.give_in()
            self.hide()


class GiveIn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1000, 400)
        self.setWindowTitle('Сдача задачи')

        self.already_solved = QLabel(self)
        self.already_solved.setText('<b style="color: rgb(250, 55, 55);">Задача уже решена</b>')
        self.already_solved.move(350, 350)
        self.already_solved.hide()

        self.no_team = QLabel(self)
        self.no_team.setText('<b style="color: rgb(250, 55, 55);">Такой команды нет</b>')
        self.no_team.move(400, 350)

        self.no_problem = QLabel(self)
        self.no_problem.setText('<b style="color: rgb(250, 55, 55);">Такой задачи нет</b>')
        self.no_problem.move(400, 350)
        self.no_problem.hide()

        self.already_solved = QLabel(self)
        self.already_solved.setText('<b style="color: rgb(250, 55, 55);">Эта задача уже решена</b>')
        self.already_solved.move(400, 350)
        self.already_solved.hide()

        self.start = QPushButton(self)
        self.start.setGeometry(750, 40, 230, 60)
        self.start.setText('Начать турнир')
        self.start.setStyleSheet('QPushButton {font-weight: bold; font-size: 14pt; color: green;}')
        self.start.clicked.connect(self.complete)
        self.start.clicked.connect(self.solved)
        self.start.clicked.connect(self.start.hide)

        self.name = QLabel(self)
        self.name.setText('<b>Название команды</b>')
        self.name.move(50, 50)
        self.name_input = QLineEdit(self)
        self.name_input.move(250, 48)
        self.name_input.textChanged.connect(self.check_team)
        rx = QRegExp('[\S][\S\s]*')
        validator = QRegExpValidator(rx, self)
        self.name_input.setValidator(validator)

        self.num = QLabel(self)
        self.num.move(50, 100)
        self.num.setText('<b>Номер задачи</b>')
        self.num_input = QLineEdit(self)
        self.num_input.move(250, 98)
        self.num_input.textChanged.connect(self.check_num)
        rx_num = QRegExp('[\d]*')
        validator = QRegExpValidator(rx_num, self)
        self.num_input.setValidator(validator)

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
        self.disable()

    def check_team(self):
        self.no_problem.hide()
        self.already_solved.hide()
        self.no_problem.hide()
        exists = False
        for team in teams:
            if self.name_input.text() == team:
                exists = True
        if not exists:
            self.no_team.show()
            self.disable()
        else:
            self.no_team.hide()
            if self.name_input.text() == '' or self.num_input.text() == '':
                self.disable()
            else:
                self.enable()

    def check_num(self):
        self.no_team.hide()
        self.already_solved.hide()
        self.no_problem.hide()
        if self.num_input.text() == '' or int(self.num_input.text()) > len(points):
            self.no_problem.show()
            self.disable()
        elif solved[self.name_input.text()][int(self.num_input.text()) - 1]:
            self.already_solved.show()
            self.disable()
        else:
            self.no_problem.hide()
            if self.name_input.text() == '' or self.num_input.text() == '':
                self.disable()
            else:
                self.enable()

    def plus(self):
        final_point = points[int(self.num_input.text()) - 1]
        reply = QMessageBox.question(self, 'Message',
                                     "Поставить + за задачу " + self.num_input.text() + " команде " + self.name_input.text() + "?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            give_point(self.name_input.text(), int(self.num_input.text()), final_point)
            solved[self.name_input.text()][int(self.num_input.text()) - 1] = True
            self.disable()

    def minus(self):
        final_point = -1
        reply = QMessageBox.question(self, 'Message',
                                     "Поставить - за задачу " + self.num_input.text() + " команде " + self.name_input.text() + "?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            give_point(self.name_input.text(), int(self.num_input.text()), final_point)
            self.disable()

    def complete(self):
        completer = QCompleter(teams, self.name_input)
        self.name_input.setCompleter(completer)

    def solved(self):
        for i in teams:
            solved[i] = [False for n in range(len(points))]

    def enable(self):
        self.result_plus.setEnabled(True)
        self.result_minus.setEnabled(True)

    def disable(self):
        self.result_plus.setEnabled(False)
        self.result_minus.setEnabled(False)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Вы точно хотите выйти?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


teams_people = {}
solved = {}
teams = []
points = [1, 1, 2, 2, 3, 3]
possible_classes = ('5', '6', '7', '8', '9', '-')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    reg = Registration()
    reg.show()
    give = GiveIn()
    sys.exit(app.exec_())