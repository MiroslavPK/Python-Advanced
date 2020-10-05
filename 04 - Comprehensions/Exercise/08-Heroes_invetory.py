names = input().split(', ')
heroes = {name: {'items': [], 'total_cost': 0} for name in names}

command = input().split('-')
while command[0] != 'End':
    name, item, cost = command
    cost = int(cost)
    if item not in heroes[name]['items']:
        heroes[name]['items'].append(item)
        heroes[name]['total_cost'] += cost

    command = input().split('-')

for name, hero_inventory in heroes.items():
    print(f'{name} -> Items: {len(hero_inventory["items"])}, Cost: {hero_inventory["total_cost"]}')
