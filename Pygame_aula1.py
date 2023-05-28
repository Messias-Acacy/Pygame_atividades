import pygame #Eu pessoalmente prefiro importar do pygame tudo por uma questão de simplificação.
from pygame.locals import * # utilize pygame.locals import QUIT apenas para teste 

from sys import exit
pygame.init()# Utilizada para iniciar
tela = pygame.display.set_mode((640,480))
pygame.display.set_caption('Jogo da velha!')


while True: # um jogo é um loop!
    for event in pygame.event.get(): 
        if event.type==QUIT: # se o tipo do event, variavel criada for sair, ele fecha o a janela e encerra o programa.
            pygame.quit()
            exit()
    pygame.display.update() #utilizado para atualizar a tela após cada loop