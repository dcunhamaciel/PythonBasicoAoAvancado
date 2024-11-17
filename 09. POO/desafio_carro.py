class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        if delta < 0:
            delta = 0

        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta

        self.velocidade_atual = nova if nova <= maxima else maxima

        return self.velocidade_atual

    def frear(self, delta=5):
        if delta < 0:
            delta = 0

        nova = self.velocidade_atual - delta

        self.velocidade_atual = nova if nova > 0 else 0

        return self.velocidade_atual

if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(f'Acererando para: {c1.acelerar(8)}')

    for _ in range(10):
        print(f'Freando para: {c1.frear(delta=20)}')
