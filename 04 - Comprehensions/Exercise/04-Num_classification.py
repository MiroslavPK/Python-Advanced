nums = list(map(int, input().split(', ')))
classifications = {'Positive': [], 'Negative': [], 'Even': [], 'Odd': []}

[classifications['Positive'].append(num) if num >= 0 else classifications['Negative'].append(num) for num in nums]
[classifications['Even'].append(num) if num % 2 == 0 else classifications['Odd'].append(num) for num in nums]

for classification, nums in classifications.items():
    print(f'{classification}: {", ".join(map(str, nums))}')
