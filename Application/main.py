# Main Entry point
import sys
import pygame as pg
import os

#Initialize pygame
pg.init()

from Application.Colour import colour
from Application.GameObject import GameObject
from Application.Window import window
from Application.Clock import clock
from Application.Player import Player
from Application.GameState import gameState
from Application.Background import background


# load in an object(x location, y location). ALl objects go here
player = Player(30, 30)
player2 = Player(100, 100)

ObjectList = [player, player2]

# set the center of the rectangular object.
if __name__ == "__main__":

    #While the game is running...
    while gameState.isRunning:

        #Check if the current state is the main menu
        if gameState.get() == gameState.stateList["Main Menu"]:

            #initialise backdrop
            background.load(gameState)
            #display title screen menu
            text = window.font.render('Press Space to Start and Backspace to Quit', True, (200, 200, 200))
            window.screen.blit(text, [200,200])

            #Check each pygame event for the current frame
            for event in pg.event.get():

                #if window is closed, exit pygame
                if event.type == pg.QUIT:
                    gameState.isRunning = False

                #handles events for each object
                for obj in ObjectList:
                    obj.EventHandler(event)

                #press space to start the game, game state changed to 1. press backspace to quit the game.
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        gameState.set(1)
                    if event.key == pg.K_BACKSPACE:
                        isRunning = False

            #updates position of object constantly
            for obj in ObjectList:
                obj.updatePosition()

        #Check if we're in a state where a player has control
        elif gameState.playerHasControl:

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

        #flip display buffer
        pg.display.flip()

pg.quit()
exit(0)