num = int(input('Digite um número para ver sua tabuada: '))
print('=' * 12) # Utilizando o operador de multiplicação para replicar string.
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
print('=' * 12)
