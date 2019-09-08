import sys
from libs import mouse, acertos, movimento, musicaNotas, txtToList, imagem
import time
import pygame

#inicialização da variavel "ini" usada para calcular o tempo das notas serem plotadas na tela
ini = time.time()

#inicialização do pygame
pygame.init()

#tamanho da tela principal e criação da mesma
size = (1280,720)
screen = pygame.display.set_mode(size)

#variavel da taxa de quadros
tempo = pygame.time.Clock()

#RGB das cores mais utilizadas
white = (255, 64, 64)
green = (29, 172, 33)
yellow = (247, 228, 54) 
blue = (39, 125, 175)
red = (247,8,8)
black = (0,0,0)
gray = (165,179,172)

#variaveis para contar os acertos e erros da musica e o multiplicador da velocidade da música
contador = 0
erros = 0
multiplicador = 2.5

#leitura do texto das notas e retornando-as para uma função que cria cada objeto com seus atributos corretos
lista_notas = txtToList.notas()
objetos_musica = musicaNotas.criar_objetos(lista_notas)

#textos exibidos na tela do game
font = pygame.font.Font('fontes/leadcoat.ttf', 32)
text1 = font.render('Time '+str(time.time()-ini), True, green, blue)
textRect1 = text1.get_rect()
textRect1.center = (640, 100)
text2 = font.render('Acertos '+str(contador), True, green, blue)
textRect2 = text2.get_rect()
textRect2.center = (640, 150)

#imagem de fundo
background = pygame.image.load('imagens/background.png').convert_alpha()

#atribuição das imagens das notas que fora acertas
verde_press = imagem.press('verde')
vermelho_press = imagem.press('vermelho')
azul_press = imagem.press('azul')
amarelo_press = imagem.press('amarelo')

while True:
    #atribuição das imagens das notas da música
    img_verde = pygame.image.load('imagens/image_1_1.png').convert_alpha()
    img_vermelha = pygame.image.load('imagens/image_1_2.png').convert_alpha()
    img_amarela = pygame.image.load('imagens/image_1_3.png').convert_alpha()
    img_azul = pygame.image.load('imagens/image_1_4.png').convert_alpha()
    
    #definição do fundo preto
    screen.fill((black))

    #carregamento do background
    screen.blit(background, (0,0))

    #renderização dos textos "time" e "acerto" na tela
    text1 = font.render('Time '+str(time.time()-ini), True, white, black)
    screen.blit(text1,textRect1)
    text2 = font.render('Acertos '+str(contador), True, white, black)
    screen.blit(text2,textRect2)

    #verificar qual tecla foi apertada com acerto e renderiza imagens de acordo com a cor da nota
    if verde_press.cor == 'verde' and verde_press.appear == True:
        if verde_press.img > 16:
            verde_press.appear = False
            verde_press.img = 1
        else:
            test = pygame.image.load('imagens/split/image_'+str(verde_press.img)+'.png').convert_alpha()
            screen.blit(test, (215,515))
            verde_press.img+=1
    if vermelho_press.cor == 'vermelho' and vermelho_press.appear == True:
        if vermelho_press.img > 16:
            vermelho_press.appear = False
            vermelho_press.img = 1
        else:
            test = pygame.image.load('imagens/split/image_'+str(vermelho_press.img)+'.png').convert_alpha()
            screen.blit(test, (315,515))
            vermelho_press.img+=1

    #for plotando os objetos nota na tela de acordo com seus atributos "tempo" e "cor"
    for obj in objetos_musica:
        img_verde = pygame.transform.smoothscale( img_verde, (int(obj.atributos[2]), int(obj.atributos[3])) )
        img_vermelha = pygame.transform.smoothscale( img_vermelha, (int(obj.atributos[2]), int(obj.atributos[3])) )
        img_amarela = pygame.transform.smoothscale( img_amarela, (int(obj.atributos[2]), int(obj.atributos[3])) )
        img_azul = pygame.transform.smoothscale( img_azul, (int(obj.atributos[2]), int(obj.atributos[3])) )

        if obj.time > time.time()-ini:
            break
        if obj.cor == 'verde' and obj.time <= time.time()-ini:
            screen.blit(img_verde, (obj.atributos[0],obj.atributos[1]))
        elif obj.cor == 'vermelho' and obj.time <= time.time()-ini:
            screen.blit(img_vermelha, (obj.atributos[0],obj.atributos[1]))
        elif obj.cor == 'amarelo' and obj.time <= time.time()-ini:
            screen.blit(img_amarela, (obj.atributos[0],obj.atributos[1]))
        elif obj.cor == 'azul' and obj.time <= time.time()-ini:
            screen.blit(img_azul, (obj.atributos[0],obj.atributos[1]))
            
    pygame.display.flip()
    
    #verificar se alguma tecla foi apertada e se sim, passando para a função acertou_nota 
    #o primeiro objeto da lista de notas para verificar se ele está na posição certa para incrementar 
    #o contador ou não
    for event in pygame.event.get() :  
        if event.type == pygame.QUIT : 
            print(f"contador: {contador}")
            print(f"erros: {erros}")
            pygame.quit() 
            quit()  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                contador = acertos.acertou_nota(objetos_musica[0], contador)
                if objetos_musica[0].acerto==True:
                    verde_press.appear = True
                    verde_press.img = 1
                    del(objetos_musica[0])
            if event.key == pygame.K_s:
                contador = acertos.acertou_nota(objetos_musica[0], contador)
                if objetos_musica[0].acerto==True:
                    vermelho_press.appear = True
                    vermelho_press.img = 1
                    del(objetos_musica[0])
            if event.key == pygame.K_j:
                contador = acertos.acertou_nota(objetos_musica[0], contador)
                if objetos_musica[0].acerto==True:
                    del(objetos_musica[0])
            if event.key == pygame.K_k:
                contador = acertos.acertou_nota(objetos_musica[0], contador)
                if objetos_musica[0].acerto==True:
                    del(objetos_musica[0])
    
    #obter posição do mouse
    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)
    
    #for movendo os objetos pela superfície cinza de acordo com suas cores 
    for obj in objetos_musica:
        if obj.atributos[1] > 660:
            erros+=1
            del(objetos_musica[objetos_musica.index(obj)])
        elif obj.time > time.time()-ini:
            break
        elif obj.cor == 'verde' and obj.time <= time.time()-ini:
            obj.atributos = movimento.movimento_verde(obj.atributos, multiplicador)
        elif obj.cor == 'vermelho' and obj.time <= time.time()-ini:
            obj.atributos = movimento.movimento_vermelho(obj.atributos, multiplicador)
        elif obj.cor == 'amarelo' and obj.time <= time.time()-ini:
            obj.atributos = movimento.movimento_amarelo(obj.atributos, multiplicador)
        elif obj.cor == 'azul' and obj.time <= time.time()-ini:
            obj.atributos = movimento.movimento_azul(obj.atributos, multiplicador)

    tempo.tick(60)
    pygame.display.update()
