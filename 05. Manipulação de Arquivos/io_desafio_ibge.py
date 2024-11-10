# Extrair o quarto e nono campos do arquivo CSV
# Ignorar a primeira linha que é o cabeçalho

import csv

with open('desafio_ibge.csv') as arquivo:
    reader = csv.reader(arquivo)

    for linha in reader:
        if reader.line_num == 1:
            continue

        print('Origem: {}, Destino: {}'.format(linha[3], linha[8]))
