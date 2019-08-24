import pygame

class Scene():
    def __init__(self):
        #fill out the object list with objects in the scene
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