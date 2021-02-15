#! usr/bin/env bash python3 

# This book uses version 2.6.2 of OpenPyXL. 
# It’s important that you install this version by running pip install --user -U openpyxl==2.6.2 
# because newer versions of OpenPyXL are incompatible with the information in this book. 

import openpyxl

wb = openpyxl.load_workbook('example.xlsx') 
type(wb)    # <class 'openpyxl.workbook.workbook.Workbook'>