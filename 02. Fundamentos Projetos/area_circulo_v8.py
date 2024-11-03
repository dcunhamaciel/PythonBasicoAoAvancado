from math import pi

def circulo(raio):
    circunferencia = pi * float(raio) ** 2
    print('Circunferência: {0}'.format(circunferencia))

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
