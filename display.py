import pygame
from object import GameLink

pygame.font.init()


class Window:
    def __init__(self, width, height, fullscreen=False):
        self.width = width
        self.height = height
        self.display = pygame.display

        if fullscreen is True:
            self.screen = self.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.screen = self.display.set_mode((self.width, self.height))


class Text(GameLink):
    def __init__(self, string, size, x, y, color=(255, 255, 255), func=None):
        self.size = size
        self.func = func
        self.x = x
        self.y = y
        self.string = string
        self.color = color
        self.font = pygame.font.Font('freesansbold.ttf', self.size)
        self.text = self.font.render(self.string, False, self.color)
        self.width = self.text.get_width()
        self.height = self.text.get_height()

    def draw(self):
        self.window.screen.blit(self.text, (self.x - self.width / 2, self.y))

    def set_string(self, string):
        self.text = self.font.render(string, False, self.color)
        self.width = self.text.get_width()
        self.height = self.text.get_height()

    def call(self):
        if self.func is not None:
            return self.func()


class Selection(GameLink):
    def __init__(self, text, color):
        self.text = text
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.rect_color = color
        self.selection = 0

    def rect(self):
        return pygame.Rect(self.x - self.width / 2, self.y, self.width, self.height)

    def draw(self):
        self.x = self.text[self.selection].x
        self.y = self.text[self.selection].y
        self.width = self.text[self.selection].width + 50
        self.height = self.text[self.selection].height
        pygame.draw.rect(self.window.screen, self.rect_color, self.rect())

        for index in range(len(self.text)):
            self.text[index].draw()

    def controls(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.selection -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.selection += 1

        if self.selection > len(self.text) - 1:
            self.selection = 0
        if self.selection < 0:
            self.selection = len(self.text) - 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.text[self.selection].call()
