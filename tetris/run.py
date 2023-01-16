import pygame
import pygame_menu
from Tetris import *
import time


class run:
    pygame.init()

white = (255, 255, 255)
SH = False
titleImg = pygame.image.load('assets/images/icon.png')
startImg = pygame.image.load('assets/images/start.png')
quitImg = pygame.image.load('assets/images/exit.png')
clickStartImg = pygame.image.load('assets/images/start2.png')
clickQuitImg = pygame.image.load('assets/images/exit2.png')
miniImg = pygame.image.load('assets/images/mini.png')
clickminiImg = pygame.image.load('assets/images/mini2.png')

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
        
        titletext = gameDisplay.blit(titleImg, (105,20))
        startButton = Button(startImg,120,100,96,96,clickStartImg,120,100,start)
        miniButton = Button(miniImg,120,200,96,96,clickminiImg,120,200,minigame)
        quitButton = Button(quitImg,120,350,96,96,clickQuitImg,120,350,quitgame)
        pygame.display.update()
        clock.tick(15)
        
def start():
    Tetris().run()
    SH = False

def minigame():
    Tetris().run()
    SH = True


mainmenu()
game_loop()