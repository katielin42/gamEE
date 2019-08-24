# Main Entry point
import sys
import pygame as pg
import os

gameState = 0
isRunning = True

# INITILISING #
pg.init()

from Application.Colour import colour
from Application.GameObject import GameObject
from Application.Window import window
from Application.Clock import clock
from Application.Player import Player

GameObject.GameState = gameState

# load in an object(x location, y location). ALl objects go here
player = Player(30, 30)
player2 = Player(100, 100)

ObjectList = [player, player2]


# set the center of the rectangular object.

if __name__ == "__main__":

# while the app is running
    while isRunning:

        #if no buttons have been pressed
        if gameState == 0:

            #initialise backdrop
            bg = pg.image.load('/Users/kate/Documents/Engineerin/gamEE/Resources/temp_backdrop0.jpg')
            window.screen.blit(bg, (0, 0))
            #display title screen menu
            text = window.font.render('Press Space to Start and Backspace to Quit', True, (200, 200, 200))
            window.screen.blit(text, [200,200])

            # loops through each event and constantly checks if the game is still running
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    isRunning = False

                #handles events for each object
                for obj in ObjectList:
                    obj.EventHandler(event)

                #press space to start the game, game state changed to 1. press backspace to quit the game.
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        gameState = 1
                        GameObject.GameState = gameState
                    if event.key == pg.K_BACKSPACE:
                        isRunning = False

            #updates position of object constantly
            for obj in ObjectList:
                obj.updatePosition()

        #if game state of >= 0 has been achieved
        elif gameState == 1:
            # display press p to pause
            # pause = startWindow.font.render('Press P to Pause',True, (200, 200, 200))
            # pauseRect = text.get_rect()
            # pauseRect.center = (startWindow.width // 2, startWindow.height // 2)
            # startWindow.screen.blit(pause, (0,0))
            # sprite.pause (pause is a function that will be implemented later)

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