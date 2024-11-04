import sys
import errno
from math import pi

def help():
    print('É necessário informar o raio do círculo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0]))

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor numérico.')
        sys.exit(errno.EINVAL)

    raio = float(sys.argv[1])
    circunferencia = circulo(raio)

    print('Circunferência: {0}'.format(circunferencia))
