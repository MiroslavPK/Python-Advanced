countries = input().split(', ')
capitals = input().split(', ')
couples = zip(countries, capitals)

[print(f'{cnt} -> {capital}') for cnt, capital in couples]

# {print(f'{countries[i]} -> {capitals[i]}') for i in range(len(countries))}
