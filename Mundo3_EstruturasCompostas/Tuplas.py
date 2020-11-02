# As tuplas são imutáveis
lanche = ('lanche','suco','pizza','pudim')
print('Temos os seguintes lanches: {}'.format(lanche))
print('O lanche na posição 2 é: {}'.format(lanche[2]))

# Fatiamento
print('Lanches nas posições 1 e 2 : {}'.format(lanche[0:2])) # Observe que a posição 2 é desconsiderada.