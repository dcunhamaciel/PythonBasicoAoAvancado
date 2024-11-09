# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def fibonacci(limite):
    resultado = [0, 1]

    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))

    return resultado

if __name__ == '__main__':
    lista = fibonacci(10000)

    for numero in lista:
        print(numero, end=',')
