from random import randint
import emoji
from math import radians, sin, cos, tan
num = randint(1, 30)
print(emoji.emojize('O número sorteado é {}. :collision:'.format(num), use_aliases=True))

angulo = float(input('Digite o valor de um ângulo: '))
seno = sin(radians(angulo))
print('O SENO do ângulo de {}º é {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O COSSENO do ângulo de {}º é {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('A TANGENTE do ângulo de {}º é {:.2f}'.format(angulo, tangente))
