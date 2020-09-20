phonebook = set()

while True:
    tokens = input()
    if tokens.isdigit():
        break
    name, phone_number = tokens.split('-')
    phonebook.add((name, phone_number))

for _ in range(int(tokens)):
    name = input()
    if not any(name in contact for contact in phonebook):
        print(f'Contact {name} does not exist.')
        continue

    for contact in phonebook:
        if name in contact:
            print(f'{name} -> {contact[1]}')

# simpler but slower solution using dictionary
# phonebook = {}
#
# while True:
#     tokens = input()
#     if tokens.isdigit():
#         break
#     name, phone_number = tokens.split('-')
#     phonebook[name] = phone_number
#
# for _ in range(int(tokens)):
#     name = input()
#     if name not in phonebook:
#         print(f'Contact {name} does not exist.')
#         continue
#     print(f'{name} -> {phonebook[name]}')
