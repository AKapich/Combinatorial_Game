import pygame
import time
from draw_controls_info import draw_controls_info
from draw_current_game_state import draw_current_game_state
from draw_win_loss_screen import draw_win_loss_screen
from draw_sequence import draw_sequence
from game_config import get_game_config
from draw_config import draw_config
from win_loss_utils import __check4arithmetic, check4arithmetic, choose_place

pygame.init()

display_info = pygame.display.Info()
screen = pygame.display.set_mode((display_info.current_w, 600))

config = get_game_config()

start_time = time.time()

while time.time() - start_time < 1:
    for event in pygame.event.get():
        pass

    screen.fill((0, 0, 0))
    draw_config(screen, config)
    pygame.display.flip()

sequence = []

color_keys = [
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
]

insertion_place = 0
running = True
lost = False
won = False
n = int(sum([s.length for s in config]) * 7/5)

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if lost or won:
                if event.key == pygame.K_r:
                    config = get_game_config()
                    lost = False
                    won = False
                    sequence = []
                    start_time = time.time()
                else:
                    break

            if event.key == pygame.K_ESCAPE:
                running = False

            for color_index, color_key in enumerate(color_keys):
                if color_index < len(config) and event.key == color_key:
                    sequence.insert(insertion_place, color_index)

                    if check4arithmetic(sequence, config):
                        lost = True
                    elif len(sequence) >= n:
                        won = True

                    insertion_place = choose_place(sequence, config)

    draw_sequence(screen, sequence, insertion_place)
    draw_controls_info(screen, config)
    draw_current_game_state(screen, len(sequence), n)

    if lost:
        draw_win_loss_screen(screen, False)
    if won:
        draw_win_loss_screen(screen, True)

    pygame.display.flip()

pygame.quit()
