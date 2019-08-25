# Main Entry point
import pygame as pg

#Initialize pygame
pg.init()

from Application.Window import window
from Application.Clock import clock
from Application.Player import Player
from Application.GameState import gameState
from Application.MainMenu import MainMenu
from Application.LevelOne import LevelOneOverWorld

#Scene objects (not initialized)
mainMenu = None
levelOneOverworld = None

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

        #Current state is the level one over world
        elif currentState == gameState.stateDict["Level 1 OverWorld"]:

            #if the over world hasn't been initialized
            if levelOneOverworld is None:
                levelOneOverworld = LevelOneOverWorld()

            #Handle Events in the main menu
            levelOneOverworld.handleEvents()

            #display title screen menu
            levelOneOverworld.drawScene()

        #flip display buffer
        pg.display.flip()

        # wait for tick
        clock.waitForTick()

pg.quit()
exit(0)