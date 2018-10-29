# coding=utf-8
class Settings():
    """ a class to store setting of alien_invasion"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #ship setting
        self.ship_speed_factor = 10
        self.ship_limit =1
        #bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 50
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        #alien setting
        self.alien_speed_factor = 1
        self.flee_drop_speed = 50
        self.flee_direction = 1
