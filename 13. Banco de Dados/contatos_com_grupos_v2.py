from db import nova_conexao
from mysql.connector import ProgrammingError
from collections import defaultdict

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
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        agrupados = defaultdict(list)
        for contato in contatos:
            agrupados[contato['grupo']].append(contato['nome'])
        print(agrupados)
