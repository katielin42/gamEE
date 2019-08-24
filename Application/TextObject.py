import pygame

from Application.GameObject import GameObject

class TextObject( GameObject ):

    def __init__(self):
        GameObject.__init__(self)

    def drawObject(self):

        if gameState.currentState() == gameState.stateList
        text = window.font.render('Press Space to Start and Backspace to Quit', True, colour.white)