casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
maximo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' o valor da prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= maximo:
    print('\033[1;34mEmpréstimo aprovado!')
else:
    print('\033[1;31mEmpréstimo negado!')
    print('O valar máximo por prestação permitido para o seu salário é de R$ {:.2f}.'.format(maximo))
    print('O valor que seria pago por prestação está R$ {:.2f} acima do permitido.'.format(prestacao - maximo))
