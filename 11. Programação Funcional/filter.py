pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

menores = filter(lambda pessoa: pessoa['idade'] < 18, pessoas)
print(list(menores))

nomes_grandes = filter(lambda pessoa: len(pessoa['nome']) > 6, pessoas)
print(list(nomes_grandes))
