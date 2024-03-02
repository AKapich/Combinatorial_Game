import pygame
from draw_text_with_color_box import draw_text_with_color_box
from game_config import SequenceConfig
from game_config import game_colors


def draw_controls_info(
    screen: pygame.Surface,
    config: list[SequenceConfig],
):
    screen_width = screen.get_width()

    spacing = 80
    box_size = 40
    start_x = 100
    x = start_x
    y = 80

    i = 0
    while i < len(config):
        rect = draw_text_with_color_box(
            screen,
            box_size,
            game_colors[i],
            "Kolor " + str(i + 1) + f" ({config[i].length})",
            x,
            y,
        )

        if rect.right > screen_width:
            x = start_x
            y += box_size
            continue

        x = rect.right + spacing
        i += 1
