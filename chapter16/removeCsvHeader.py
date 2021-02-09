#! python3 usr/bin/env bash
# removeCsvHeader.py - removes top line headers from all csv files in the current working directory

import os, csv
from pathlib import Path

os.makedirs('headerRemoved', exist_ok=True)

# Loop throught every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files

    print(f'Removing header from {csvFilename}...')

    # Read the CSV file in (skipping first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file
    outputFileObj = open(Path('headerRemoved')/f'{csvFilename}', 'w', newline="")
    outputWriter = csv.writer(outputFileObj)
    for row in csvRows:
        outputWriter.writerow(row)
    outputFileObj.close()


