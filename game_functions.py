"""游戏相关的函数."""
from rain_drop import RainDrop


def cal_available_rows(rains_sets, rain_drop_width):
    # 不需要预留空间
    available_space_x = rains_sets.scr_width
    # 因为图片本身上下左右留有空白, 所以密集排列显示效果也不会很密集
    available_rows = available_space_x // rain_drop_width
    return available_rows


def cal_available_lines(rains_sets, rain_drop_height):
    available_space_y = rains_sets.scr_height
    available_lines = available_space_y // rain_drop_height
    return available_lines


def gen_rains(rains_sets, screen, rains):
    """生成一行/多行雨滴"""
    # 初始化一个示例雨滴(用于算width/height)
    ex_rain_drop = RainDrop(screen)
    rain_drop_width = ex_rain_drop.rect.width
    rain_drop_height = ex_rain_drop.rect.height
    available_rows = cal_available_rows(rains_sets, rain_drop_width)
    available_lines = cal_available_lines(rains_sets, rain_drop_height)
    for line in range(available_lines):
        for row in range(available_rows):
            rain_drop = RainDrop(screen)
            rain_drop.rect.x = row * rain_drop_width
            rain_drop.rect.y = line * rain_drop_height
            rains.add(rain_drop)
