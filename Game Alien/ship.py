import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('ship.png')
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def updete(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # +Ограничение перемещений
            # self.rect.centerx += 1
            # Обновляется атрибут center, не rect.
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            # +Ограничение перемещений
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.center = self.screen_rect.centerx
