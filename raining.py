"""游戏主文件."""
import pygame
from pygame.sprite import Group
import sys

from settings import Settings
import game_functions as gf


def main():
    pygame.init()
    rains_sets = Settings()
    screen = pygame.display.set_mode((rains_sets.scr_width,
                                      rains_sets.scr_height))

    # 初始化雨滴的Group
    rains = Group()
    gf.gen_rains(rains_sets, screen, rains)
    # 主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(rains_sets.scr_bgcolor)
        # rain_drop.blitme()
        gf.update_rains(rains, rains_sets)
        rains.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
