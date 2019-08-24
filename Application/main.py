# Main Entry point
import sys
import pygame as pg

# INIT #
pg.init()

sstate = 0

class Window():
    IsInit = False
    width = 720
    height = 1280


    def __init__(self):
        if Window.IsInit:
            print("Dumbass")
            return
        Window.IsInit = True
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.screen = pg.display.set_mode((Window.height, Window.width))
        pg.display.set_caption("Our Game")

window = Window()

text = window.font.render('                                                          Press Space to Start               Press Backspace to Quit', True, (0,255,0))

textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (Window.width //2, Window.height // 2)

if __name__ == "__main__":

    isRunning = True
    while isRunning:
        window.screen.blit(text, textRect)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    state = 1
                if event.key == pg.K_BACKSPACE:
                    isRunning = False
        pg.display.flip()

