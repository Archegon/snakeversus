import pygame


class Player:
    def __init__(self, window, grid, color):
        self.color = color
        self.size = 40
        self.direction = 'RIGHT'
        self.key_direction = 'None'
        self.speed = 10
        self.x = 0
        self.y = 0
        self.grid = grid
        self.window = window
        self.movementDelay = 110 - self.speed
        self.lastMoveTime = 0
        self.body = [[[self.x, self.y], self.direction]]
        self.k_forward = None
        self.k_right = None
        self.k_down = None
        self.k_left = None

    def set_keys(self, k_forward, k_right, k_down, k_left):
        self.k_forward = k_forward
        self.k_right = k_right
        self.k_down = k_down
        self.k_left = k_left

    def controls(self, event):
        if event.type == pygame.KEYDOWN and event.key == self.k_forward:
            self.key_direction = 'UP'
        if event.type == pygame.KEYDOWN and event.key == self.k_right:
            self.key_direction = 'RIGHT'
        if event.type == pygame.KEYDOWN and event.key == self.k_down:
            self.key_direction = 'DOWN'
        if event.type == pygame.KEYDOWN and event.key == self.k_left:
            self.key_direction = 'LEFT'

        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            self.add_body()

    def __collision(self):
        if len(self.body) > 1:
            for index in range(len(self.body)):
                if index > 0:
                    if self.body[0][0] == self.body[index][0]:
                        print("Hit")

    def rect(self, x=None, y=None):
        if x is None:
            x = self.grid.convert(self.x)
        else:
            x = self.grid.convert(x)

        if y is None:
            y = self.grid.convert(self.y)
        else:
            y = self.grid.convert(y)

        return pygame.Rect(x, y, self.size, self.size)

    def add_body(self):
        print("Added new body")
        if self.body[-1][1] == 'UP':
            self.body.append([[self.body[-1][0][0], self.body[-1][0][1] + 1], ''])
        if self.body[-1][1] == 'RIGHT':
            self.body.append([[self.body[-1][0][0] - 1, self.body[-1][0][1]], ''])
        if self.body[-1][1] == 'DOWN':
            self.body.append([[self.body[-1][0][0], self.body[-1][0][1] - 1], ''])
        if self.body[-1][1] == 'LEFT':
            self.body.append([[self.body[-1][0][0] + 1, self.body[-1][0][1]], ''])

    def draw(self):
        pygame.draw.rect(self.window.screen, self.color, self.rect())

        for index in range(len(self.body)):
            if index > 0:
                pygame.draw.rect(self.window.screen, self.color,
                                 self.rect(self.body[index][0][0], self.body[index][0][1]))

    def __body_update(self):
        self.body[0][0][0] = self.x
        self.body[0][0][1] = self.y

        for index in reversed(range(len(self.body))):
            if len(self.body) > 1:
                self.body[index][1] = self.body[index - 1][1]

            if index > 0:
                if self.body[index][1] == 'UP':
                    self.body[index][0][1] -= 1
                if self.body[index][1] == 'RIGHT':
                    self.body[index][0][0] += 1
                if self.body[index][1] == 'DOWN':
                    self.body[index][0][1] += 1
                if self.body[index][1] == 'LEFT':
                    self.body[index][0][0] -= 1

        self.body[0][1] = self.direction

    def movement(self):
        if (pygame.time.get_ticks() - self.lastMoveTime) >= self.movementDelay:
            if len(self.body) > 1:
                if self.direction == 'UP' and self.key_direction != 'DOWN':
                    self.direction = self.key_direction
                elif self.direction == 'RIGHT' and self.key_direction != 'LEFT':
                    self.direction = self.key_direction
                elif self.direction == 'DOWN' and self.key_direction != 'UP':
                    self.direction = self.key_direction
                elif self.direction == 'LEFT' and self.key_direction != 'RIGHT':
                    self.direction = self.key_direction
            else:
                self.direction = self.key_direction

            if self.direction == 'UP':
                self.y -= 1
                self.lastMoveTime = pygame.time.get_ticks()
            if self.direction == 'RIGHT':
                self.x += 1
                self.lastMoveTime = pygame.time.get_ticks()
            if self.direction == 'DOWN':
                self.y += 1
                self.lastMoveTime = pygame.time.get_ticks()
            if self.direction == 'LEFT':
                self.x -= 1
                self.lastMoveTime = pygame.time.get_ticks()

            self.__body_update()

    def update(self):
        self.draw()
        self.__collision()
        self.movement()


class Grid:
    def __init__(self, window):
        self.size = 40
        self.window = window
        self.color = (255, 255, 255)
        self.width = window.width // self.size - 1
        self.height = window.height // self.size - 1

    def draw(self):
        for index in range(int(self.width + 1)):
            x = index * self.size
            pygame.draw.line(self.window.screen, self.color, (x, 0), (x, self.window.height))

        for index in range(int(self.height + 1)):
            y = index * self.size
            pygame.draw.line(self.window.screen, self.color, (0, y), (self.window.width, y))

    def convert(self, pos):
        return pos * self.size
