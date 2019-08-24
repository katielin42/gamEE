from typing import Optional, Any

import pygame as pg
from PIL import Image

from Application.GameObject import GameObject
from Application.Window import window
from Application.GameState import gameState

class Background( GameObject ):
    img = None
    def __init__(self):
        pass

    def load(self):
        #Startup state
        if gameState.get() == 0:
            #load in background image
            self.convertPIL2Pygame("../Resources/temp_backdrop0.jpg")
            window.screen.blit(Background.img, (0, 0))

    def convertPIL2Pygame(self, location):
        # load in back image
        PIL_img = Image.open(location)
        mode = PIL_img.mode
        size = PIL_img.size
        PIL_img_asBytes = PIL_img.tobytes()
        Background.img = pg.image.fromstring(PIL_img_asBytes, size, mode)

background = Background()
