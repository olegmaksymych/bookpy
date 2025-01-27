import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """General class, that manages the game's resources and behavior."""

    def __init__(self):
        """Initialize the game, create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_hight = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        self.bg_color = (230,230,230)

        self.ship = Ship(self)

    def run_game(self):
        """Start the main cycle of the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            # Redraw the screen at each iteration of the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

    def _check_events(self):
        """Monitor/check the mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        # React on pressing the button
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
    # React when the key is not pressed
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        """Update the image on the screen and switch to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Show the last screen drawn.
        pygame.display.flip()


if __name__ == '__main__':
    # Create the instance and start the game.
    ai = AlienInvasion()
    ai.run_game()
