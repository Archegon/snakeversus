import pygame
import display
import game

pygame.init()

fullscreen = False

running = True

clock = pygame.time.Clock()
window = display.Window(1920, 1080, fullscreen)
grid = game.Grid(window)
player1 = game.Player(window, grid, (255, 255, 255))
player1.set_keys(pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)


while running:
    window.screen.fill((0, 0, 0))
    player1.draw()
    player1.movement()

    for event in pygame.event.get():
        player1.controls(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            window.display.quit()
            pygame.quit()
            exit()

        if event.type == pygame.QUIT:
            running = False

    window.display.flip()
    clock.tick(60)
