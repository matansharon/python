import pygame


class ship:
    """:a class to represent the alien ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.settings = ai_game.settings

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.x = 200
        self.rect.y = 200
