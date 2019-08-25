import pygame

from Application.GameState import gameState
from Application.Player import Player
from Application.Scene import Scene

class LevelOneOverWorld( Scene ):

    def __init__(self):
        Scene.__init__(self)

        player = Player(30, 30)
        player2 = Player(100, 100)

        #for testing
        self.objectList.append( player )
        self.objectList.append( player2 )

    def drawScene(self):
        #render appended objects
        self.renderObjects()

    def handleEvents(self):
        # Check each pygame event for the current frame
        for event in pygame.event.get():

            # if window is closed, exit pygame
            if event.type == pygame.QUIT:
                gameState.isRunning = False

            #Handle Events
            for obj in self.objectList:
                obj.EventHandler(event)

class LevelOneUnderWorld( Scene ):
    def __init__(self, player_pos_x = 0, player_pos_y = 0, player_vel_x = 0, player_vel_y = 0):
        Scene.__init__(self)

        player = Player(player_pos_x, player_pos_y, player_vel_x, player_vel_y)
        player2 = Player(100, 100)

        #for testing
        self.objectList.append( player )
        self.objectList.append( player2 )

    def drawScene(self):
        #render appended objects
        self.renderObjects()

    def handleEvents(self):
        # Check each pygame event for the current frame
        for event in pygame.event.get():

            # if window is closed, exit pygame
            if event.type == pygame.QUIT:
                gameState.isRunning = False

            for obj in self.objectList:
                obj.EventHandler(event)
