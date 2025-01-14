from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'insert into contatos (nome, tel) values (%s, %s)'
args = (
    ('Ana', '96765-4321'),
    ('Bia', '97765-4321'),
    ('Luca', '99765-4321'),
    ('Lu', '98765-4321'),
    ('Gui', '98735-4321'),
    ('Beca', '98765-2221'),
    ('Pedro', '98765-6721')
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
