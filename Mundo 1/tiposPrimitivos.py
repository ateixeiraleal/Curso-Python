n1 = input('Digite um número: ')
n2 = (input('Digite outro número: '))
s = n1 + n2
print('A contatenação dos valore é: {}'.format(s))
n1 = int(n1)
n2 = int(n2)
s = n1 + n2
print('A soma de {} e {} = {}'.format(n1, n2, s))

n3 = float(input('Digite um número real: '))
s = s + n3
print('Soma = {}'.format(s))

boolean = bool(input('As somas estão corretas? ')) # "True" ou "False"
print(boolean)

texto = str(input('Digite uma frase: ')) # Se o tipo primitivo não for informado, sempre será String.
print(texto)

print('Tipo primitivo da variável n1: {}'.format(type(n1))) # "type" imprimo o tipo da variável.
print('Tipo primitivo da variável n3: {}'.format(type(n3)))
print('Tipo primitivo da variável texto: {}'.format(type(texto)))
print('Tipo primitivo da variável boolean: {}'.format(type(boolean)))

print('A variável texto é numérica? {}'.format(texto.isupper())) # Tem várias opções de is.
