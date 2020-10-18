import os
from pathlib import Path

print('Please write in "Example" to traverse the given example:')
example_path = input()
sorted_files = {}

for file in os.listdir('Example'):
    _, file_extension = file.split('.')
    if file_extension not in sorted_files:
        sorted_files[file_extension] = []
    sorted_files[file_extension].append(file)

home = str(Path.home())
separator = os.path.sep
path = fr'{home}{separator}Desktop{separator}report.txt'

with open(path, 'w') as report:
    for ext, files in sorted(sorted_files.items()):
        report.write(f'.{ext}\n')
        for file in files:
            report.write(f'- - - {file}\n')
