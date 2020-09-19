parentheses = input()

bracket_couples = {
    '(': ')',
    '[': ']',
    '{': '}'
}

check = []
is_balanced = True

for bracket in parentheses:
    if bracket in '([{':
        check.append(bracket)
        continue

    if not check:
        is_balanced = False
        break

    elif bracket_couples[check.pop()] != bracket:
        is_balanced = False
        break

if is_balanced:
    print('YES')
else:
    print('NO')
