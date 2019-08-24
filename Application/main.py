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
from Application.Testing.MainMenu import MainMenu


# load in an object(x location, y location).
player = Player(30, 30)
player2 = Player(100, 100)

ObjectList = [player, player2]

#Scene objects (not initialized)
mainMenu = None

# set the center of the rectangular object.
if __name__ == "__main__":

    #While the game is running...
    while gameState.isRunning:

        #Get the current state
        currentState = gameState.get()

        #Check if the current state is the main menu
        if currentState == gameState.stateDict["Main Menu"]:

            #if mainMenu has not been initialized
            if mainMenu is None:
                mainMenu = MainMenu()

            #Handle events in the main menu
            mainMenu.handleEvents()

            #display title screen menu
            mainMenu.drawScene()

            #if game state has transitioned delete the main menu object
            if gameState.currentState != gameState.stateDict["Main Menu"]:
                del mainMenu
                mainMenu = None

        #Check if we're in a state where a player has control
        elif currentState == gameState.stateDict["Level 1 OverWorld"]:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameState.isRunning = False

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