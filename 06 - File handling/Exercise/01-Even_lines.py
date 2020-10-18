import re

with open('text.txt') as file:
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            matches = re.findall(r'[-,.?!]', line)
            for symbol in matches:
                line = line.replace(symbol, '@')

            txt = ' '.join(line.split()[::-1])
            print(txt)
