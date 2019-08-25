import pygame

from Application.Colour import colour
from Application.GameObject import GameObject
from Application.Window import window
from Application.GameState import gameState

class Player( GameObject ):

    def __init__(self, position_x = 30, position_y = 30, velocity_x = 0, velocity_y = 0):
        #init GameObject
        GameObject.__init__(self)

        self.position.x = position_x
        self.position.y = position_y
        self.velocity.x = velocity_x
        self.velocity.y = velocity_y

    #Event handler is ran every tick and will deal with the events
    def EventHandler(self, event):
        #check what keys are currently pressed
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_w]:
            self.velocity.y = -3
        elif keysPressed[pygame.K_s]:
            self.velocity.y = 3
        else:
            self.velocity.y = 0
        if keysPressed[pygame.K_a]:
            self.velocity.x = -3
        elif keysPressed[pygame.K_d]:
            self.velocity.x = 3
        else:
            self.velocity.x = 0

        # update the position of the object.
        self.updatePosition()


    def drawObject(self):
        if gameState.get() > 0:
            pygame.draw.rect(window.screen, colour.blue,
                             (self.position.x, self.position.y, 30, 30))