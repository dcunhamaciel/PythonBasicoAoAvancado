# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacci(quantidade, sequencia = (0, 1)):
    return sequencia if len(sequencia) == quantidade else fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == '__main__':
    lista = fibonacci(20)

    for numero in lista:
        print(numero, end=',')
