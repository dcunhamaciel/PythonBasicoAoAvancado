a = {1, 2, 3}
b = set('codddd3r')

print(type(a))
print(type(b))

print(a)
print(b)

print('3' in b)
print(4 not in b)

print({1, 2, 3} == {3, 2, 1, 3})

c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))
print(c1.intersection(c2))

c1.update(c2)
print(c1)

print(c2 <= c1)
print(c1 >= c2)

print({1, 2, 3} - {2})
print(c1 - c2)

c1 -= {2}
print(c1)
