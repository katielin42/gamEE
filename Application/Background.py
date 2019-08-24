import pygame as pg
from PIL import Image

from Application.GameObject import GameObject
from Application.Window import window
class Background( GameObject ):
    img = None
    def __init__(self):
        pass

    def load(self, gameState):
        if gameState == 0:
            Background.img = Image.Open("../Resources/temp_backdrop0.jpg")
            window.screen.blit(Background.img, (0, 0))
background = Background()