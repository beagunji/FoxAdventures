import pygame
from pygame.locals import *
from sys import exit

image_1 = 'IMAGENS/Garden_sForest/Garden_sForest/background1.png'
image_2 = 'IMAGENS/Garden_sForest/Garden_sForest/background2.png'
image_3 = 'IMAGENS/Garden_sForest/Garden_sForest/background3.png'
image_4 = 'IMAGENS/Garden_sForest/Garden_sForest/background4.png'
image_5 = 'IMAGENS/Garden_sForest/Garden_sForest/frontleaves.png'
image_6 = 'IMAGENS/Garden_sForest/Garden_sForest/pushes.png'
image_7 = 'IMAGENS/Garden_sForest/Garden_sForest/trees.png'


pygame.init()
screen = pygame.display.set_mode((640, 480))

background1 = pygame.image.load(image_1).convert()
background2 = pygame.image.load(image_2).convert()
background3 = pygame.image.load(image_3).convert()
background4 = pygame.image.load(image_4).convert()
background5 = pygame.image.load(image_5).convert()
background6 = pygame.image.load(image_6).convert()
background7 = pygame.image.load(image_7).convert()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(background1, (0,0))
    screen.blit(background2, (0,0))
    screen.blit(background3, (0,0))
    screen.blit(background4, (0,0))
    screen.blit(background5, (0,0))
    screen.blit(background6, (0,0))
    screen.blit(background7, (0,0))
    
    pygame.display.update()




#D:\4oSEMESTRE\JOGOS DIGITAIS\31 AGO\ex3 -  BEATRIZ GUNJI
