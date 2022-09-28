import openpyxl
import csv

file_name = 'noortrade'
wb = openpyxl.load_workbook(file_name + '.xlsx')
sh = wb.get_active_sheet()
with open(file_name + '.csv', 'w', newline="") as f:
    # open('test.csv', 'w', newline="") for python 3 # open('test.csv', 'wb') as f
    c = csv.writer(f)
    for r in sh.rows:
        c.writerow([cell.value for cell in r])
