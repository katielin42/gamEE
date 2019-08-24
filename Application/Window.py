import pygame as pg
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
        Window.screen = pg.display.set_mode((Window.width, Window.height))

        #clear background
        Window.clear()

        #flip buffer
        pg.display.flip()

    @staticmethod
    def clear():
        Window.screen.fill(colour.black)

#Window object
window = Window()


# start Screen configurations
class StartWindow():
    IsInit = False
    width = 720
    height = 1280


    def __init__(self):
        if StartWindow.IsInit:
            print("Dumbass")
            return
        StartWindow.IsInit = True
        self.font = pg.font.SysFont('Comic Sans MS', 32)
        self.screen = pg.display.set_mode((StartWindow.height, StartWindow.width))
        pg.display.set_caption("Our Game")
#start window
startWindow = StartWindow()