
import pygame
from pygame.locals import * 
from sys import exit


pygame.init()
y = 0
x= 640/2-40/2
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((640,480))
pygame.display.set_caption('Jogo da velha!')


while True:
    relogio.tick(60) # Frame por segundo. Encontrei ótimos resultados usando o time.sleep
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela,(255,0,0),(x,y,40,50))
    y = y+1
    if y >= 640:
        y = 0


    pygame.display.update()