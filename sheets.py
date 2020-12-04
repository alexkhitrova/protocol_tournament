import pygsheets
from orm_operations import *

gc = pygsheets.authorize(client_secret='client_secret_391891465960_i956mfi2rjc439c8qtdblkgn6ktuhob2_apps.json')

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]

sh = gc.open('Протокол')
wks = sh.worksheet_by_title("6-7")
wks.update_value('A1', "Команда")
for i in range(1, 10):
    wks.update_value(alphabet[i]+'1', str(i))
wks.update_value("K1", "Бонус")
wks = sh.worksheet_by_title("8-9")
wks.update_value('A1', "Команда")
for i in range(1, 10):
    wks.update_value(alphabet[i]+'1', str(i))
wks.update_value("K1", "Бонус")



def update_data(gr):
    if gr < 8:
        wks = sh.worksheet_by_title("6-7")
        wks.update_values('A2', table(gr))

    if gr > 7:
        wks = sh.worksheet_by_title("8-9")
        wks.update_values('A2', table(gr))