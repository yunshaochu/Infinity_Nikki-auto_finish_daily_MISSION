import time

from Util.util import press_keyboard, click_coordinate, wait_and_click_image, wait_image, to_main_menu

press_keyboard('p')
wait_image('return')
click_coordinate(1800,550)
to_main_menu()