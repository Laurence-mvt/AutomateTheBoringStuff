# readCensusExcel.py - Tabulates population and number of census tracts for each county.

import openpyxl, pprint

print('opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

countyData = {}

# Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # each row has data for one census tract
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value

    # Make sure that the key for this state exists
    countyData.setdefault(state, {})
    # Make sure that the key for this county exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one
    countyData[state][county]['tracts'] += 1
    # Add the population to that county's pop
    countyData[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))     # pprint returns string
resultFile.close()
print('Done.')