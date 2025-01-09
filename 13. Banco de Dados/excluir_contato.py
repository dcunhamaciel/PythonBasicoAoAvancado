from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'delete from contatos where nome = %s'
args = ('Lucas', )

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s)')
