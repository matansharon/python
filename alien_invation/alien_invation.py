import sys
import pygame
from Setting import Setting
from ship import ship
from Bullet import Bullet
from alien import alien as Alien
from time import sleep
from game_stats import game_stats
from Button import Button


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Setting()
        # the size of the screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_high = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.stats = game_stats(self)
        self.bg_color = self.settings.bg_color  # the color of the background
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.button = Button(self, "play")
        self.create_fleet()
        self.game_over_flag = False
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.edge_flag = True

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.update_movement()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        if self.stats.game_active:
            self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.button.draw_button()
        pygame.display.flip()

    def _check_event(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                # Make the most recently drawn screen visible.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_event(event)

    def _check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_q:

            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
            self.stats.add_shot()
        elif event.key == pygame.K_e:  # a debugging tool to end the game fast
            self.aliens.empty()
            pygame.mouse.set_visible(True)

    def _check_key_up_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_UP:
            self.moving_up = False
        else:
            self.moving_down = False

    def update_movement(self):
        if self.moving_right and self.ship.rect.x < self.settings.screen_high - (self.ship.rect.width - 15):
            self.ship.rect.x += self.settings.speed

        if self.moving_left and self.ship.rect.x > 0:
            self.ship.rect.x -= self.settings.speed
        if self.moving_up and self.ship.rect.y > 0:
            self.ship.rect.y -= self.settings.speed
        if self.moving_down and self.ship.rect.y < 570:
            self.ship.rect.y += self.settings.speed

    def _fire_bullets(self):
        """create a new bullet and add it to the bullet's group"""

        if len(self.bullets) < self.settings.bullets_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bul in self.bullets.copy():
            if bul.rect.bottom <= 0:
                self.bullets.remove(bul)
        self._check_bullet_and_alien_collision()

    def _check_bullet_and_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.stats.add_shot_hit()
        if not self.aliens:
            self.stats.game_active = False
            # self.print_stats()
            self.bullets.empty()
            # self.stats.reset_stats()

    def create_fleet(self):
        # alien = Alien(self)

        # alien_width, alien_height = alien.rect.size
        # ship_height = self.ship.rect.height
        # available_space_y = self.settings.screen_high - (3 * alien_height) - ship_height
        # available_space_x = self.settings.screen_width - (2 * alien_width)
        # number_of_aliens = available_space_x // (2 * alien_width)
        number_of_aliens = 10
        # number_of_rows = available_space_y // (2 * alien_height)
        number_of_rows = 4
        for row in range(number_of_rows):
            # 14 זה רק מספר עבוריץ צריך להשתמש ב number_of_alien
            for alien_number in range(number_of_aliens):
                self.create_alien(alien_number, row)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
        self.aliens.add(alien)

    def _update_aliens(self):
        if self.edge_flag:
            self._check_fleet_edges()
            self.aliens.update()
            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                self._ship_hit()
            self._check_aliens_at_bottom()

    def _ship_hit(self):
        self.stats.ship_lives -= 1
        if self.stats.ship_lives == 0:
            self.print_stats()
            sys.exit()
        self.aliens.empty()
        self.bullets.empty()
        self.create_fleet()
        self.ship.rect.x = self.settings.screen_width / 2
        self.ship.rect.y = 510
        sleep(1)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_at_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= 670:
                self._ship_hit()
                break

    def print_stats(self):
        print("ship lives: {}".format(self.stats.ship_lives))
        print("shots made: {}".format(self.stats.shots_made))
        print("shots hit: {}".format(self.stats.shots_hit))
        print("success rate: {}".format(float(self.stats.shots_hit / self.stats.shots_made) * 100))

    def check_button(self, mouse_pos):
        if self.button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True
            self.stats.reset_stats()
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()
        if self.stats.game_active:
            pygame.mouse.set_visible(False)



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
