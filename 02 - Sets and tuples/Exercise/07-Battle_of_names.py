n = int(input())

odd = set()
even = set()

for i in range(n):
    total = sum(map(ord, input()))
    total //= (i + 1)

    if total % 2 == 0:
        even.add(total)
    else:
        odd.add(total)

if sum(odd) == sum(even):
    final_set = odd | even
elif sum(odd) > sum(even):
    final_set = odd - even
else:
    final_set = odd ^ even

print(', '.join(map(str, final_set)))
