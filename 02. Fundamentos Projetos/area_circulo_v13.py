import sys
from math import pi

def help():
    print('É necessário informar o raio do círculo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0]))

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = float(sys.argv[1])
        circunferencia = circulo(raio)

        print('Circunferência: {0}'.format(circunferencia))
