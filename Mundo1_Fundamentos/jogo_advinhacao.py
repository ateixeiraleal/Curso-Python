from random import randint
from emoji import emojize
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tende adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(5) # Entra em estado de espera de 5 segundos.
if computador == jogador:
    print(emojize('PARABÉNS!!! Você venceu! :thumbsup:', use_aliases=True))
else:
    print(emojize('Você perdeu! :-1:', use_aliases=True))
    print('Eu pensei no número {}.'.format(computador))
