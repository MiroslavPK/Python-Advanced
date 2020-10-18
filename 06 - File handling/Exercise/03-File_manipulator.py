import os
import re


def exists_file(command, file_name):
    if command in 'Create, Add':
        with open(file_name, 'w'):
            pass
        return True
    elif command in 'Replace, Delete':
        print('An error occurred')
        return False


while True:
    tokens = input().split('-')
    if tokens[0] == 'End':
        break

    command, file_name = tokens[0], tokens[1]

    if not os.path.exists(file_name):
        if not exists_file(command, file_name):
            continue

    if command == 'Add':
        content = tokens[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        old_string, new_string = tokens[2:]
        with open(file_name, 'r+') as file:
            text = file.read()
            text = re.sub(old_string, new_string, text)
            file.seek(0)
            file.write(text)

    elif command == 'Delete':
        os.remove(file_name)
