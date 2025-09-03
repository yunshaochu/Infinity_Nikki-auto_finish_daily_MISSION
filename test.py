import time

import pyautogui

from Util.util import wait_and_click_image, activate_window_by_title, wait_image, map_jump, press_keyboard, \
    click_coordinate, to_main_menu

activate_window_by_title()


# 懒得截图了，直接模拟点击
press_keyboard("C")
time.sleep(2)
click_coordinate(45,700)
time.sleep(2)
click_coordinate(50,600)
time.sleep(2)
click_coordinate(800,970)
time.sleep(2)
click_coordinate(1240,500)


to_main_menu()