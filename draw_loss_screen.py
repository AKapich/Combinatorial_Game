import pygame

from constants import WHITE


def draw_loss_screen(screen):
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    font = pygame.font.Font(None, 25)
    text = font.render("You lost. Press R to restart", True, WHITE)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(text, text_rect)
