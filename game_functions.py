# coding=utf-8
import sys
import pygame
from bullet import Bullet
from alien import Aliens
from time import sleep


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen ,ship,bullets,aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullete(ai_settings, screen, ship,bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(screen,ai_setting,bullets,aliens,ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, aliens, bullets, screen, ship)


def check_bullet_alien_collisions(ai_setting, aliens, bullets, screen, ship):
    collisons = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_flee(screen, ai_setting, aliens, ship)


def fire_bullete(ai_settings,screen,ship,bullets):
    #print(len(bullets))
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_flee(screen,ai_setting,aliens,ship):
    alien = Aliens(screen,ai_setting)
    number_aliens_x = get_number_alien_x(ai_setting,alien.rect.width)
    row_numbers = get_number_rows(ai_setting,alien.rect.height,ship.rect.height)
    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, alien_number, aliens, screen,row_number)


def create_alien(ai_setting, alien_number, aliens, screen,row_number):
    alien = Aliens(screen, ai_setting)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2* row_number* alien.rect.height
    aliens.add(alien)


def get_number_alien_x(ai_setting,alien_width):
    available_space_x = ai_setting.screen_width -2 * alien_width
    number_aliens_x = int(available_space_x/(alien_width*2))
    return number_aliens_x


def get_number_rows(ai_setting, alien_height, ship_height):
    avaiable_space_y = ai_setting.screen_height - ship_height - 3 * alien_height
    number_rows = int(avaiable_space_y / (2 * alien_height))
    return number_rows

def check_flee_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_flee_direction(ai_settings,aliens)
            break

def change_flee_direction(ai_setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.flee_drop_speed
    #先向下平移 然后再反向 margin留出了一个飞碟的距离
    ai_setting.flee_direction *= -1


def update_aliens(stats,ai_setting,screen,aliens,bullets,ship):
    check_flee_edges(ai_setting,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,aliens,bullets,ship,screen,ai_setting)
        return None
    check_aliens_bottom(stats, aliens, bullets, ship, screen, ai_setting)

def ship_hit(stats,aliens,bullets,ship,screen,ai_settings):
    stats.ship_left -= 1
    aliens.empty()
    bullets.empty()
    if stats.ship_left > 0 :
        create_flee(screen,ai_settings,aliens,ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(stats,aliens,bullets,ship,screen,ai_settings):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats,aliens,bullets,ship,screen,ai_settings)
            break
