import pandas as pd

#df = pd.DataFrame({'1': (('', '6'), ('', '6'), ('', '6'), ('', '6')), '4': (('', '6'), ('', '7'), ('', '6'), ('', '-'))})
#df.to_excel('C:/Users/Alexandra/PycharmProjects/protocol/try.xlsx')
import openpyxl
dct = {'1': (('', '6'), ('', '6'), ('', '6'), ('', '6')), '4': (('', '6'), ('', '7'), ('', '6'), ('', '-'))}
wb = openpyxl.load_workbook(filename='C:/Users/Alexandra/PycharmProjects/protocol/try.xlsx')
sheet = wb['test']
i = 1
for rec in (0, 1):
    sheet.cell(row=i, column=2).value = rec
    i += 1
wb.save('C:/Users/Alexandra/PycharmProjects/protocol/try.xlsx')