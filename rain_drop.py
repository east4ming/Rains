"""雨滴类"""
import pygame
from pygame.sprite import Sprite


class RainDrop(Sprite):
    """雨滴类"""
    def __init__(self, screen):
        super(RainDrop, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/rain_drop.png')
        self.rect = self.image.get_rect()
        # 雨滴初始的(x, y)为(width, height)
        self.rect.x = 0
        self.rect.y = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # def update(self, *args):
    #     self.rect.y +=
