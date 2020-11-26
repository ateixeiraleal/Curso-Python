from datetime import date
ano_atual = date.today().year
nascimento = int(input('Entre com o ano de nascimento: '))
idade = ano_atual - nascimento
print('\033[1;34mQuem nasceu em {} tem \033[1;33m{} anos\033[m \033[1;34m'
      'em {}.\033[m'.format(nascimento, idade, ano_atual))
if idade == 18:
      print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
      print('Fantam {} anos para você se alistar.'.format(18 - idade))
else:
      data_alistamento = ano_atual - idade + 18
      print('Seu alistamento deveria ter ocorrido em {}.'.format(data_alistamento))
      print('Caso você não tenha se alistado, você está {} anos atrasado.'.format(ano_atual - data_alistamento))
