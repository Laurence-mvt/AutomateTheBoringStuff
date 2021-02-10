#! python3 usr/bin/env bash
# Notes on chapter 16 - CSV and JSON

import csv

# to read csvs, need to use a reader object, to enable iterating over lines in csv file

import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile) # note must pass an open file to csv.reader, not a filepath/file
exampleData = list(exampleReader) # a list of lists, each sublist is a row in csv file, each sub-list element is a cell 
exampleData
exampleFile.close()


exampleData[0][2]

# for large CSV files, use the reader in a for loop to avoid loading entire file into memory
for row in exampleReader:
    print(f'Row # {exampleReader.line_num} {str(row)}' )
# note can only be looped over once, need to create another csv reader object if rereading

# user writer object to write to a CSV
outputFile = open('output.csv', 'w', newline="")
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']) # returns 21 (i.e number of characters)
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']) # 32
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

# for csv files with header rows, often more convenient to user DictReader and DictWriter
exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile) # returns DictReader object which is like a list of dictionaries, where keys are the headings
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
exampleFile.close()

# when CSV file has no headers, can create some to be used as keys with dict reader
exampleFile = open('example.csv') # no headers
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])
exampleFile.close()

# use dictionaries to write files
outputFile = open('output.csv', 'w', newline="")
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader() # to include headers
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'}) # missing keys will be empty in the created csv file
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':'dog'})
outputFile.close()

# JSON data a common data format for APIs
# JSON can only store values of data types: strings, integers, floats, Booleans, lists, dictionaries, and NoneType
# can't represent Python-specific objects like File objects, CSV reader or writer objections, Regex objects, or Selenium WebElement objects

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}' 
# note JSON strings always use double quotes
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)    # .loads() is read 'load string', not 'loads'
jsonDataAsPythonValue   # returns as dictionary: {"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}

# write a JSON formatted string with json.dumps(), meaning 'dump string', not 'dumps'
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)  # '{"isCat": True ... "felineIQ": None}, although key-value pairs are unordered

