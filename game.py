"""Simple Tetris-inspired game written with Python and PyGame"""
import pygame
import config


def pre_configure_window():
    """Configure whole stuff around game"""

    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    screen.fill(config.Color.DARKRED.value)
    return screen


def game():
    """Runs whole game"""
    pygame.init()
    screen = pre_configure_window()


if __name__ == "__main__":
    game()
