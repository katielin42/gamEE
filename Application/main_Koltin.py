import pygame

gameState = 0

#flag to indicate if running
IsRunning = True

from Application.Colour import colour
from Application.Map import
from Application.GameObject import GameObject
from Application.Window import window
from Application.Clock import clock
from Application.Player import Player

GameObject.GameState = gameState
#load in an object
player = Player(30, 30)
player2 = Player(100, 100)

ObjectList = [player, player2]

#main loop
while IsRunning:

    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsRunning = False

        #run the event handler for the event
        for obj in ObjectList:
            obj.EventHandler(event)

    # update the position of the object.
    for obj in ObjectList:
        obj.updatePosition()

    #render
    #start out with a clear background.
    window.clear()

    #render objects
    for obj in ObjectList:
        obj.drawObject()

    #flip buffer
    pygame.display.flip()

    #wait for tick
    clock.waitForTick()

pygame.quit()
exit(0)