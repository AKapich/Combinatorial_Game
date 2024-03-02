import pygame

from constants import WHITE


def draw_current_game_state(screen: pygame.Surface, sequence_length: int, n: int):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    right_edge = screen_width - 20

    font = pygame.font.Font(None, 36)
    text1 = font.render(f"n = {6}", True, WHITE)
    text_size1 = text1.get_rect()
    text_rect1 = text1.get_rect(
        center=(screen_width - text_size1[0], screen_height - 60)
    )

    # text2 = font.render(f"Obecna dlugość sekwencji: {sequence_length}", True, WHITE)
    # text_rect2 = text2.get_rect()
    # text_rect2.right = right_edge

    # text_rect1.bottom = screen_height - text_rect2.height
    # text_rect2.bottom = text_rect1.bottom + 10

    screen.blit(text1, text_rect1)
    # screen.blit(text2, text_rect2)
