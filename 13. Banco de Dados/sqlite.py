from sqlite3 import connect, ProgrammingError, Row

criar_tabela_grupos = """
    create table if not exists grupos(
        id integer primary key autoincrement,
        descricao varchar(30)
    )
"""

criar_tabela_contatos = """
    create table if not exists contatos(
        id integer primary key autoincrement,
        nome varchar(50),
        tel varchar(40),
        grupo_id int,
        foreign key (grupo_id) references grupos(id)
    )
"""

insert_grupos = 'insert into grupos (descricao) values (?)'
select_grupos = 'select id, descricao from grupos'

insert_contatos = 'insert into contatos (nome, tel, grupo_id) values (?, ?, ?)'
select_contatos =   """
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

try:
    conexao = connect(':memory:')
    conexao.row_factory = Row

    cursor = conexao.cursor()
    cursor.execute(criar_tabela_grupos)
    cursor.execute(criar_tabela_contatos)

    cursor.executemany(insert_grupos, (('Casa', ), ('Trabalho', )))
    cursor.execute(select_grupos)
    grupos = {row['descricao']: row['id'] for row in cursor.fetchall()}

    contatos = (
        ('Arthur', '456', grupos['Casa']),
        ('Paulo', '789', grupos['Casa']),
        ('Ângelo', '000', grupos['Casa']),
        ('Eduardo', '987', grupos['Trabalho']),
        ('Yuri', '654', None),
        ('Leonardo', '321', None)
    )
    cursor.executemany(insert_contatos, contatos)

    cursor.execute(select_contatos)
    for contato in cursor:
        print(contato['nome'], contato['grupo'])
except ProgrammingError as e:
    print(f'Erro: {e.msg}')
