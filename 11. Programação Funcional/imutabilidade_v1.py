from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')

# Listas todos os meses do ano com 31 dias
meses = map(lambda mes, dias: {'mes': mes, 'dias': dias}, month_name, mdays)
meses_31 = filter(lambda mes: mes['dias'] == 31, meses)
meses_31_nome = reduce(lambda nomes, mes: nomes + mes['mes'] + ', ', meses_31, '')
print(meses_31_nome)

# Listas todos os meses do ano com 31 dias (professor)
meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_31_nome = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos} \n-{nome_mes}', meses_31_nome, 'Meses com 31 dias:')
print(juntar_meses)
