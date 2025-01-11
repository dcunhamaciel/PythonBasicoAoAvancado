from db import nova_conexao
from mysql.connector import ProgrammingError

sql =  """
    select
        grupos.descricao as grupo,
        contatos.nome
    from
        grupos
        inner join contatos on contatos.grupo_id = grupos.id
    order by
        grupo,
        nome
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato['grupo']}: {contato['nome']}')
