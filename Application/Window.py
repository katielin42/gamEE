import pygame as pg
from Application.Colour import colour

class Window():
    IsInit = False

    width = 853
    height = 480
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

        self.font = pg.font.SysFont('Comic Sans MS', 32)
        pg.display.set_caption("Our Game")

    @staticmethod
    def clear():
        Window.screen.fill(colour.black)

#Window object
window = Window()

#
# # start Screen configurations
# class StartWindow():
#     IsInit = False
#
#     def __init__(self):
#         if StartWindow.IsInit:
#             print("Dumbass")
#             return
#         StartWindow.IsInit = True
#
#
# #start window
# startWindow = StartWindow()