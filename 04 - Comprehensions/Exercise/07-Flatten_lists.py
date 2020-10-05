lst = [sublist.split() for sublist in input().split('|')]

flat_lst = [item for items in reversed(lst) for item in items]
print(' '.join(flat_lst))
