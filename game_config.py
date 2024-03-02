import random
import pygame


game_colors = [
    pygame.Color(255, 0, 0),
    pygame.Color(0, 255, 0),
    pygame.Color(0, 0, 255),
    pygame.Color(255, 255, 0),
    pygame.Color(255, 0, 255),
    pygame.Color(0, 255, 255),
]


class SequenceConfig:
    def __init__(self, length: int, color: pygame.Color):
        self.length = length
        self.color = color


def get_game_config() -> list[SequenceConfig]:
    number_of_colors = random.randint(3, 4)

    return [
        SequenceConfig(
            length=random.randint(3, 5),
            color=game_colors[i],
        )
        for i in range(number_of_colors)
    ]
