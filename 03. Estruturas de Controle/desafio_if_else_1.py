# Conceitos  Notas
# A          De 10,0 à 9,1
# A-         De 9,0 à 8,1
# B          De 8,0 à 7,1
# B-         De 7,0 à 6,1
# C          De 6,0 à 5,1
# C-         De 5,0 à 4,1
# D          De 4,0 à 3,1
# D-         De 3,0 à 2,1
# E          De 2,0 à 1,1
# E-         De 1,0 à 0,0

# *Para notas maiores que 10 e menores que 0 será impresso "Nota válida"

import sys
import errno

ERRO = '\033[91m'
NORMAL = '\033[0m'

def obter_conceito(nota):
    if nota < 0 or nota > 10:
        return 'Nota Inválida.'

    if nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('É necessário informar a nota.')
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        print(ERRO + 'A nota deve ser um valor numérico.' + NORMAL)
        sys.exit(errno.EINVAL)

    nota = float(sys.argv[1])

    if nota < 0 or nota > 10:
        print(ERRO + 'A nota deve estar entre 0 e 10.' + NORMAL)
        sys.exit(errno.EINVAL)

    print('Conceito: {0}'.format(obter_conceito(nota)))
