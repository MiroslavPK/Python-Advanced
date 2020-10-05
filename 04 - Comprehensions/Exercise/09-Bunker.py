categories = input().split(', ')
bunker = {category: {'item': []} for category in categories}
n = int(input())
qty = 0
qly = 0

for _ in range(n):
    category, item, specs = input().split(' - ')
    quantity, quality = specs.split(';')
    _, qty_value = quantity.split(':')
    _, qly_value = quality.split(':')
    qty_value = int(qty_value)
    qly_value = int(qly_value)

    bunker[category]['item'].append(item)
    qty += qty_value
    qly += qly_value

print(f'Count of items: {qty}')
print(f'Average quality: {qly/len(categories):.2f}')
for cat, items in bunker.items():
    print(f'{cat} -> {", ".join(items["item"])}')
