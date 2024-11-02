from decimal import Decimal, getcontext

getcontext().prec = 4

print(1.1 + 2.2) # 3.3000000000000003
print(Decimal(1.1) + Decimal(2.2))

print(Decimal.max(Decimal(1), Decimal(7)))
