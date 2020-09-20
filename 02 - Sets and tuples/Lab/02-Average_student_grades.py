n = int(input())
students = {}

for _ in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    grades_str = " ".join(map(lambda x: format(x, ".2f"), grades))
    print(f'{student} -> {grades_str} (avg: {(sum(grades) / len(grades)):.2f})')
