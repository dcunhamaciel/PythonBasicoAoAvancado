PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    conjunto_palavras = set(texto.lower().split())
    intersecao = PALAVRAS_PROIBIDAS.intersection(conjunto_palavras)
    if intersecao:
        print('Texto possui pelo menos uma palavra proibida:', intersecao)
    else:
        print('Texto autorizado:', texto)
