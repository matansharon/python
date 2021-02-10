class Setting:
    """a setting class to store all setting if the alien invasion """

    def __init__(self):
        """initialize the game's setting"""
        self.screen_width = 800
        self.screen_high = 400
        self.bg_color = (230, 230, 230)
        self.speed = 3
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_limit = 100
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet direction is 1 to go right and -1 to go left
        self.fleet_direction = 1
        self.ship_lives = 3
