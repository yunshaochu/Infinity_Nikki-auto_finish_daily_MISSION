import time

from Util.util import press_keyboard, wait_and_click_image, to_main_menu, activate_window_by_title

activate_window_by_title()

press_keyboard('esc')
wait_and_click_image('dig')

wait_and_click_image('harvest') # 这一句目前不是100%成功

wait_and_click_image('dig2')

to_main_menu()