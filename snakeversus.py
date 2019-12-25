import pygame
import display
import game
import object

pygame.init()
pygame.display.set_caption("Snake Versus")

fullscreen = True
game_running = True
score_win = 20

running = True

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
black = (0, 0, 0)

clock = pygame.time.Clock()
window = display.Window(1920, 1080, fullscreen)
top_bar = game.TopBar(window)
grid = game.Grid(window, top_bar)
object.GameLink.window = window
object.GameLink.grid = grid

program_state = {
    "main_menu": lambda: main_menu(),
    "score_mode": lambda: score_mode()
}

current_state = "main_menu"
last_state = ""


def set_current_state(text):
    global current_state

    current_state = text


def quit_game():
    window.display.quit()
    pygame.quit()
    exit()


text1 = display.Text("SNAKE VERSUS", 84, window.width / 2, 200, (219, 68, 68))
text2 = display.Text("By DAV", 24, text1.x + 270, text1.y + 70)
option1 = display.Text("Score Mode", 32, text1.x, text1.y + 300, func=lambda: set_current_state("score_mode"))
option2 = display.Text("Head to Head Mode", 32, text1.x, text1.y + 350)
option3 = display.Text("Options", 32, text1.x, text1.y + 400)
option4 = display.Text("Quit game", 32, text1.x, text1.y + 450, func=lambda: quit_game())
selection1 = display.Selection([option1, option2, option3, option4], (219, 68, 68))


def main_menu():
    global running

    window.screen.fill(black)

    text1.draw()
    text2.draw()
    selection1.draw()

    for event in pygame.event.get():
        selection1.controls(event)

        if event.type == pygame.QUIT:
            running = False


def toggle_pause():
    global game_running
    game_running = not game_running


pause_option1 = display.Text("Resume", 32, window.width / 2, 250, black, func=lambda: toggle_pause())
pause_option2 = display.Text("Exit to menu", 32, window.width / 2, 300, black,
                             func=lambda: set_current_state("main_menu"))
pause_option3 = display.Text("Quit game", 32, window.width / 2, 350, black, func=lambda: quit_game())
pause_selection = display.Selection([pause_option1, pause_option2, pause_option3], white)


def pause_menu():
    rect = object.Rect(400, 700, window.width / 2, 140, (168, 60, 50))

    rect.draw()
    pause_selection.draw()


rect2 = object.Rect(600, 100, window.width / 2, 10, (168, 60, 50))


def score_mode():
    global running
    global game_running
    global score_header_str

    score_p1 = display.Text("Player 1", 32, 85 + 100, 20, player1.color)
    score_text = display.Text("Score:", 32, 95 + 100, 60)
    score_val = display.Text(str(player1.score), 32, 175 + 100, 60)

    score_p2 = display.Text("Player 2", 32, 85 + 1600, 20, player2.color)
    score_text2 = display.Text("Score:", 32, 95 + 1600, 60)
    score_val2 = display.Text(str(player2.score), 32, 175 + 1600, 60)
    score_header = display.Text(score_header_str, 48, window.width / 2, 40)

    if game_running:
        if player1.score >= score_win:
            score_header_str = "Player 1 Wins"
            game_running = False
        elif player2.score >= score_win:
            score_header_str = "Player 2 Wins"
            game_running = False

        window.screen.fill(black)
        player1.update()
        player2.update()
        food.update()
        grid.draw()
        score_text.draw()
        score_p1.draw()
        score_val.draw()

        score_p2.draw()
        score_text2.draw()
        score_val2.draw()

        score_header.draw()

    else:
        pause_menu()
        rect2.draw()
        score_header.draw()

    for event in pygame.event.get():
        player1.controls(event)
        player2.controls(event)

        if game_running is False:
            pause_selection.controls(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            toggle_pause()
            pause_selection.selection = 0

        if event.type == pygame.QUIT:
            running = False


while running:
    if current_state != last_state:
        if current_state == "main_menu":
            selection1.selection = 0
        elif current_state == "score_mode":
            score_header_str = "First to " + str(score_win) + " Wins!"
            game_running = True
            pause_selection.selection = 0
            player1 = game.Player(window, grid, blue)
            player1.set_keys(pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
            player2 = game.Player(window, grid, green)
            player2.set_keys(pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
            player2.x = grid.width
            food = game.Food([player1, player2])

    last_state = current_state
    program_state[current_state]()

    window.display.flip()
    clock.tick(60)
