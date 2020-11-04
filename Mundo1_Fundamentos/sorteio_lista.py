from random import choice, shuffle
n1 = 'Alisson'
n2 = 'Anderson'
n3 = 'Danielly'
n4 = 'Grasielly'
n5 = 'Otávio'
lista = [n1, n2, n3, n4, n5]
print('O usuário escolhido foi: {}.'.format(choice(lista)))

# Embaralhando a lista de usuários
shuffle(lista)
print('Lista embaralhada: {}'.format(lista))
