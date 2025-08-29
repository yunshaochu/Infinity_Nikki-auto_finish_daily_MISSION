import pyautogui

from Util.util import wait_and_click_image, activate_window_by_title, wait_image

activate_window_by_title()


print(wait_image('challenge', max_attempts=10))