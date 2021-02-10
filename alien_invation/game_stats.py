class game_stats:
    def __init__(self, ai_game):
        self.ship_lives = ai_game.settings.ship_lives
        self.shots_made = 0
        self.shots_hit = 0
        self.settings = ai_game.settings
        self.game_active = False

    def add_shot(self):
        self.shots_made += 1

    def reset_stats(self):
        self.shots_made = 0
        self.shots_hit = 0
        self.ship_lives = self.settings.ship_lives

    def add_shot_hit(self):
        self.shots_hit += 1
