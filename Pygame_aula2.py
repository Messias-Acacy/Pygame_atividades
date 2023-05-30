import pygame
from pygame.locals import * 
from sys import exit


pygame.init()

tela = pygame.display.set_mode((640,480))
pygame.display.set_caption('Jogo da velha!')


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    # a posição zero chama a variavel, a posição 1 chamma a cor, a posição 2 chama a posição x, y, a largura e a altura
    #ler a documentação 
    pygame.draw.rect(tela,(255,0,0),(200,300,40,50))
    pygame.draw.circle(tela,(255,255,0),(300,260), 40)
    pygame.draw.line(tela,(255,0,0),(100,90),(100,150),5) 


    pygame.display.update()
