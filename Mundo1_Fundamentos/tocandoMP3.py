import pygame
pygame.init() #inicializa o pygame.
pygame.mixer.music.load('sextou.mp3') #define a música a ser tocada.
pygame.mixer.music.play() #executa o arquivo de música.
pygame.event.wait() #espera o evento terminar para encerrar o programa.
