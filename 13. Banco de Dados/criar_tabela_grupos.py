from db import nova_conexao
from mysql.connector import ProgrammingError

criar_tabela_grupos = """
    create table if not exists grupos(
        id int auto_increment primary key,
        descricao varchar(30)
    )
"""

alterar_tabela_contatos_1 = """
    alter table contatos add grupo_id int
"""

alterar_tabela_contatos_2 = """
    alter table contatos add foreign key (grupo_id)
        references grupos(id)
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(criar_tabela_grupos)
        cursor.execute(alterar_tabela_contatos_1)
        cursor.execute(alterar_tabela_contatos_2)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
