import pygsheets
from orm_operations import *

gc = pygsheets.authorize(client_secret='client_secret_391891465960-i956mfi2rjc439c8qtdblkgn6ktuhob2.apps.googleusercontent.com.json')
#gc = pygsheets.authorize()

alphabet = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]

sh = gc.open('Test')
wks = sh.worksheet_by_title("67")
wks.update_value('A1', "Название команды")
wks.update_value('B1', "Баллы за задачи")
wks = sh.worksheet_by_title("89")
wks.update_value('A1', "Название команды")
wks.update_value('B1', "Баллы за задачи")


def update_data(gr, row):
    if gr == 67:
        wks = sh.worksheet_by_title("67")
        wks.update_values('A'+str(row), table(67))

    if gr == 89:
        wks = sh.worksheet_by_title("89")
        wks.update_values('A'+str(row), table(89))
