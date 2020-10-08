def age_assignment(*args, **kwargs):
    return {name: v for k, v in kwargs.items() for name in args if name[0] == k}


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
