nome = input('Qual o seu nome: ')
if nome == 'Anderson':
    print('Que nome bonito {}!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('{} seu nome é bem popular no Brasul.'.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('{} seu nome é feminino.'.format(nome))
else:
    print('Tenha um bom dia {}!'.format(nome))