# coding=utf-8
import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Aliens
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #init pygame ,setting ,screen object
    pygame.init()
    #initial setting
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Allen_Invasion")

    stats = GameStats(ai_settings)

    button = Button(screen,'Play!')
    scoreboard = Scoreboard(screen,ai_settings,stats)

    ship = Ship(screen,ai_settings)
    bullets = Group()
    #alien = Aliens(screen,ai_settings)
    aliens = Group()
    gf.create_flee(screen, ai_settings, aliens, ship)

    while True:
        gf.check_events(ai_settings,screen,aliens,ship,bullets,stats,button,scoreboard)
        if stats.game_active:
            ship.update()
            gf.update_bullets(screen, ai_settings, bullets, aliens, ship,stats,scoreboard)
            gf.update_aliens(stats, ai_settings, screen, aliens, bullets, ship,scoreboard)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens,button,scoreboard,stats)

run_game()
