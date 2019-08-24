import pygame

class Clock():

    def __init__(self, FPS):
        self.clock = pygame.time.Clock()

        self.FPS = FPS

    def waitForTick(self):
        self.clock.tick(self.FPS)

    def changeFPS(self, FPS):
        self.FPS = FPS

clock = Clock(60)