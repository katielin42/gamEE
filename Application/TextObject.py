import pygame

from Application.Colour import colour
from Application.GameObject import GameObject
from Application.GameState import gameState
from Application.Window import window

class TextObject( GameObject ):

    #rendered texts
    renderedTextDict = {
        "Main Menu": None
    }

    def __init__(self, context = None):
        GameObject.__init__(self)

        self.context = context

    def drawObject(self, context = None):

        if gameState.get() == gameState.stateDict["Main Menu"]:

            #check if text has been rendered.
            if TextObject.renderedTextDict["Main Menu"] is None:
                TextObject.renderedTextDict["Main Menu"] = \
                    window.font.render('Press Space to Start and Backspace to Quit', True, colour.white)

            window.screen.blit(TextObject.renderedTextDict["Main Menu"], [200, 200])

