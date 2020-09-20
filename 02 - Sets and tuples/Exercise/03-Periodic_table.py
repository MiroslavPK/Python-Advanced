n = int(input())

elements = set()

for _ in range(n):
    chemical_compounds = input().split()
    while chemical_compounds:
        elements.add(chemical_compounds.pop())

print('\n'.join(elements))
