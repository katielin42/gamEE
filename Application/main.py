# Main Entry point
import sys
import pygame as pg
gameState = 0
isRunning = True
# INIT #
pg.init()

from Application.Colour import colour
from Application.GameObject import GameObject
from Application.Window import window
from Application.Clock import clock
from Application.Player import Player

GameObject.GameState = gameState
#load in an object
player = Player(30, 30)
player2 = Player(100, 100)

ObjectList = [player, player2]

class StartWindow():
    IsInit = False
    width = 720
    height = 1280


    def __init__(self):
        if StartWindow.IsInit:
            print("Dumbass")
            return
        StartWindow.IsInit = True
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.screen = pg.display.set_mode((StartWindow.height, StartWindow.width))
        pg.display.set_caption("Our Game")

startWindow = StartWindow()

text = startWindow.font.render('                                                          Press Space to Start               Press Backspace to Quit', True, (0,200,0))

textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (startWindow.width //2, startWindow.height // 2)

if __name__ == "__main__":

    while isRunning:
        if gameState == 0:
            startWindow.screen.blit(text, textRect)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    isRunning = False
                for obj in ObjectList:
                    obj.EventHandler(event)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        gameState = 1
                        GameObject.GameState = gameState
                    if event.key == pg.K_BACKSPACE:
                        isRunning = False
            for obj in ObjectList:
                obj.updatePosition()
        elif gameState != 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    isRunning = False

                for obj in ObjectList:
                    obj.EventHandler(event)

            # update the position of the object.
            for obj in ObjectList:
                obj.updatePosition()

            # render
            # start out with a clear background.
            window.clear()

            # render objects
            for obj in ObjectList:
                obj.drawObject()

            # flip buffer
            pg.display.flip()

            # wait for tick
            clock.waitForTick()

        pg.display.flip()

pg.quit()
exit(0)