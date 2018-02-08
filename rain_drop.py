"""雨滴类"""
import pygame
from pygame.sprite import Sprite


class RainDrop(Sprite):
    """雨滴类"""
    def __init__(self, rains_sets, screen):
        super(RainDrop, self).__init__()
        self.rains_sets = rains_sets
        self.screen = screen
        self.image = pygame.image.load('images/rain_drop.png')
        self.rect = self.image.get_rect()
        # 雨滴初始的(x, y)为(width, height)
        self.rect.x = 0
        self.rect.y = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新雨滴的位置"""
        if self.rect.top < self.rains_sets.scr_height:
            self.rect.y += self.rains_sets.rain_drop_speed
