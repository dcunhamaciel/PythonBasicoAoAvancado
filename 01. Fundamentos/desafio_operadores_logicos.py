trabalho_terca = True
trabalho_quinta = True
tv_32 = trabalho_terca != trabalho_quinta
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saude = not sorvete

print('Tv32={} Tv50={} Sorvete={} Saudável={}'
    .format(tv_32, tv_50, sorvete, mais_saude))

trabalho_terca = True
trabalho_quinta = False
tv_32 = trabalho_terca != trabalho_quinta
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saude = not sorvete

print('Tv32={} Tv50={} Sorvete={} Saudável={}'
    .format(tv_32, tv_50, sorvete, mais_saude))

trabalho_terca = False
trabalho_quinta = True
tv_32 = trabalho_terca != trabalho_quinta
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saude = not sorvete

print('Tv32={} Tv50={} Sorvete={} Saudável={}'
    .format(tv_32, tv_50, sorvete, mais_saude))

trabalho_terca = False
trabalho_quinta = False
tv_32 = trabalho_terca != trabalho_quinta
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saude = not sorvete

print('Tv32={} Tv50={} Sorvete={} Saudável={}'
    .format(tv_32, tv_50, sorvete, mais_saude))
