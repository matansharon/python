import pygame
from pygame.sprite import Sprite


class alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self._ai_game = ai_game
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.settings = ai_game.settings

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.rect.x < self._ai_game.ship.rect.width + self.settings.screen_width and self._ai_game.edge_flag:
            self.x += (self.settings.alien_speed*self.settings.fleet_direction)
            self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= 1080 or self.rect.left <= 0:
            return True
