import pygame

from constants import WHITE


def draw_win_loss_screen(screen: pygame.Surface, won: bool):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    font = pygame.font.Font(None, 60)

    text = "You lost. Press R to restart" if not won else "You won. Press R to restart"

    text = font.render(text, True, WHITE)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height * 0.75))
    screen.blit(text, text_rect)
