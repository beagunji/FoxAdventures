#----------FOX ADVENTURES----------
#Giovana Gomes Leal - TIA: 32219431
#Beatriz Hitomi Gunji - TIA: 32248024


import pygame
from pygame.locals import *
from sys import exit 
import os
from random import randrange, choice
import random
import math

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fox Adventures")

WHITE = (255, 255, 255)


BASE_PATH = os.path.dirname(__file__)
IMAGEM_PATH = os.path.join(BASE_PATH, "IMAGENS")
MUSICA_PATH = os.path.join(BASE_PATH, 'MUSICA')

sprite_sheet = pygame.image.load(os.path.join(IMAGEM_PATH, 'sequencia_Nivel1.png')).convert_alpha()


som_colisao = pygame.mixer.Sound(os.path.join(MUSICA_PATH, 'colisao.wav'))
som_colisao.set_volume(1)


bateu = False

escolher_obstaculo = choice([0, 0])

pontos = 0

velocidade_jogo = 20


sorvete_image = pygame.image.load(os.path.join(IMAGEM_PATH,'IceCream.png'))
       
class IceCream(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sorvete_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -10)
        self.speed_y = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(-100, -10)
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.speed_y = random.randint(1, 5)


ice_cream_sprites = pygame.sprite.Group()

#instanciar sorvetes
for _ in range(10):
    ice_cream = IceCream()
    ice_cream_sprites.add(ice_cream)



def exibir_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}' 
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def reiniciar_jogo():
    global pontos, velocidade_jogo, bateu, escolher_obstaculo
    pontos = 0
    velocidade_jogo = 10
    bateu = False
    fox.rect.y = HEIGHT - 64 - 96//2
    fox.pulo = False
    fox_pulador.rect.x = WIDTH
    tronco.rect.x = WIDTH
    escolher_obstaculo = choice([0, 0])

class Fox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(MUSICA_PATH, 'catch.mp3'))
        self.som_pulo.set_volume(1)
        self.imagens_fox = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 25,0), (25,23))
            img = pygame.transform.scale(img, (25*3, 23*3))
            self.imagens_fox.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_fox[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = HEIGHT - 64 - 96//2
        self.rect.topleft = (100, self.pos_y_inicial) 
        self.pulo = False
        

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):

        if self.pulo == True:
            if self.rect.y <= self.pos_y_inicial - 150:
                self.pulo = False
            self.rect.y -= 15

        else:
            if self.rect.y >= self.pos_y_inicial:
                self.rect.y = self.pos_y_inicial
            else:
                self.rect.y += 15
        
 
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_fox[int(self.index_lista)]




class Tronco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*25, 0), (25,23))
        self.image = pygame.transform.scale(self.image, (25*2, 23*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolher_obstaculo
        self.rect.center = (WIDTH,  HEIGHT - 64)
        self.rect.x = WIDTH

    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = WIDTH
            self.rect.x -= velocidade_jogo



class FoxPulador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_fox = []
        for i in range(2,4):
            img = sprite_sheet.subsurface((i*25, 0), (25,23))
            img = pygame.transform.scale(img, (25*3, 23*3))
            self.imagens_fox.append(img)

        self.index_lista = 0
        self.image = self.imagens_fox[self.index_lista]
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolher_obstaculo
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH, 300)
        self.rect.x = WIDTH

    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = WIDTH
            self.rect.x -= velocidade_jogo

            if self.index_lista > 1:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagens_fox[int(self.index_lista)]


tudo_sprites = pygame.sprite.Group()
fox = Fox()
tudo_sprites.add(fox)

tronco = Tronco()
tudo_sprites.add(tronco)

fox_pulador = FoxPulador()
tudo_sprites.add(fox_pulador)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(tronco)
grupo_obstaculos.add(fox_pulador)



score = 0


clock = pygame.time.Clock()
while True:
    #clock.tick(30)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and bateu == False:
                if fox.rect.y != fox.pos_y_inicial:
                    pass
                else:
                    fox.pular()
                    
            if event.key == K_r and bateu == True:
                reiniciar_jogo()

            
    tudo_sprites.draw(screen)

    colisoes = pygame.sprite.spritecollide(fox, grupo_obstaculos, False, pygame.sprite.collide_mask)

    tudo_sprites.draw(screen)

    if tronco.rect.topright[0] <= 0 or fox_pulador.rect.topright[0] <= 0:
        escolher_obstaculo = choice([0, 0])
        tronco.rect.x = WIDTH
        fox_pulador.rect.x = WIDTH
        tronco.escolha = escolher_obstaculo
        fox_pulador.escolha = escolher_obstaculo

    if colisoes and bateu == False:
        som_colisao.play()
        bateu = True

    if bateu == True:
        if pontos % 100 == 0:
            pontos += 1
        game_over = exibir_mensagem('GAME OVER', 40, (0,0,0))
        screen.blit(game_over, (WIDTH//2, HEIGHT//2))
        restart = exibir_mensagem('Click R para jogar novamente', 20, (0,0,0))
        screen.blit(restart, (WIDTH//2, (HEIGHT//2) + 60))


    else:
        pontos += 1
        tudo_sprites.update()
        texto_pontos = exibir_mensagem(pontos, 40, (0,0,0))

        

    if pontos % 100 == 0:
        if velocidade_jogo >= 50:
            velocidade_jogo += 0
        else:
            velocidade_jogo += 1


    #checar colisao
    ice_cream_collisions = pygame.sprite.spritecollide(fox, ice_cream_sprites, True)
    for ice_cream in ice_cream_collisions:
        score += 1

    ice_cream_sprites.update()

    ice_cream_sprites.draw(screen)
        
    screen.blit(texto_pontos, (520, 30))

    pygame.time.Clock().tick(60)


    pygame.display.flip()




