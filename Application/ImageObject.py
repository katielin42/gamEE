
import pygame as pg
from PIL import Image

from Application.GameObject import GameObject
from Application.Window import window
from Application.GameState import gameState

class ImageObject( GameObject ):
    #Imagines stored as pygame strings
    imgDict = {
        "Press Space Start" : None,
        "Press Backspace Exit": None
    }

    imgRef = {
        "Press Space Start": 0,
        "Press Backspace Exit": 1
    }

    imgLocDict = {
        "Press Space Start": "../Resources/pressSpaceStart.png",
        "Press Backspace Exit": "../Resources/pressBackspaceExit.png"
    }

    def __init__(self):
        self.imageLoaded = False
        pass

    def drawObject(self, context = None):
        #Startup state
        if gameState.get() == gameState.stateDict["Main Menu"]:
            #load in background image
            if ImageObject.imgDict["Press Space Start"] is None:
                self.convertPIL2Pygame(ImageObject.imgLocDict["Press Space Start"], ImageObject.imgRef["Press Space Start"])
            window.screen.blit(ImageObject.imgDict["Press Space Start"], (200, 0))

            if ImageObject.imgDict["Press Backspace Exit"] is None:
                self.convertPIL2Pygame(ImageObject.imgLocDict["Press Backspace Exit"], ImageObject.imgRef["Press Backspace Exit"])
            window.screen.blit(ImageObject.imgDict["Press Backspace Exit"], (0, 0))

    def convertPIL2Pygame(self, location, context = 0):
        # load in background image
        PIL_img = Image.open(location)
        mode = PIL_img.mode
        size = PIL_img.size
        PIL_img_asBytes = PIL_img.tobytes()

        if gameState.currentState == gameState.stateDict["Main Menu"]:
            if context == ImageObject.imgRef["Press Space Start"]:
                #based on current state store the pygame surface image
                ImageObject.imgDict["Press Space Start"] = pg.image.load(location)
                #resize back to size of window
                ImageObject.imgDict["Press Space Start"]= \
                    pg.transform.scale(ImageObject.imgDict["Press Space Start"], \
                    (200, 200))
            if context == ImageObject.imgRef["Press Backspace Exit"]:
                # based on current state store the pygame surface image
                ImageObject.imgDict["Press Backspace Exit"] = pg.image.load(location)
                # resize back to size of window
                ImageObject.imgDict["Press Backspace Exit"] = \
                    pg.transform.scale(ImageObject.imgDict["Press Backspace Exit"], \
                                       (200, 200))
