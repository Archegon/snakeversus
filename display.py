import pygame


class Window:
    def __init__(self, width, height, fullscreen=False):
        self.width = width
        self.height = height
        self.display = pygame.display

        if fullscreen is True:
            self.screen = self.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = self.display.set_mode((self.width, self.height))
