import pygame
from PIL import Image

from Application.GameObject import GameObject

class Background( GameObject ):
    img = None
    def __init__(self):
        pass

    def load(self, gameState):
        if gameState == 0:
            Background.img = Image.open("Resources/temp_backdrop0.jpg")