num = int(input('Entre com um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O valor em BINÁRIO é: {}'.format(bin(num)[2:]))
elif opcao == 2:
    print('O valor em OCTAL é: {}'.format(oct(num)[2:]))
elif opcao == 3:
    print('O valor em HEXADECIMAL é: {}'.format(hex(num)[:2]))
else:
    print('\033[1;31mOpção inválida!')