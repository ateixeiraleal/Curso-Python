print('\033[4;030;45mOlá, Mundo!\033[m')
print('Olá, programador {}{}{}{}{}!'.format('\033[1;34m', 'Anderson ', '\033[35m', 'Leal', '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'negativo':'\033[7;30m'}
print('Você manda {}MUITO{} bem!!!'.format(cores['negativo'], cores['limpa']))
