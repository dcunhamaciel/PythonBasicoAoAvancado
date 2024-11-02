#print(dir(int))
#print(dir(float))

a = 5
b = 2.5

print(type(a))
print(type(b))

print(type(a + b))
print(type(a - b))
print(type(a * b))
print(type(a / b))

print(b.is_integer())
print(5.0.is_integer())

print(int.__add__(2, 3))
print(int.__abs__(-2))
print((-2).__abs__())

print((-3.6).__abs__())
print(abs(-3.6))
