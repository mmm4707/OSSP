# OSD_game  

[![License](https://img.shields.io/badge/license-GPLv3-green.svg)](http://www.gnu.org/licenses/gpl-3.0.html)
![Laguage](https://img.shields.io/badge/python-3.11.1-blue.svg)
![Laguage](https://img.shields.io/badge/pygame-1.9.3-blue.svg)    

### [ScreenShots](https://github.com/alchon/OSD_game/tree/master/pictures)        
![Gaming](https://github.com/alchon/OSD_game/blob/master/pictures/tetris.gif?raw=true)  

## 조작 키  
- a, ← 블럭을 왼쪽으로 한칸 옮김
- d, → 블럭을 오른쪽으로 한칸 옮김
- w, ↑ 블럭을 윗쪽으로 한칸 옮김
- s, ↓ 블럭을 아랫쪽으로 한칸 옮김
- 스페이스바 : 블럭을 즉시 아래로 떨굼
- p : 게임 일시정지
- q : 스킬 사용
- m : bgm on/off 

## 기본 기능  
- 7종류의 블럭이 랜덤하게 내려옵니다.  
- 특정 키를 눌러 블럭을 회전시킬 수 있습니다.  
- 회전한 블럭이 아래에 쌓입니다.  
- 한 줄 가득 블럭이 쌓이면 그 줄이 지워집니다.  

## 추가한 기능  
- 

## 사용한 오픈소스  
- https://github.com/hbseo/OSD_game

# Imports
import sys
import pygame

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
             self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))