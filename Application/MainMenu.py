import pygame as pg

from Application.Background import Background
from Application.Colour import colour
from Application.GameObject import GameObject
from Application.GameState import gameState
from Application.Scene import Scene
from Application.TextObject import TextObject
from Application.Window import window

class MainMenu( Scene ):

    def __init__(self):
        Scene.__init__(self)

        #initialize objects in scene

        #Initialize background object
        self.objectList.append( Background() )

        #Initialize text objects
        self.objectList.append( TextObject() )

    def drawScene(self):
        #render appended objects
        self.renderObjects()

    def handleEvents(self):
        # Check each pygame event for the current frame
        for event in pg.event.get():

            # if window is closed, exit pygame
            if event.type == pg.QUIT:
                gameState.isRunning = False

            # press space to start the game, game state changed to 1. press backspace to quit the game.
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    gameState.set( gameState.stateDict["Level 1 OverWorld"] )
                if event.key == pg.K_BACKSPACE:
                    gameState.isRunning = False