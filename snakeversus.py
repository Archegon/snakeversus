import pygame
import display
import game

pygame.init()

fullscreen = False
game_running = True

running = True

clock = pygame.time.Clock()
window = display.Window(1920, 1080, fullscreen)
grid = game.Grid(window)
player1 = game.Player(window, grid, (255, 255, 255))
player1.set_keys(pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
player2 = game.Player(window, grid, (255, 255, 255))
player2.set_keys(pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)


while running:
    if game_running:
        window.screen.fill((0, 0, 0))
        player1.update()

    for event in pygame.event.get():
        player1.controls(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_running = not game_running

        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            window.display.quit()
            pygame.quit()
            exit()

        if event.type == pygame.QUIT:
            running = False

    window.display.flip()
    clock.tick(60)
