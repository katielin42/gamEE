import pygame

from Application.Window import window
from Application.Colour import colour
from Application.GameState import gameState

class GameObject():
    def __init__(self , pos_x = 0, pos_y = 0, vel_x = 0, vel_y = 0):
        #initialize position
        self.position = pygame.Vector2()
        self.position.x = pos_x
        self.position.y = pos_y

        #initialize velocity. Velocity is in units of pixels per frame.
        self.velocity = pygame.Vector2()
        self.velocity.x = vel_x
        self.velocity.y = vel_y

    #method for updating the current position depending on current velocity
    def updatePosition(self):
        self.position += self.velocity

    #method for drawing the game object
    def drawObject(self):
        pygame.draw.rect(window.screen, colour.blue,
                         (self.position.x, self.position.y, 30, 30))

    def EventHandler(self, event):
        pass




