import pygame

from Application.Window import window
from Application.Colour import colour

class GameObject():
    def __init__(self):
        #initialize position
        self.position = pygame.Vector2()
        self.position.x = 0
        self.position.y = 0

        #initialize velocity. Velocity is in units of pixels per frame.
        self.velocity = pygame.Vector2()
        self.velocity.x = 0
        self.velocity.y = 0

    #method for updating the current position depending on current velocity
    def updatePosition(self):
        self.position += self.velocity

    #method for drawing the game object
    def drawObject(self):
        pygame.draw.rect(window.screen, colour.blue,
                         (self.position.x, self.position.y, 30, 30))

    def EventHandler(self, event):
        pass




