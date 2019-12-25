import pygame


class Player:
    def __init__(self, window, grid, color):
        self.color = color
        self.size = 40
        self.direction = 'RIGHT'
        self.key_direction = 'None'
        self.speed = 10
        self.step = 1
        self.x = grid.width
        self.y = grid.height
        self.grid = grid
        self.window = window
        self.border = False
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
        self.grid.set_body(self.body)

        if len(self.body) > 1:
            for index in range(len(self.body)):
                if index > 0:
                    if self.body[0][0] == self.body[index][0]:
                        print("Hit body")

        if self.border:
            if self.grid.collision() == '+x' or self.grid.collision() == '+y' or self.grid.collision() == '-y' or self.grid.collision() == '-x':
                print("Border hit")
        else:
            if self.grid.collision() == '+x':
                self.x = 0
                self.body[0][1] = self.grid.collision()
            if self.grid.collision() == '-x':
                self.x = self.grid.width
                self.body[0][1] = self.grid.collision()
            if self.grid.collision() == '+y':
                self.y = self.grid.x_start
                self.body[0][1] = self.grid.collision()
            if self.grid.collision() == '-y':
                self.y = self.grid.height
                self.body[0][1] = self.grid.collision()

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
        pygame.draw.rect(self.window.screen, (255, 255, 255), self.rect())

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
                    self.body[index][0][1] -= self.step
                if self.body[index][1] == 'RIGHT':
                    self.body[index][0][0] += self.step
                if self.body[index][1] == 'DOWN':
                    self.body[index][0][1] += self.step
                if self.body[index][1] == 'LEFT':
                    self.body[index][0][0] -= self.step
                if self.body[index][1] == '+x':
                    self.body[index][0][0] = 0
                if self.body[index][1] == '-x':
                    self.body[index][0][0] = self.grid.width
                if self.body[index][1] == '+y':
                    self.body[index][0][1] = self.grid.x_start
                if self.body[index][1] == '-y':
                    self.body[index][0][1] = self.grid.height

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
                self.y -= self.step
                self.lastMoveTime = pygame.time.get_ticks()
            if self.direction == 'RIGHT':
                self.x += self.step
                self.lastMoveTime = pygame.time.get_ticks()
            if self.direction == 'DOWN':
                self.y += self.step
                self.lastMoveTime = pygame.time.get_ticks()
            if self.direction == 'LEFT':
                self.x -= self.step
                self.lastMoveTime = pygame.time.get_ticks()

            self.__body_update()

    def update(self):
        self.draw()
        self.__collision()
        self.movement()


class TopBar:
    def __init__(self, window):
        self.window = window
        self.size = 120
        self.height = self.size
        self.width = self.window.width


class Grid:
    def __init__(self, window, top_bar):
        self.top_bar = top_bar
        self.size = 40
        self.window = window
        self.color = (255, 255, 255)
        self.top_size = self.top_bar.size
        self.x_start = self.top_size // self.size
        self.y_start = 0
        self.width = self.window.width // self.size - 1
        self.height = self.window.height // self.size - 1
        self.body = None
        self.draw_grid = False
        self.draw_top = True
        self.rect = None

    def set_body(self, body):
        self.body = body

    def draw(self):
        self.rect = pygame.Rect(0, 0, self.window.width, self.top_size)
        pygame.draw.rect(self.window.screen, (0, 0, 0), self.rect)

        if self.draw_grid:
            for index in range(int(self.width + 1)):
                x = index * self.size
                pygame.draw.line(self.window.screen, self.color, (x, 0), (x, self.window.height))

            for index in range(int(self.height + 1)):
                y = index * self.size + self.top_size
                pygame.draw.line(self.window.screen, self.color, (0, y), (self.window.width, y))
        elif self.draw_top:
            pygame.draw.line(self.window.screen, self.color, (0, self.top_size), (self.window.width, self.top_size))

    def collision(self):
        if self.body[0][0][0] > self.width:
            return '+x'
        if self.body[0][0][0] < 0:
            return '-x'
        if self.body[0][0][1] > self.height:
            return '+y'
        if self.body[0][0][1] < self.x_start:
            return '-y'

    def convert(self, pos):
        return pos * self.size
