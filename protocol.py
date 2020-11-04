import sys
import openpyxl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import QCoreApplication


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
        self.two_class = QLabel(self)
        self.two_class.setText('Класс')
        self.two_class.move(600, 150)
        self.two_class_input = QLineEdit(self)
        self.two_class_input.move(650, 148)
        self.three_class = QLabel(self)
        self.three_class.setText('Класс')
        self.three_class.move(600, 200)
        self.three_class_input = QLineEdit(self)
        self.three_class_input.move(650, 198)
        self.four_class = QLabel(self)
        self.four_class.setText('Класс')
        self.four_class.move(600, 250)
        self.four_class_input = QLineEdit(self)
        self.four_class_input.move(650, 248)


        self.ok = QPushButton('OK', self)
        self.ok.clicked.connect(self.team_people)
        self.ok.move(50, 350)

        self.ready = QPushButton('READY', self)
        self.ready.clicked.connect(self.lst_teams)
        self.ready.clicked.connect(QCoreApplication.instance().quit)
        self.ready.move(850, 350)

        self.name_input.textChanged.connect(self.check)
        self.one_class_input.textChanged.connect(self.check)
        self.two_class_input.textChanged.connect(self.check)
        self.three_class_input.textChanged.connect(self.check)
        self.four_class_input.textChanged.connect(self.check)

        self.show()

    def team_people(self):
        teams_people[self.name_input.text()] = ((self.one_input.text(), self.one_class_input.text()),
                                                (self.two_input.text(), self.two_class_input.text()),
                                                (self.three_input.text(), self.three_class_input.text()),
                                                (self.four_input.text(), self.four_class_input.text()))
        self.name_input.setText('')
        self.one_input.setText('')
        self.one_class_input.setText('')
        self.two_input.setText('')
        self.two_class_input.setText('')
        self.three_input.setText('')
        self.three_class_input.setText('')
        self.four_input.setText('')
        self.four_class_input.setText('')

    def lst_teams(self):
        print(teams_people)

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


#def registrated_to_table():
#    wb = openpyxl.load_workbook(filename='C:/Users/Alexandra/PycharmProjects/protocol/6-7.xlsx')
#    sheet = wb['6-7']
#    i = 2
#    for name in teams_people.keys():
#        sheet.cell(row=i, column=1).value = name
#        i += 1
#    wb.save('C:/Users/Alexandra/PycharmProjects/protocol/6-7.xlsx')


teams_people = {}
possible_classes = ('6', '7', '8', '9', '-')

#registrated_to_table()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration()
    sys.exit(app.exec_())