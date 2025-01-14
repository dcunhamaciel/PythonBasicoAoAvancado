from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'insert into contatos (nome, tel) values (%s, %s)'
args = ('Lucas', '98765-4321')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('1 registro incluído, ID: ', cursor.lastrowid)
