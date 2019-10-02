import itertools

a = itertools.product('1234', repeat=3)

for aa in a:
    print(aa)

print(a)
