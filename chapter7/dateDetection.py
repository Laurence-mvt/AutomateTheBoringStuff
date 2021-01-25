import re

# find all dates in format DD/MM/YYYY
dateRegex = re.compile(r'''(
                            (\d\d)/              # DD/
                            (\d\d)/              # MM/
                            (\d\d\d\d)          # YYYY
                        )''', re.VERBOSE)

text = "it will accept nonexistent dates like 31/02/2020 or 31/04/2021, or 31/09/2021 or 34/05/2021 as well as valid dates like 01/01/2020 and 07/09/1995."

mo = dateRegex.findall(text)

dates = []
for o in mo:
    dates.append(o[0])

# now check for valid dates
toDelete = [] # list of invalid dates to later remove
for index, date in enumerate(dates):
    year = int(date[6:])
    month = int(date[3:5])
    if date[3:5] in ['04', '06', '09', '11']:  # check April, June, September, November have 30 days
        if int(date[:2]) > 30:
            toDelete.append(dates[index]) # later delete that date if over 30 days
    if date[3:5] in ['01', '03', '05', '07', '08', '10', '12']: # check Jan, Mar, May, July, Aug, Oct, Dec have 31 days
        if int(date[:2]) > 31:
            toDelete.append(dates[index]) # delete that date if over 31 days
    if date[3:5] == '02':   # check Feb dates have 28 days or 29 in a leap year:
        # if leap year (Leap years are every year evenly divisible by 4, 
        # except for years evenly divisible by 100, unless the year is also evenly divisible by 400)
        if year % 4 == 0:
            if year % 100 != 0 or year % 400 == 0: # then leap year
                if int(date[:2]) > 29:
                    toDelete.append(dates[index])
            else: # not a leap year
                if int(date[:2]) > 28:
                    toDelete.append(dates[index])

# only keep valid dates
cleanDates = [date for date in dates if date not in toDelete]
print(cleanDates)


