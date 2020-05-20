import os
from typing import Tuple
import pygame

from constants import WHITE, BLACK

"""
    YOU ARE NOT SUPPOSED TO DO CHANGES TO THIS FILE.
    DO THE CHANGES AT YOUR OWN RISK. IT WOULD BE HARD TO THE INSTRUCTORS
    TO PROVIDE SUPPORT ON THE CONTENT OF THIS FILE
"""


def get_event() -> pygame.event:
    return pygame.event.poll()


def load_images() -> Tuple[pygame.Surface, pygame.Surface]:
    """
        This function loads to memory the images needed by our app.
    """
    assets_path = os.path.join(
        os.path.dirname(__file__),
        'assets'
    )
    ball_image = pygame.image.load(
        os.path.join(
            assets_path,
            'ball.png'
        )
    ).convert()
    cross_image = pygame.image.load(
        os.path.join(
            assets_path,
            'cross.png'
        )
    ).convert()
    return ball_image, cross_image


def set_up_screen(width: int = 820, height: int = 800) -> pygame.Surface:
    """
        This function is responsable by initiate the screen.
        It creates the window and setup the background.
    Keyword Arguments:
        width {int} -- [widown width] (default: {820})
        height {int} -- [window height] (default: {800})
    """
    pygame.init()
    pygame.display.set_caption('TicTacToe')
    pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    assets_path = os.path.join(
        os.path.dirname(__file__),
        'assets'
    )
    background_image = pygame.image.load(
        os.path.join(
            assets_path,
            'background.png'
        )
    ).convert()
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])
    pygame.display.flip()
    return screen


def show_image(
    screen: pygame.Surface,
    pos: Tuple[int, int],
    image: pygame.image
):
    screen.blit(image, pos)
    pygame.display.flip()


def show_message(screen: pygame.Surface, message: str):
    # Prepare the Text
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, BLACK, WHITE)
    text_rect = text.get_rect()
    # Center the text on the screen
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    # Show the text
    screen.blit(text, [text_x, text_y])
    pygame.display.flip()
