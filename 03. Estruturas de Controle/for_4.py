from random import randint

def sortear_dado():
    return randint(1, 6)

for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim!')

for i in range(1, 7):
    if i % 2 == 1:
        continue

    if i == sortear_dado():
        print('Acertou!', i)
        break
else:
    print('Não acertou o número!')
