import pygame

from constants import WHITE


def draw_text_with_color_box(
    screen: pygame.Surface,
    box_size: float,
    color: pygame.color,
    text: str,
    center_x: float,
    y: float,
) -> pygame.Rect:
    half_box_size = box_size / 2

    font = pygame.font.Font(None, 25)
    text = font.render(text, True, WHITE)

    spacing = 10

    text_rect = text.get_rect(center=(center_x + half_box_size + spacing, y))

    screen.blit(text, text_rect)

    box_left = center_x - half_box_size - (text.get_width() / 2)
    box_top = y - half_box_size

    pygame.draw.rect(
        screen,
        color,
        pygame.Rect(
            (box_left, box_top),
            (box_size, box_size),
        ),
    )

    return pygame.Rect(
        (box_left, box_top), (text_rect.right - box_left + spacing, box_size)
    )
