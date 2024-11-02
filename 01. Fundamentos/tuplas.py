tupla_1 = tuple()
tupla_2 = ()

print(type(tupla_1))
print(type(tupla_2))

nao_eh_tupla = ('um')
tupla = ('um',)

print(type(nao_eh_tupla))
print(type(tupla))
print(tupla[0])

cores = ('verde', 'amarelo', 'azul', 'branco')

print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))
