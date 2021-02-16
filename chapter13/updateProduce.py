# updateProduce.py - Correct costs in produce sales spreadsheet

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']

# The produce types and their updated prices
PRICE_UPDATES = {'Garlic': 3.07, 
                'Celery': 1.19,
                'Lemon': 1.27}

# TODO: Loop through the rows and update their prices
for row in sheet.rows:
    # if first column is key in PRICE_UPDATES
    if list(row)[0].value in PRICE_UPDATES:
        # update second column with that price
        list(row)[1].value = PRICE_UPDATES[list(row)[0].value]

# Save new spreadsheet as copy
wb.save('productSalesUpdated.xlsx')