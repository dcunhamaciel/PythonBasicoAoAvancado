from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='masterkey'
)

cursor = conexao.cursor()
cursor.execute('create database if not exists agenda')
