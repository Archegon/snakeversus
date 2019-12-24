import pygame
import display

pygame.init()

running = True

clock = pygame.time.Clock()
window = display.Window(1920, 1080, False)


while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            window.display.quit()
            pygame.quit()
            exit()

        if event.type == pygame.QUIT:
            running = False

    window.display.flip()
    clock.tick(60)
