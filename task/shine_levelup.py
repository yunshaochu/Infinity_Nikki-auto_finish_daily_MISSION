import time
import pyautogui
from Util.util import press_keyboard, wait_and_click_image, wait_image, click_coordinate, get_picture_path, \
    to_main_menu, activate_window_by_title

class ShineLevelUpTask:
    def __init__(self):
        pass

    def execute(self):
        activate_window_by_title()
        press_keyboard('esc')
        wait_and_click_image('shine')
        wait_image('return')
        click_coordinate(1855, 1020)
        wait_and_click_image('levelup')
        time.sleep(2)
        click_coordinate(1300, 850)
        click_coordinate(125, 200)
        wait_image('add')
        click_coordinate(1055, 460)
        click_coordinate(1055, 460)
        click_coordinate(1055, 460)
        click_coordinate(1055, 460)
        wait_and_click_image('yes3')
        # wait_image("yes3")
        wait_and_click_image('levelup')

        # 返回主页面
        to_main_menu()

if __name__ == "__main__":
    task = ShineLevelUpTask()
    task.execute()