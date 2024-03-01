import pygame
from draw_arrow import draw_arrow
from game_config import game_colors


def draw_sequence(
    screen: pygame.Surface, sequence: list[pygame.Color], arrow_index: int
):
    sequence_length = len(sequence)

    if sequence_length == 0:
        return

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    padding = 50
    spacing = 10

    circle_radius = (
        (screen_width - (padding * 2) - ((sequence_length - 1) * spacing))
        / sequence_length
        / 2
    )

    circle_radius = min(circle_radius, screen_height / 8)

    for i, color_index in enumerate(sequence):
        x = padding + i * (circle_radius * 2 + spacing) + circle_radius
        pygame.draw.circle(
            screen,
            game_colors[color_index],
            (x, screen_height / 2),
            circle_radius,
        )

    arrow_x = padding + arrow_index * (circle_radius * 2 + spacing) + (spacing / 2)

    center = pygame.Vector2(
        arrow_x,
        screen_height / 2 - 150,
    )

    end = pygame.Vector2(arrow_x, screen_height / 2 - circle_radius)
    draw_arrow(screen, center, end, pygame.Color("dodgerblue"), 10, 20, 12)
