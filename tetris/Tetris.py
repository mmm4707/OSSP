import pygame, sys, time
from pygame.locals import *
from Board import *
from mini_Board import *
#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)


class Tetris:

    def __init__(self):
        self.screen = pygame.display.set_mode((350, 450))
        self.clock = pygame.time.Clock()
        self.board = Board(self.screen)
        self.mini_board = mini_Board(self.screen)
        self.music_on_off = True
        self.check_reset = True
        

    def handle_key(self, event_key):
        if event_key == K_DOWN or event_key == K_s:
            self.board.drop_piece()
            self.mini_board.drop_piece()
            
        elif event_key == K_LEFT or event_key == K_a:
            self.board.move_piece(dx=-1, dy=0)
            self.mini_board.move_piece(dx=-1, dy=0)

        elif event_key == K_RIGHT or event_key == K_d:
            self.board.move_piece(dx=1, dy=0)
            self.mini_board.move_piece(dx=1, dy=0)

        elif event_key == K_UP or event_key == K_w:
            self.board.rotate_piece()
            self.mini_board.rotate_piece()
            
        elif event_key == K_SPACE:
            self.board.full_drop_piece()
            self.mini_board.full_drop_piece()

        elif event_key == K_q:
            self.board.ultimate()
            self.mini_board.ultimate()
            
        elif event_key == K_m:
            self.music_on_off = not self.music_on_off
            if self.music_on_off:
                pygame.mixer.music.play(-1, 0.0)
            else:
                pygame.mixer.music.stop()

    def HighScore(self):
        try:
            f = open('assets/save.txt', 'r')
            l = f.read()
            f.close()
            if int(l) < self.board.score:
                h_s = self.board.score
                f = open('assets/save.txt', 'w')
                f.write(str(self.board.score))
                f.close()
            else:
                h_s = l
            self.board.HS(str(h_s))
        except:
            f = open('assets/save.txt', 'w')
            f.write(str(self.board.score))
            f.close()
            self.board.HS(str(self.board.score))


    def run(self):
        pygame.init()
        icon = pygame.image.load('assets/images/icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Tetris')
        pygame.time.set_timer(pygame.USEREVENT, 500)
        start_sound = pygame.mixer.Sound('assets/sounds/Start.wav')
        start_sound.play()
#        bgm = pygame.mixer.music.load('assets/sounds/bgm.mp3')
        while True:
            if self.check_reset:
                self.board.newGame()
                self.check_reset = False
#                pygame.mixer.music.play(-1, 0.0)
            if self.board.game_over():
                self.screen.fill(WHITE)
#                pygame.mixer.music.stop()
                self.board.GameOver()
                self.HighScore()
                self.check_reset = True
                self.board.init_board()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP and event.key == K_p:
                    self.screen.fill(WHITE)
                    pygame.mixer.music.stop()
                    self.board.pause()
                    pygame.mixer.music.play(-1, 0.0)
                elif event.type == KEYDOWN:
                    self.handle_key(event.key)
                elif event.type == pygame.USEREVENT:
                    self.board.drop_piece()

                elif event.type == VIDEORESIZE:
                    info = pygame.display.Info()
                    resize = event.h / self.board.display_height

                    if event.w != self.board.display_width:
                        pygame.display.set_mode((self.board.display_width, self.board.display_height), RESIZABLE)

                    if resize != 1:
                        self.vdresize(resize, event.h)
                        if info.current_w == (1855):
                            pygame.display.set_mode((info.current_w, info.current_h), RESIZABLE).fill(MAIN_VIOLET)

            # self.screen.fill(BLACK)
            self.board.draw()
            pygame.display.update()
            self.clock.tick(30)

    def mini_run(self):
        pygame.init()
        icon = pygame.image.load('assets/images/icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Tetris mini')
        pygame.time.set_timer(pygame.USEREVENT, 500)
        start_sound = pygame.mixer.Sound('assets/sounds/Start.wav')
        start_sound.play()
#        bgm = pygame.mixer.music.load('assets/sounds/bgm.mp3')
        while True:
            if self.check_reset:
                self.mini_board.newGame()
                self.check_reset = False
#                pygame.mixer.music.play(-1, 0.0)
            if self.mini_board.game_over():
                self.screen.fill(WHITE)
#                pygame.mixer.music.stop()
                self.mini_board.GameOver()
                self.HighScore()
                self.check_reset = True
                self.mini_board.init_mini_Board()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP and event.key == K_p:
                    self.screen.fill(WHITE)
                    pygame.mixer.music.stop()
                    self.mini_board.pause()
                    pygame.mixer.music.play(-1, 0.0)
                elif event.type == KEYDOWN:
                    self.handle_key(event.key)
                elif event.type == pygame.USEREVENT:
                    self.mini_board.drop_piece()

                elif event.type == VIDEORESIZE:
                    info = pygame.display.Info()
                    resize = event.h / self.mini_board.display_height

                    if event.w != self.mini_board.display_width:
                        pygame.display.set_mode((self.mini_board.display_width, self.mini_board.display_height), RESIZABLE)

                    if resize != 1:
                        self.vdresize(resize, event.h)
                        if info.current_w == (1855):
                            pygame.display.set_mode((info.current_w, info.current_h), RESIZABLE).fill(MAIN_VIOLET)

            # self.screen.fill(BLACK)
            self.mini_board.draw()
            pygame.display.update()
            self.clock.tick(30)

if __name__ == "__main__":
    Tetris().run()