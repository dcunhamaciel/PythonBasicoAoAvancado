from functools import reduce

def mdc(numeros):
    minimo = min(numeros)

    for divisor in list(range(1, minimo + 1))[::-1]:
        soma_divisor = reduce(lambda total, numero: total + (numero % divisor), numeros, 0)
        if soma_divisor == 0:
            return divisor

def mdc_professor(numeros):
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 else calc(divisor - 1)

    return calc(min(numeros))

if __name__ == '__main__':
    print(mdc([21, 7]))         # 7
    print(mdc([125, 40]))       # 5
    print(mdc([9, 564, 66, 3])) # 3
    print(mdc([55, 22]))        # 11
    print(mdc([15, 150]))       # 15
    print(mdc([7, 9]))          # 1

    print()

    print(mdc_professor([21, 7]))         # 7
    print(mdc_professor([125, 40]))       # 5
    print(mdc_professor([9, 564, 66, 3])) # 3
    print(mdc_professor([55, 22]))        # 11
    print(mdc_professor([15, 150]))       # 15
    print(mdc_professor([7, 9]))          # 1
