# Importando o PyGame
import pygame
import os

# Inicializando o Mixer do PyGame
pygame.mixer.init()

# Gerando a lista de músicas
print('\033[1;36m{} MÚSICAS DISPONÍVEIS {}'.format('-=-'*5, '-=-'*5))
for c in os.listdir():
    if '.wav' in c:
        print(c)
print('-=-'*17, '\033[m')

musica = input('Entre com o nome da música: ')

# Carregando o arquivo MP3 e executando
if os.path.exists(musica):
    pygame.mixer.music.load(musica) #define a música a ser tocada.
    pygame.mixer.music.play() #executa o arquivo de música.
    pygame.mixer.music.set_volume(1)
    input('Digite para parar')
else:
    print('\033[1;31mPossíveis erros:')
    print('>>> O arquivo {} não está no diretório do script Python'.format(musica))
    print('>>> Formato do arquivo não foi informado ".wav"')
