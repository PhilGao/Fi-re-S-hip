# coding=utf-8
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #init the ship class
    def __init__(self,screen,ai_settings):
        super(Ship, self).__init__()
        self.screen = screen
        # image init , load image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # image , set position to bottom & center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # store decimal value for ship's center
        self.center = float(self.rect.centerx)
        #flat to moving right or left
        self.moving_right = False
        self.moving_left = False
        # setting information , like speed factor
        self.ai_settings = ai_settings

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.ai_settings.ship_speed_factor
        #here it change the centerx indeed
        self.rect.centerx = self.center


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = float(self.rect.centerx)


