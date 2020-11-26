frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

# Eliminando o for
'''inverso = '' 
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]'''

print('\033[36m\n>>> {}'.format(junto))
print('<<< {}'.format(inverso))

if junto == inverso:
    print('\033[m\nTemos um palíndromo!')
else:
    print('\033[m\nNão temos um palíndromo!')
