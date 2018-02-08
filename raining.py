"""游戏主文件."""
import pygame
from pygame.sprite import Group
import sys

from settings import Settings
from rain_drop import RainDrop
import game_functions as gf


def main():
    pygame.init()
    rains_sets = Settings()
    screen = pygame.display.set_mode((rains_sets.scr_width,
                                      rains_sets.scr_height))
    pygame.display.set_caption("连绵细雨")
    # 初始化一个示例雨滴, 用于获取雨滴的各项指标
    ex_rain_drop = RainDrop(rains_sets, screen)
    rain_drop_width = ex_rain_drop.rect.width
    rain_drop_height = ex_rain_drop.rect.height
    # 初始化雨滴的Group
    rains = Group()
    gf.gen_rains(rains_sets, screen, rains, rain_drop_width, rain_drop_height)
    # 主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(rains_sets.scr_bgcolor)
        # rain_drop.blitme()
        gf.update_rains(rains, rains_sets, screen, rain_drop_width, rain_drop_height)
        rains.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
