# Main Entry point
import sys, pygame


# INIT #
pygame.init()
display_height = 1280
display_width =720


gameDisplay = pygame.display.set_mode((display_height,display_width))

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)


if __name__ == "__main__":
    print("Hello World")
