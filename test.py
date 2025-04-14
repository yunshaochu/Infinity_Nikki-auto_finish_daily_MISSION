import time

import pyautogui

from Util.util import wait_and_click_image, wait_image, activate_window_by_title, map_jump, press_keyboard, \
    click_coordinate, to_main_menu

activate_window_by_title()

wait_image('daMiao')
pyautogui.keyDown('shift')
pyautogui.keyDown('up')
pyautogui.keyDown('w')
pyautogui.keyDown('d')
pyautogui.keyUp('d')
pyautogui.keyUp('w')
pyautogui.keyUp('up')
pyautogui.keyUp('shift')