import pygame


class GameLink:
    window = None
    grid = None


class Rect(GameLink):
    def __init__(self, width, height, x=0, y=0, color=(255, 255, 255)):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

    def get(self):
        return pygame.Rect(self.x - self.width / 2, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.window.screen, self.color, self.get())
