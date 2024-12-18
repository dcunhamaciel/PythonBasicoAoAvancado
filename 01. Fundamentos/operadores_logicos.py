print(True or False)
print(7 != 3 and 2 > 3)

# Tabela verdade do AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Tabela verdade do OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Tabela verdade do XOR
print(True != True)
print(True != False)
print(False != True)
print(False != False)

# Operador de Negação (unário)
print(not True)
print(not False)
print(not 0)
print(not 1)
print(not -1)

# Cuidado! Operador bit a bit
print(True & False)
print(False | True)
print(True ^ False)

# AND bit a bit
# 3 = 11
# 2 = 10
# _ = 10
print(3 & 2) #2

# OR bit a bit
# 3 = 11
# 2 = 10
# _ = 11
print(3 | 2) #3

# XOR bit a bit
# 3 = 11
# 2 = 10
# _ = 01
print(3 ^ 2) #1

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
print(meta)
