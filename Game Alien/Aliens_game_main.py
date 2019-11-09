
import pygame
from setgame import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group
from stats import GameStats

clock = pygame.time.Clock()

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    # Инициализирует pygame, settings и объект экрана.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Inv")
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
        # for event in pygame.event.get():        # получить доступ к событиям, обнаруженным Pygame
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # gf.check_events(ship)   # замена вышеуказаного цикла на модуль game_function
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.updete()           # запуск движение корабля

        # # заливка фона, при каждом проходе цикла, цветом для удаления следа картинки
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # # Отображение последнего прорисованного экрана.
        # pygame.display.flip()
        # bullets.update()
        #
        # # Удаление пуль, вышедших за край экрана
        # for bullet in bullets.copy():   #копию группы
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # gf.update_bullets(bullets)  # замена вышеуказаного на новую фукцию
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)  # замена вышеуказаного на новую фукцию
        gf.update_aliens(ai_settings, aliens)
        #gf.update_screen(ai_settings, screen, ship, bullets) # заменяем выше обновление экрана модулем gf
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        clock.tick(100)

run_game()


