import string

with open('text.txt') as file:
    text = file.readlines()

with open('output.txt', 'w') as output_file:
    for row, line in enumerate(text):
        letters_cnt = len([char for char in line if char in string.ascii_letters])
        punctuation_cnt = len([sign for sign in line if sign in string.punctuation])
        output_file.write(f'Line {row + 1}: {line.strip()} ({letters_cnt})({punctuation_cnt})\n')
