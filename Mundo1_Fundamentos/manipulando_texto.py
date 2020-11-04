frase = '   Que vivam os loucos de boas cabeças, pois no Mundo em que vivemos não temos motivos para ' \
        'sermos normais.  '
print('1 ->', frase)
n = len(frase) # Armazena a quantidade de caracteres contidos na frase.
print('2 -> A frase contém {} caracteres.'.format(n))
print('3 -> Último caractere da frase: "{}"'.format(frase[n-1])) # Escreve o elemento na posição 10. Lembrando que é contado zero.
print('4 ->', frase[::2]) # Escreve a frase pulando de 2 em 2 caracteres.
print('5 ->', frase[:10]) # Escreve a frase até a posição n-1.
print('6 -> A palavra "cabeça" está iniciando na posição {} da frase.'.format(frase.find('cabeça')))
print('7 -> Existe a palavra "Raul Seixas" na frase? {}'.format('Raul Seixas' in frase))
print('8 -> Existe a palavra "loucos" na frase? {}'.format('loucos' in frase))
print('9 ->', frase.replace('boas cabeças', 'bons pensamentos'))
print('10 ->', frase.upper())
print('11 ->', frase.lower())
print('12 ->', frase.capitalize())
print('13 ->', frase.title())
frase1 = frase.strip()
print('14 -> {}'.format(frase1))
palavras = frase.split()
print('15 -> A frase contém {} palavras.'.format(len(palavras)))
frase2 = '_'.join(palavras)
print('16 ->', frase2)
print('17 -> {}'.format(palavras[3][3]))
print('18 -> A frase contém {} letras'.format(len(frase) - frase.count(' ')))
print('19 -> A primeira palavra tem {} letras.'.format(frase1.find(' ')))
