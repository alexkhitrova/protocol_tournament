import pygsheets
from orm_operations import *

gc = pygsheets.authorize(client_secret='client_secret_391891465960-i956mfi2rjc439c8qtdblkgn6ktuhob2.apps.googleusercontent.com.json')
#gc = pygsheets.authorize()

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]

sh = gc.open('Test')
wks = sh.worksheet_by_title("67")
wks.update_value('A1', "Команда")
for i in range(1, 10):
    wks.update_value(alphabet[i]+'1', str(i))
wks.update_value("H1", "Бонусная задача")
wks = sh.worksheet_by_title("89")
wks.update_value('A1', "Команда")
for i in range(1, 10):
    wks.update_value(alphabet[i]+'1', str(i))
wks.update_value("H1", "Бонусная задача")


def update_data(gr, row):
    if gr < 8:
        wks = sh.worksheet_by_title("67")
        wks.update_values('A'+str(row), table(gr))

    if gr > 7:
        wks = sh.worksheet_by_title("89")
        wks.update_values('A'+str(row), table(gr))
