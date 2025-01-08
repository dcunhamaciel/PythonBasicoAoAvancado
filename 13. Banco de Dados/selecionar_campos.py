from db import nova_conexao

sql = 'select tel, nome from contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    contatos = cursor.fetchall()

    for contato in contatos:
        print('\t'.join(str(campo) for campo in contato))
