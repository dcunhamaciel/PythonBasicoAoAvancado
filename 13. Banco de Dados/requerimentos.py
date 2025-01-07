try:
    from mysql import connector
except ModuleNotFoundError:
    print('My SQL Connector não instalado!')
else:
    print('MySQL Connector instalado e pronto!')
