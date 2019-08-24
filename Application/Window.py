import pygame
from Application.Colour import colour

class Window():
    IsInit = False

    width = 480
    height = 360
    screen = []

    def __init__(self):
        if Window.IsInit:
            print("Already Initialized a Window")
            return
        Window.IsInit = True

        #setup screen
        Window.screen = pygame.display.set_mode((Window.width, Window.height))

        #clear background
        Window.clear()

        #flip buffer
        pygame.display.flip()

    @staticmethod
    def clear():
        Window.screen.fill(colour.black)

#Window object
window = Window()