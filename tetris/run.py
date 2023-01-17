import pygame
import pygame_menu
from Tetris import *
import time
class run:
    pygame.init()

white = (255, 255, 255)
titleImg = pygame.image.load('assets/images/icon.png')
startImg = pygame.image.load('assets/images/start.png')
quitImg = pygame.image.load('assets/images/exit.png')
clickStartImg = pygame.image.load('assets/images/start2.png')
clickQuitImg = pygame.image.load('assets/images/exit2.png')
miniImg = pygame.image.load('assets/images/mini.png')
clickminiImg = pygame.image.load('assets/images/mini2.png')
maxImg = pygame.image.load('assets/images/max.png')
clickmaxImg = pygame.image.load('assets/images/max2.png')
TetImg = pygame.image.load('assets/images/tetris.png')
backImg = pygame.image.load('assets/images/back.png')
clickbackImg = pygame.image.load('assets/images/back2.png')
keyImg = pygame.image.load('assets/images/keyboard.png')
clickkeyImg = pygame.image.load('assets/images/keyboard2.png')

display_width = 350
display_height = 450
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("테트리스")

clock = pygame.time.Clock()


class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

def quitgame():
    pygame.quit()
    sys.exit()


def mainmenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        
        titletext = gameDisplay.blit(TetImg, (110,0))
        startButton = Button(startImg,120,100,96,96,clickStartImg,120,100,startmenu)
        controlButton = Button(keyImg,120,200,96,96,clickkeyImg,120,200,controlkey)
        quitButton = Button(quitImg,120,350,96,96,clickQuitImg,120,350,quitgame)

        pygame.display.update()
        clock.tick(15)
        

def startmenu():
    startmenu = True
    while startmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(WHITE)
        
    #    titletext = gameDisplay.blit(titleImg, (105,20))
        startButton = Button(maxImg,120,60,96,96,clickmaxImg,100,40,start)
        miniButton = Button(miniImg,120,200,96,96,clickminiImg,100,180,minigame)
        quitButton = Button(quitImg,190,330,96,96,clickQuitImg,190,330,quitgame)
        backButton = Button(backImg,40,320,96,96,clickbackImg,40,320,mainmenu)

        pygame.display.update()
        clock.tick(15)

def controlkey():
    controlkey = True
    while controlkey:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(WHITE)
        text =  pygame.font.Font('assets/kor.ttf', 20).render('                 조작키                 ', True, BLACK)
        text1 = pygame.font.Font('assets/kor.ttf', 20).render('A,←     블럭을 왼쪽으로 한칸 옮김', True, BLACK)
        text2 = pygame.font.Font('assets/kor.ttf', 20).render('D,→     블럭을 오른쪽으로 한칸 옮김', True, BLACK)
        text3 = pygame.font.Font('assets/kor.ttf', 20).render('W,↑     블럭을 윗쪽으로 한칸 옮김', True, BLACK)
        text4 = pygame.font.Font('assets/kor.ttf', 20).render('S,↓     블럭을 아랫쪽으로 한칸 옮김', True, BLACK)
        text5 = pygame.font.Font('assets/kor.ttf', 18).render('스페이스바   블럭을 즉시 아래로 떨굼', True, BLACK)
        text6 = pygame.font.Font('assets/kor.ttf', 18).render('Q        스킬 사용', True, BLACK)
        text7 = pygame.font.Font('assets/kor.ttf', 18).render('M        bgm on/off', True, BLACK)
    
        gameDisplay.blit(text, (25, 20))
        gameDisplay.blit(text1, (25, 60))
        gameDisplay.blit(text2, (25, 100))
        gameDisplay.blit(text3, (25, 140))
        gameDisplay.blit(text4, (25, 180))
        gameDisplay.blit(text5, (25, 210))
        gameDisplay.blit(text6, (25, 240))
        gameDisplay.blit(text7, (25, 270))

    #    titletext = gameDisplay.blit(titleImg, (105,20))
        quitButton = Button(quitImg,190,330,96,96,clickQuitImg,190,330,quitgame)
        backButton = Button(backImg,40,320,96,96,clickbackImg,40,320,mainmenu)
        pygame.display.update()
        
        clock.tick(15)


def start():
    Tetris().run()


def minigame():
    Tetris().mini_run()



mainmenu()
game_loop()