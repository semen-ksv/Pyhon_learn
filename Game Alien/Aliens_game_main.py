import pygame
from setgame import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group
from stats import GameStats
from button import Button
from score_board import Score

clock = pygame.time.Clock()


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    # Инициализирует pygame, settings и объект экрана.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Inv")
    play_button = Button(ai_settings, screen, "Play")
    # Создание экземпляров GameStats и Score.
    stats = GameStats(ai_settings)
    score = Score(ai_settings, screen, stats)
    # bg_color = (200, 200, 200)
    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullets = Group()
    # # Создание пришельца
    alien = Alien(ai_settings, screen)
    # Создание флота пришельцев.
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, score, play_button, ship, aliens, bullets)
        if stats.game_active:
            # запуск движение корабля
            ship.updete()
            gf.update_bullets(ai_settings, screen, stats, score, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, score, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, score, ship, aliens, bullets, play_button)
            clock.tick(100)


run_game()
