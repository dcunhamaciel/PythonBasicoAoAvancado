pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}

pessoa['idade'] = 44
pessoa['cursos'].append('JavaScript')

print(pessoa)

pessoa.pop('idade')
print(pessoa)

pessoa.update({'idade': 40, 'sexo': 'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear()
print(pessoa)
