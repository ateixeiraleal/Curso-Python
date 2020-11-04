n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}.'.format(n, t, n, r))

print('>>> Outra forma <<<')
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.'.format(n, (n*3)))
print('A raiz quadrada de {} vale {:.2f}.'.format(n, pow(n, (1/2))))
