import pygame
import display
import game
import object

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

pygame.display.set_caption("Snake Versus")

fullscreen = False
score_win = 20
match_point = 19

running = True
score_music = False
in_progress = False

game.Player.EAT_SOUND = pygame.mixer.Sound('./sounds/eat2.wav')
game.Player.REDUCE_SOUND = pygame.mixer.Sound('./sounds/jump.wav')

white = (255, 255, 255)
green = (0, 255, 0)
blue = (54, 196, 247)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (250, 196, 47)

clock = pygame.time.Clock()
window = display.Window(1920, 1080, fullscreen)
object.GameLink.window = window
top_bar = game.TopBar()
grid = game.Grid(top_bar)
object.GameLink.grid = grid

current_state = "MainMenu"
last_state = ""
save_state = ""


def set_current_state(text):
    global current_state

    current_state = text


def quit_game():
    window.display.quit()
    pygame.quit()
    exit()


score_header_str = ""


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


def pause_menu():
    global running

    rect = object.Rect(400, 700, window.width / 2, 140, (168, 60, 50))

    rect.draw()
    pause_selection.draw()

    for event in pygame.event.get():
        pause_selection.controls(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            set_current_state(save_state)

        if event.type == pygame.QUIT:
            running = False


def score_mode(mode):
    global running
    global score_header_str
    global score_music
    global in_progress

    if score_music:
        if not in_progress:
            pygame.mixer.music.load('./sounds/heartbeat.mp3')
            pygame.mixer.music.play(-1)
            in_progress = True

    if mode == 1:
        score_header.set_string("First to " + str(score_win) + " Wins!")
        window.screen.fill(black)

        if player1.score >= match_point:
            score_music = True
        else:
            pygame.mixer.music.stop()
            in_progress = False

        if player1.score >= score_win:
            score_header.set_string("Player 1 Wins")
            set_current_state("ScoreMode_completed")

        score_p1 = display.Text("Player 1", 32, 85 + 100, 20, player1.color)
        score_text = display.Text("Score:", 32, 95 + 100, 60)
        score_val = display.Text(str(player1.score), 32, 175 + 100, 60)

        player1.update()
        food.update()
        grid.draw()
        score_text.draw()
        score_p1.draw()
        score_val.draw()
        score_header.draw()

    if mode == 2:
        score_header.set_string("First to " + str(score_win) + " Wins!")
        window.screen.fill(black)

        if player2.score >= match_point or player1.score >= match_point:
            score_music = True
        else:
            pygame.mixer.music.stop()
            in_progress = False

        if player1.score >= score_win:
            score_header.set_string("Player 1 Wins")
            set_current_state("ScoreMode_completed")
        elif player2.score >= score_win:
            score_header.set_string("Player 2 Wins")
            set_current_state("ScoreMode_completed")

        score_p1 = display.Text("Player 1", 32, 85 + 100, 20, player1.color)
        score_text = display.Text("Score:", 32, 95 + 100, 60)
        score_val = display.Text(str(player1.score), 32, 175 + 100, 60)
        score_p2 = display.Text("Player 2", 32, 85 + 400, 20, player2.color)
        score_text2 = display.Text("Score:", 32, 95 + 400, 60)
        score_val2 = display.Text(str(player2.score), 32, 175 + 400, 60)

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

    if mode == 3:
        score_header.set_string("First to " + str(score_win) + " Wins!")
        window.screen.fill(black)

        if player3.score >= match_point or player2.score >= match_point or player1.score >= match_point:
            score_music = True
        else:
            pygame.mixer.music.stop()
            in_progress = False

        if player1.score >= score_win:
            score_header.set_string("Player 1 Wins")
            set_current_state("ScoreMode_completed")
        elif player2.score >= score_win:
            score_header.set_string("Player 2 Wins")
            set_current_state("ScoreMode_completed")
        elif player3.score >= score_win:
            score_header.set_string("Player 3 Wins")
            set_current_state("ScoreMode_completed")

        score_p1 = display.Text("Player 1", 32, 85 + 100, 20, player1.color)
        score_text = display.Text("Score:", 32, 95 + 100, 60)
        score_val = display.Text(str(player1.score), 32, 175 + 100, 60)
        score_p2 = display.Text("Player 2", 32, 85 + 400, 20, player2.color)
        score_text2 = display.Text("Score:", 32, 95 + 400, 60)
        score_val2 = display.Text(str(player2.score), 32, 175 + 400, 60)
        score_p3 = display.Text("Player 3", 32, 85 + 1300, 20, player3.color)
        score_text3 = display.Text("Score:", 32, 95 + 1300, 60)
        score_val3 = display.Text(str(player3.score), 32, 175 + 1300, 60)

        player1.update()
        player2.update()
        player3.update()
        food.update()
        grid.draw()
        score_p1.draw()
        score_val.draw()
        score_text.draw()
        score_p2.draw()
        score_text2.draw()
        score_val2.draw()
        score_p3.draw()
        score_text3.draw()
        score_val3.draw()
        score_header.draw()

    if mode == 4:
        score_header.set_string("First to " + str(score_win) + " Wins!")
        window.screen.fill(black)

        if player3.score >= match_point or player2.score >= match_point or player1.score >= match_point:
            score_music = True
        else:
            pygame.mixer.music.stop()
            in_progress = False

        if player1.score >= score_win:
            score_header.set_string("Player 1 Wins")
            set_current_state("ScoreMode_completed")
        elif player2.score >= score_win:
            score_header.set_string("Player 2 Wins")
            set_current_state("ScoreMode_completed")
        elif player3.score >= score_win:
            score_header.set_string("Player 3 Wins")
            set_current_state("ScoreMode_completed")
        elif player4.score >= score_win:
            score_header.set_string("Player 4 Wins")
            set_current_state("ScoreMode_completed")

        score_p1 = display.Text("Player 1", 32, 85 + 100, 20, player1.color)
        score_text = display.Text("Score:", 32, 95 + 100, 60)
        score_val = display.Text(str(player1.score), 32, 175 + 100, 60)
        score_p2 = display.Text("Player 2", 32, 85 + 400, 20, player2.color)
        score_text2 = display.Text("Score:", 32, 95 + 400, 60)
        score_val2 = display.Text(str(player2.score), 32, 175 + 400, 60)
        score_p3 = display.Text("Player 3", 32, 85 + 1300, 20, player3.color)
        score_text3 = display.Text("Score:", 32, 95 + 1300, 60)
        score_val3 = display.Text(str(player3.score), 32, 175 + 1300, 60)
        score_p4 = display.Text("Player 4", 32, 85 + 1500, 20, player3.color)
        score_text4 = display.Text("Score:", 32, 95 + 1500, 60)
        score_val4 = display.Text(str(player4.score), 32, 175 + 1500, 60)

        player1.update()
        player2.update()
        player3.update()
        player4.update()
        food.update()
        grid.draw()
        score_p1.draw()
        score_val.draw()
        score_text.draw()
        score_p2.draw()
        score_text2.draw()
        score_val2.draw()
        score_p3.draw()
        score_text3.draw()
        score_val3.draw()
        score_p4.draw()
        score_text4.draw()
        score_val4.draw()
        score_header.draw()

    for event in pygame.event.get():
        if mode >= 1:
            player1.controls(event)
        if mode >= 2:
            player2.controls(event)
        if mode >= 3:
            player3.controls(event)
        if mode >= 4:
            player4.controls(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            set_current_state("ScoreMode_pause")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            food.generate()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_END:
            player4.eat()

        if event.type == pygame.QUIT:
            running = False


def score_mode_completed():
    global running

    score_header.draw()
    set_current_state("ScoreMode_pause")

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


def player_selection():
    global running

    rect = object.Rect(500, 600, window.width / 2, 400, black)

    rect.draw()
    player_selection_1.draw()

    for event in pygame.event.get():
        player_selection_1.controls(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            set_current_state("MainMenu")
        if event.type == pygame.QUIT:
            running = False


while running:
    if current_state != last_state:
        if current_state == "MainMenu":
            text1 = display.Text("SNAKE VERSUS", 84, window.width / 2, 200, (219, 68, 68))
            text2 = display.Text("By DAV", 24, text1.x + 270, text1.y + 70)
            option1 = display.Text("Score Mode", 32, text1.x, text1.y + 300,
                                   func=lambda: set_current_state("PlayerSelection"))
            option2 = display.Text("Head to Head Mode", 32, text1.x, text1.y + 350)
            option3 = display.Text("Options", 32, text1.x, text1.y + 400)
            option4 = display.Text("Quit game", 32, text1.x, text1.y + 450, func=lambda: quit_game())
            selection1 = display.Selection([option1, option2, option3, option4], (219, 68, 68))
            selection1.selection = 0
            pygame.mixer.music.load('./sounds/background music.mp3')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

        elif current_state == "PlayerSelection":
            selection_1 = display.Text("1 Player Mode", 32, window.width / 2, 500,
                                       func=lambda: set_current_state("1_player_score_mode_init"))
            selection_2 = display.Text("2 Player Mode", 32, window.width / 2, 570,
                                       func=lambda: set_current_state("2_player_score_mode_init"))
            selection_3 = display.Text("3 Player Mode", 32, window.width / 2, 640,
                                       func=lambda: set_current_state("3_player_score_mode_init"))
            selection_4 = display.Text("4 Player Mode", 32, window.width / 2, 720,
                                       func=lambda: set_current_state("4_player_score_mode_init"))
            player_selection_1 = display.Selection([selection_1, selection_2, selection_3, selection_4], (219, 68, 68))

        elif current_state == "1_player_score_mode_init":
            pygame.mixer.music.stop()
            score_header = display.Text(score_header_str, 48, window.width / 2, 40)
            player1 = game.Player(blue)
            player1.set_keys(pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
            food = game.Food([player1])
            set_current_state("1_player_score_mode_running")

        elif current_state == "2_player_score_mode_init":
            pygame.mixer.music.stop()
            score_header = display.Text(score_header_str, 48, window.width / 2, 40)
            player1 = game.Player(blue)
            player1.set_keys(pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
            player2 = game.Player(green)
            player2.set_keys(pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
            player2.x = grid.width
            food = game.Food([player1, player2])
            set_current_state("2_player_score_mode_running")

        elif current_state == "3_player_score_mode_init":
            pygame.mixer.music.stop()
            score_header = display.Text(score_header_str, 48, window.width / 2, 40)
            player1 = game.Player(blue)
            player1.set_keys(pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
            player2 = game.Player(green)
            player2.set_keys(pygame.K_i, pygame.K_l, pygame.K_k, pygame.K_j)
            player2.x = grid.width
            player3 = game.Player(yellow)
            player3.set_keys(pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
            player3.y = grid.height
            food = game.Food([player1, player2, player3])
            set_current_state("3_player_score_mode_running")

        elif current_state == "4_player_score_mode_init":
            pygame.mixer.music.stop()
            score_header = display.Text(score_header_str, 48, window.width / 2, 40)
            player1 = game.Player(blue)
            player1.set_keys(pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
            player2 = game.Player(green)
            player2.set_keys(pygame.K_i, pygame.K_l, pygame.K_k, pygame.K_j)
            player2.x = grid.width
            player3 = game.Player(yellow)
            player3.set_keys(pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
            player3.y = grid.height
            player4 = game.Player((204, 0, 204))
            player4.set_keys(pygame.K_KP5, pygame.K_KP3, pygame.K_KP2, pygame.K_KP1)
            player4.y = grid.height
            player4.x = grid.width
            food = game.Food([player1, player2, player3, player4])
            set_current_state("4_player_score_mode_running")

        elif current_state == "ScoreMode_pause":
            pause_option1 = display.Text("Resume", 32, window.width / 2, 250, black,
                                         func=lambda: set_current_state(save_state))
            pause_option2 = display.Text("Exit to menu", 32, window.width / 2, 300, black,
                                         func=lambda: set_current_state("MainMenu"))
            pause_option3 = display.Text("Quit game", 32, window.width / 2, 350, black, func=lambda: quit_game())
            pause_selection = display.Selection([pause_option1, pause_option2, pause_option3], white)
            pause_selection.selection = 0
            save_state = last_state

        elif current_state == "ScoreMode_completed":
            pygame.mixer.music.stop()

    last_state = current_state

    if current_state == "MainMenu":
        main_menu()
    elif current_state == "PlayerSelection":
        player_selection()
    elif current_state == "1_player_score_mode_running":
        score_mode(1)
    elif current_state == "2_player_score_mode_running":
        score_mode(2)
    elif current_state == "3_player_score_mode_running":
        score_mode(3)
    elif current_state == "4_player_score_mode_running":
        score_mode(4)
    elif current_state == "ScoreMode_pause":
        pause_menu()
    elif current_state == "ScoreMode_completed":
        score_mode_completed()

    window.display.flip()
    clock.tick(60)
