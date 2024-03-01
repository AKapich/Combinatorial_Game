import pygame
import time
from draw_controls_info import draw_controls_info
from draw_loss_screen import draw_loss_screen
from draw_sequence import draw_sequence
from game_config import get_game_config
from draw_config import draw_config

pygame.init()

display_info = pygame.display.Info()
screen = pygame.display.set_mode((display_info.current_w, display_info.current_h))

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

running = True
lost = False
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_r and lost:
                config = get_game_config()
                lost = False
                sequence = []
                start_time = time.time()

            for color_index, color_key in enumerate(color_keys):
                if event.key == color_key:
                    sequence.append(color_index)

    draw_sequence(screen, sequence, len(sequence))
    draw_controls_info(screen, config)

    if lost:
        draw_loss_screen()

    pygame.display.flip()

pygame.quit()
