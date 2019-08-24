import pygame

from Application.GameObject import GameObject

class Player( GameObject ):

    def __init__(self, position_x = 30, position_y = 30):
        #init GameObject
        GameObject.__init__(self)

        self.position.x = position_x
        self.position.y = position_y

    def EventHandler(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.velocity.x = -3
            if event.key == pygame.K_d:
                self.velocity.x = 3
            if event.key == pygame.K_w:
                self.velocity.y = -3
            if event.key == pygame.K_s:
                self.velocity.y = 3
            if event.key == pygame.K_SPACE:
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.velocity.x = 0
            if event.key == pygame.K_d:
                self.velocity.x = 0
            if event.key == pygame.K_w:
                self.velocity.y = 0
            if event.key == pygame.K_s:
                self.velocity.y = 0
            if event.key == pygame.K_SPACE:
                pass
        else:
            pass

