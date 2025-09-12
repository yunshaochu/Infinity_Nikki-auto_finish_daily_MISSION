import time
import pyautogui
from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()

class ShineLevelUpTask:
    def __init__(self):
        pass

    def execute(self):
        util.activate_window_by_title()
        util.press_keyboard('esc')
        util.wait_and_click_image('shine')
        util.wait_image('return')
        util.click_coordinate(1855, 1020)
        util.wait_and_click_image('levelup')
        time.sleep(2)
        util.click_coordinate(1300, 850)
        util.click_coordinate(125, 200)
        util.wait_image('add')
        util.click_coordinate(1055, 460)
        util.click_coordinate(1055, 460)
        util.click_coordinate(1055, 460)
        util.click_coordinate(1055, 460)
        util.wait_and_click_image('yes3')
        # util.wait_image("yes3")
        util.wait_and_click_image('levelup')

        # 返回主页面
        util.to_main_menu()

if __name__ == "__main__":
    task = ShineLevelUpTask()
    task.execute()