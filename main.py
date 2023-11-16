#----------FOX ADVENTURES----------
#Giovana Gomes Leal - TIA: 32219431
#Beatriz Hitomi Gunji - TIA: 32248024

#Imports
import pygame
from pygame.locals import *
import sys
import os
import random
from button import Button
#import spritesheet

#inicializando o jogo
pygame.init()

#CLOCK
clock = pygame.time.Clock()
FPS = 50

#configurações da tela
pygame.display.set_caption('Fox Adventures')
screen = pygame.display.set_mode((960, 540))


#MENU PRINCIPAL
Menu_background = pygame.image.load("Menu.png")
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
Menu_background = pygame.transform.scale(Menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Fonte
def get_font(size): 
    return pygame.font.Font("font.ttf", size)

#VENCEU -> NIVEL 1
def venceu1():
    #Música
    venceu_music = pygame.mixer.Sound("MUSICA/Ganhou.mp3")
    venceu_music.play(-1)#o -1 cria um loop na música
    screen.fill("#fffd8d")
    while True:
        venceu_texto = get_font(60).render("VOCÊ VENCEU", True, "Black")
        venceu_central = venceu_texto.get_rect(center=(480, 100))
        screen.blit(venceu_texto, venceu_central)
        voltar_mouse_pos = pygame.mouse.get_pos()
        venceu_voltar = Button(image=None, pos=(480, 370), 
                            text_input="VOLTAR", font=get_font(20), base_color="Black", hovering_color="#F27F0C")
        next_mouse_pos = pygame.mouse.get_pos()
        next_level = Button(image=None, pos=(480, 470), 
                            text_input="PRÓXIMA FASE", font=get_font(20), base_color="Black", hovering_color="#F27F0C")

        venceu_voltar.changeColor(voltar_mouse_pos)
        venceu_voltar.update(screen)
        next_level.changeColor(next_mouse_pos)
        next_level.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if venceu_voltar.checkForInput(voltar_mouse_pos):
                    venceu_music.stop()
                    main_menu()
                if next_level.checkForInput(next_mouse_pos):
                    venceu_music.stop()
                    nivel2()
        pygame.display.update()
        
#VENCEU -> NIVEL 2
def venceu2():
    #Música
    venceu_music = pygame.mixer.Sound("MUSICA/Ganhou.mp3")
    venceu_music.play(-1)#o -1 cria um loop na música
    screen.fill("#fffd8d")
    while True:
        venceu_texto = get_font(60).render("VOCÊ VENCEU", True, "Black")
        venceu_central = venceu_texto.get_rect(center=(480, 100))
        screen.blit(venceu_texto, venceu_central)
        voltar_mouse_pos = pygame.mouse.get_pos()
        venceu_voltar = Button(image=None, pos=(480, 370), 
                            text_input="VOLTAR", font=get_font(20), base_color="Black", hovering_color="#F27F0C")
        next_mouse_pos = pygame.mouse.get_pos()
        next_level = Button(image=None, pos=(480, 470), 
                            text_input="PRÓXIMA FASE", font=get_font(20), base_color="Black", hovering_color="#F27F0C")

        venceu_voltar.changeColor(voltar_mouse_pos)
        venceu_voltar.update(screen)
        next_level.changeColor(next_mouse_pos)
        next_level.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if venceu_voltar.checkForInput(voltar_mouse_pos):
                    venceu_music.stop()
                    main_menu()
                if next_level.checkForInput(next_mouse_pos):
                    venceu_music.stop()
                    nivel3()
        pygame.display.update()
        
#VENCEU -> NIVEL 3
def venceu3():
    #Música
    venceu_music = pygame.mixer.Sound("MUSICA/Zerou.mp3")
    venceu_music.play(-1)#o -1 cria um loop na música
    venceu_background = pygame.image.load("Venceu.png")
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 540
    venceu_background = pygame.transform.scale(venceu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.blit(venceu_background, (0, 0))
        venceu_texto = get_font(35).render("VOCÊ SALVOU A FLORESTA!!!", True, "Black")
        venceu_central = venceu_texto.get_rect(center=(480, 100))
        screen.blit(venceu_texto, venceu_central)
        voltar_mouse_pos = pygame.mouse.get_pos()
        venceu_voltar = Button(image=None, pos=(480, 470), 
                            text_input="VOLTAR", font=get_font(20), base_color="Black", hovering_color="#F27F0C")

        venceu_voltar.changeColor(voltar_mouse_pos)
        venceu_voltar.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if venceu_voltar.checkForInput(voltar_mouse_pos):
                    venceu_music.stop()
                    main_menu()
        pygame.display.update()        

#PERDEU
def perdeu():
    #Música
    perdeu_music = pygame.mixer.Sound("MUSICA/Perdeu.mp3")
    perdeu_music.play(-1)#o -1 cria um loop na música
    screen.fill("Black")
    while True:
        perdeu_texto = get_font(60).render("VOCÊ PERDEU", True, "White")
        perdeu_central = perdeu_texto.get_rect(center=(480, 100))
        screen.blit(perdeu_texto, perdeu_central)
        voltar_mouse_pos = pygame.mouse.get_pos()
        perdeu_voltar = Button(image=None, pos=(480, 370), 
                            text_input="VOLTAR", font=get_font(20), base_color="White", hovering_color="#F27F0C")
    
        perdeu_voltar.changeColor(voltar_mouse_pos)
        perdeu_voltar.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if perdeu_voltar.checkForInput(voltar_mouse_pos):
                    perdeu_music.stop()
                    main_menu()
        pygame.display.update()

#PLAY
def play():
    while True:
        nivel1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
        pygame.display.update()
        
        
#NÍVEL1
def nivel1():
    #Música
    nivel1_music = pygame.mixer.Sound("MUSICA/Nivel1.mp3")
    nivel1_music.play(-1)#o -1 cria um loop na música

    #PARALLAX
    scroll_Nivel1 = 0
    Nivel1_chao = pygame.image.load("ground.png").convert_alpha()
    Nivel1_chao_width = Nivel1_chao.get_width()
    Nivel1_chao_height = Nivel1_chao.get_height()
    
    Nivel1_bg = []
    for i in range(1,10):
        Nivel1_Background = pygame.image.load(f"IMAGENS/Background_Nivel1/Nivel1_{i}.png").convert_alpha()
        Nivel1_bg.append(Nivel1_Background)
    Nivel1_width = Nivel1_bg[0].get_width()
    def draw_nivel1():
        for x in range(1000):
            speed_Nivel1 = 1
            for i in Nivel1_bg:
                screen.blit(i, ((x * Nivel1_width) - scroll_Nivel1 * speed_Nivel1, 0))
                speed_Nivel1 += 0.2
    def draw_nivel1_chao():
        for x in range(1000):
            screen.blit(Nivel1_chao, ((x * Nivel1_chao_width) - scroll_Nivel1 * 2.5, SCREEN_HEIGHT - Nivel1_chao_height))
    #loopGame    
    while True:
        score = 0
        play_mouse_pos = pygame.mouse.get_pos()

        clock.tick(FPS)
        draw_nivel1()
        draw_nivel1_chao()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and scroll_Nivel1 < 3000:
            scroll_Nivel1 += 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
#NÍVEL2
def nivel2():
    #Música
    nivel2_music = pygame.mixer.Sound("MUSICA/Nivel2.mp3")
    nivel2_music.play(-1)#o -1 cria um loop na música

    #PARALLAX
    scroll_Nivel2 = 0
    Nivel2_chao = pygame.image.load("ground.png").convert_alpha()
    Nivel2_chao_width = Nivel2_chao.get_width()
    Nivel2_chao_height = Nivel2_chao.get_height()
    
    Nivel2_bg = []
    for i in range(1,6):
        Nivel2_Background = pygame.image.load(f"Nivel2_{i}.png").convert_alpha()
        Nivel2_bg.append(Nivel2_Background)
    Nivel2_width = Nivel2_bg[0].get_width()
    def draw_nivel2():
        for x in range(1000):
            speed_Nivel2 = 1
            for i in Nivel2_bg:
                screen.blit(i, ((x * Nivel2_width) - scroll_Nivel2 * speed_Nivel2, 0))
                speed_Nivel2 += 0.2
    def draw_nivel2_chao():
        for x in range(1000):
            screen.blit(Nivel2_chao, ((x * Nivel2_chao_width) - scroll_Nivel2 * 2.5, SCREEN_HEIGHT - Nivel2_chao_height))
    #loopGame    
    while True:
        score = 0
        play_mouse_pos = pygame.mouse.get_pos()

        clock.tick(FPS)
        draw_nivel2()
        draw_nivel2_chao()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and scroll_Nivel2 < 3000:
            scroll_Nivel2 += 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
#NÍVEL3
def nivel3():
    #Música
    nivel3_music = pygame.mixer.Sound("MUSICA/Nivel3.mp3")
    nivel3_music.play(-1)#o -1 cria um loop na música

    #PARALLAX
    scroll_Nivel3 = 0
    Nivel3_chao = pygame.image.load("ground.png").convert_alpha()
    Nivel3_chao_width = Nivel3_chao.get_width()
    Nivel3_chao_height = Nivel3_chao.get_height()
    
    Nivel3_bg = []
    for i in range(1,8):
        Nivel3_Background = pygame.image.load(f"IMAGENS/Background_Nivel3/Nivel3_{i}.png").convert_alpha()
        Nivel3_bg.append(Nivel3_Background)
    Nivel3_width = Nivel3_bg[0].get_width()
    def draw_nivel3():
        for x in range(1000):
            speed_Nivel3 = 1
            for i in Nivel3_bg:
                screen.blit(i, ((x * Nivel3_width) - scroll_Nivel3 * speed_Nivel3, 0))
                speed_Nivel3 += 0.2
    def draw_nivel3_chao():
        for x in range(1000):
            screen.blit(Nivel3_chao, ((x * Nivel3_chao_width) - scroll_Nivel3 * 2.5, SCREEN_HEIGHT - Nivel3_chao_height))
    
    #loopGame    
    while True:
        score = 0
        play_mouse_pos = pygame.mouse.get_pos()

        clock.tick(FPS)
        draw_nivel3()
        draw_nivel3_chao()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and scroll_Nivel3 < 3000:
            scroll_Nivel3 += 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()    
#RANKING    
def ranking():
    ranking_music = pygame.mixer.Sound("MUSICA/Nivel3.mp3")
    ranking_music.play(-1)#o -1 cria um loop na música
    while True:
        ranking_mouse_pos = pygame.mouse.get_pos()

        screen.fill("Black")

        ranking_texto = get_font(30).render("HIGHSCORES", True, "White")
        ranking_central = ranking_texto.get_rect(center=(480, 170))
        name1 = get_font(15).render("1 - User: GHOST - SORVETES: 500", True, "White")
        user_tela1 = name1.get_rect(center=(480, 210))
        name2 = get_font(15).render("2 - User: 707 - SORVETES: 499", True, "White")
        user_tela2 = name2.get_rect(center=(480, 230))
        name3 = get_font(15).render("3 - User: aNy4 - SORVETES: 470", True, "White")
        user_tela3 = name3.get_rect(center=(480, 250))
        name4 = get_font(15).render("4 - User: Unknown - SORVETES: 450", True, "White")
        user_tela4 = name4.get_rect(center=(480, 270))
        name5 = get_font(15).render("5 - User: FizZy - SORVETES: 443", True, "White")
        user_tela5 = name5.get_rect(center=(480, 290))
        name6 = get_font(15).render("6 - User: JINX - SORVETES: 398", True, "White")
        user_tela6 = name6.get_rect(center=(480, 310))
        name7 = get_font(15).render("7 - User: Mike - SORVETES: 387", True, "White")
        user_tela7 = name6.get_rect(center=(480, 330))
        name8 = get_font(15).render("8 - User: Peaches - SORVETES: 360", True, "White")
        user_tela8 = name8.get_rect(center=(480, 350))
        name9 = get_font(15).render("9 - User: Isabelle - SORVETES: 289", True, "White")
        user_tela9 = name9.get_rect(center=(480, 370))
        name10 = get_font(15).render("10 - User: PurPLe GuY - SORVETES: 283", True, "White")
        user_tela10 = name10.get_rect(center=(480, 390))
        
        
        screen.blit(name1, user_tela1)
        screen.blit(name2, user_tela2)
        screen.blit(name3, user_tela3)
        screen.blit(name4, user_tela4)
        screen.blit(name5, user_tela5)
        screen.blit(name6, user_tela6)
        screen.blit(name7, user_tela7)
        screen.blit(name8, user_tela8)
        screen.blit(name9, user_tela9)
        screen.blit(name10, user_tela10)
        screen.blit(ranking_texto, ranking_central)

        ranking_voltar = Button(image=None, pos=(480, 460), 
                            text_input="VOLTAR", font=get_font(15), base_color="White", hovering_color="#F27F0C")

        ranking_voltar.changeColor(ranking_mouse_pos)
        ranking_voltar.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ranking_voltar.checkForInput(ranking_mouse_pos):
                    ranking_music.stop()
                    main_menu()

        pygame.display.update()
#INSTRUÇÕES    
def instrucoes():
    while True:
        ranking_mouse_pos = pygame.mouse.get_pos()

        screen.fill("#F27F0C")

        texto1 = get_font(30).render("BEM VINDO AO FOX ADVENTURES", True, "Black")
        texto_tela1 = texto1.get_rect(center=(480, 140))
        texto2 = get_font(15).render("Para jogar siga as instruções:", True, "Black")
        texto_tela2 = texto2.get_rect(center=(480, 240))
        texto3 = get_font(15).render("Para pular utilize a barra de espaço", True, "Black")
        texto_tela3 = texto3.get_rect(center=(480, 290))
        texto5 = get_font(15).render("Para tirar a música do menu aperte DESLIGAR SOM", True, "Black")
        texto_tela5 = texto5.get_rect(center=(480, 330))
        texto6 = get_font(15).render("Para voltar a música aperte em qualquer local da tela", True, "Black")
        texto_tela6 = texto6.get_rect(center=(480, 380))
        texto7 = get_font(15).render("BOM JOGO!!!", True, "Black")
        texto_tela7 = texto7.get_rect(center=(480, 430))
        
        screen.blit(texto1, texto_tela1)
        screen.blit(texto2, texto_tela2)
        screen.blit(texto3, texto_tela3)
        screen.blit(texto4, texto_tela4)
        screen.blit(texto5, texto_tela5)
        screen.blit(texto6, texto_tela6)
        screen.blit(texto6, texto_tela6)
        screen.blit(texto7, texto_tela7)

        ranking_voltar = Button(image=None, pos=(480, 510), 
                            text_input="VOLTAR", font=get_font(15), base_color="Black", hovering_color="White")

        ranking_voltar.changeColor(ranking_mouse_pos)
        ranking_voltar.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ranking_voltar.checkForInput(ranking_mouse_pos):
                    main_menu()

        pygame.display.update()

#MENU
def main_menu():
    #Musica
    menu_music = pygame.mixer.Sound("MUSICA/Menu.mp3")
    menu_music.play(-1)#o -1 cria um loop na música
    
    while True:
        screen.blit(Menu_background, (0, 0))
        
        #posição mouse
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_texto = get_font(50).render("FOX ADVENTURES", True, "White")
        menu_central = menu_texto.get_rect(center=(480, 100))

        #botões
        play_button = Button(image=None, pos=(480, 200), 
                            text_input="PLAY", font=get_font(35), base_color="White", hovering_color="#F27F0C")
        ranking_button = Button(image=None, pos=(480, 300), 
                            text_input="RANKING", font=get_font(35), base_color="White", hovering_color="#F27F0C")
        instrucoes_button = Button(image=None, pos=(480, 400), 
                            text_input="INSTRUÇÕES", font=get_font(35), base_color="White", hovering_color="#F27F0C")
        som_button = Button(image= None, pos=(860, 50), 
                            text_input= "DESLIGAR SOM", font=get_font(15), base_color="White", hovering_color="#F27F0C")
        quit_button = Button(image=None, pos=(480, 500), 
                            text_input="SAIR", font=get_font(35), base_color="White", hovering_color="#F27F0C")

        screen.blit(menu_texto, menu_central)

        for button in [play_button, som_button,instrucoes_button, ranking_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_music.play()
                if play_button.checkForInput(menu_mouse_pos):
                    menu_music.stop()
                    play()
                if ranking_button.checkForInput(menu_mouse_pos):
                    menu_music.stop()
                    ranking()
                if instrucoes_button.checkForInput(menu_mouse_pos):
                    menu_music.stop()
                    instrucoes()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
                if som_button.checkForInput(menu_mouse_pos):
                    menu_music.stop()

        pygame.display.update()

main_menu()

