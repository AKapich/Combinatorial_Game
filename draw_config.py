import pygame
from draw_text_with_color_box import draw_text_with_color_box
from game_config import SequenceConfig


def draw_config(
    screen: pygame.Surface,
    config: list[SequenceConfig],
):
    screen_width, screen_height = pygame.display.get_surface().get_size()

    color_box_size = 40

    spacing = 10

    screen_center_x = screen_width / 2
    screen_center_y = screen_height / 2

    total_height = 40 * len(config)
    start_y = screen_center_y - (total_height / 2)

    for i, sequence_config in enumerate(config):
        y = start_y + i * (color_box_size + spacing)

        draw_text_with_color_box(
            screen,
            color_box_size,
            sequence_config.color,
            f"Length: {sequence_config.length}",
            screen_center_x,
            y,
        )
