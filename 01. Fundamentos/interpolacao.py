from string import Template

nome, idade = 'Ana', 30

print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {0} Idade: {1}'.format(nome, idade))
print(f'Nome: {nome} Idade: {idade}')

str = Template('Nome: $nome Idade: $idade')
print(str.substitute(nome=nome, idade=idade))
