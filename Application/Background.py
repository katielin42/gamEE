from typing import Optional, Any

import pygame as pg
from PIL import Image

from Application.GameObject import GameObject
from Application.Window import window
from Application.GameState import gameState

class Background( GameObject ):
    #Imagines stored as pygame strings
    imgDict = {
        "Main Menu": None,
        "Level 1 OverWorld": None,
        "Level 1 UnderWorld": None,
        "Death Screen": None,
        "Win Screen": None
    }

    imgLocDict = {
        "Main Menu": "../Resources/temp_backdrop0.jpg"
    }

    def __init__(self):
        self.imageLoaded = False
        pass

    def drawObject(self):
        #Startup state
        if gameState.get() == gameState.stateList["Main Menu"]:
            #load in background image
            if Background.imgDict["Main Menu"] is None:
                self.convertPIL2Pygame(Background.imgLocDict["Main Menu"])
            window.screen.blit(Background.imgDict["Main Menu"], (0, 0))

    def convertPIL2Pygame(self, location):
        # load in background image
        PIL_img = Image.open(location)
        mode = PIL_img.mode
        size = PIL_img.size
        PIL_img_asBytes = PIL_img.tobytes()

        #based on current state store the pygame surface image
        Background.imgDict[gameState.getDict()] = pg.image.fromstring(PIL_img_asBytes, size, mode)
