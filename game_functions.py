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


def add_rain_drop(rains_sets, screen, rains, row, line):
    rain_drop = RainDrop(rains_sets, screen)
    rain_drop.rect.x = row * rain_drop.rect.width
    rain_drop.rect.y = line * rain_drop.rect.height
    rains.add(rain_drop)


def gen_rains(rains_sets, screen, rains, rain_drop_width, rain_drop_height):
    """生成一行/多行雨滴"""
    available_rows = cal_available_rows(rains_sets, rain_drop_width)
    available_lines = cal_available_lines(rains_sets, rain_drop_height)
    for line in range(available_lines):
        for row in range(available_rows):
            add_rain_drop(rains_sets, screen, rains, row, line)


def update_rains(rains, rains_sets, screen, rain_drop_width, rain_drop_height):
    rains.update()
    for rain_drop in rains.copy():
        if rain_drop.rect.top >= rains_sets.scr_height:
            rains.remove(rain_drop)
            del rain_drop
    if len(rains) < ((cal_available_rows(rains_sets, rain_drop_width)) *
                     (cal_available_lines(rains_sets, rain_drop_height))):
        for row in range(cal_available_rows(rains_sets, rain_drop_width)):
            add_rain_drop(rains_sets, screen, rains, row, 0)
