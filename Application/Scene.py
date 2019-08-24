import pygame

class Scene():
    def __init__(self):
        self.objectList = []

    def drawScene(self):
        #override method
        pass

    def renderObjects(self):
        for obj in self.objectList:
            obj.drawObject()

    def handleEvents(self):
        #override method
        pass