# csvToExcel - converts alumni csv to excel file (for educational purposes only)

import csv
import openpyxl
from openpyxl.utils import get_column_letter

# open csv file and store results in list of dictionaries
alumFile = open('alumList3.csv')
alumReader = csv.DictReader(alumFile)
alumList = list(alumReader)
alumFile.close()

# open Excel workbook and get sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'New York'

# add headers
headers = alumReader.fieldnames
for i in range(1, len(headers)+1):
    sheet[f'{get_column_letter(i)}1'] = headers[i-1]

# add alumni data
# loop over all alums
rowNum = 2  # first alum's row, after headers
for i, alum in enumerate(alumList[1:]):
    # loop over fields for that alum's row
    for index, header in enumerate(headers):
        sheet[f'{get_column_letter(index+1)}{rowNum}'] = alumList[i][header]
    rowNum += 1

# save workbook
wb.save('/Users/laurencefinch/Desktop/AutomateBoringStuff/alumList3.xlsx')






