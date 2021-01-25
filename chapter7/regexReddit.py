import re

text = "match: 42, 1,234, 6,368,745 but not match: 12,34,567, or 1234 and 12,345,67 "

good_values = ['1', '23', '456', '7,890', '89,012', '901,234', '1,234,567', '12,345,678', '123,456,789', '1,234,567,890']
bad_values = ['1234', '12,34,567', '1,1', '12,345,67']

regex = re.compile(r'((\d{1,3}(,\d{3})*))')

mo = regex.findall(text)

print(mo)
"""
for good in good_values:
    match = regex.fullmatch(good)
    if match:
        print(f'{match=}')
for bad in bad_values:
    match = regex.fullmatch(bad)
    if match:
        print(f'uh oh: {match=}')
    else:
        print('no match found')
"""