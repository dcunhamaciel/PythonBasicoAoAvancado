from db import nova_conexao

sql = 'select * from contatos where nome like "%ca%"'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
