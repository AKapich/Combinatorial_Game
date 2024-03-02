import pygame

from constants import WHITE


def draw_current_game_state(screen: pygame.Surface, sequence_length: int, n: int):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    font = pygame.font.Font(None, 36)
    text1 = font.render(f"n = {n}", True, WHITE)
    text_rect1 = text1.get_rect()

    text2 = font.render(f"Obecna dlugość sekwencji: {sequence_length}", True, WHITE)
    text_rect2 = text2.get_rect()

    text_rect1.right = text_rect2.right = screen_width - 20
    text_rect1.bottom = screen_height - text_rect2.height - 50
    text_rect2.bottom = screen_height - 20

    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)
