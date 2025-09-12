import time

from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()


class DiggingTask:
    def __init__(self):
        pass

    def execute(self):
        print("开始挖掘")
        util.activate_window_by_title()
        util.press_keyboard('esc')
        util.wait_and_click_image('dig')
        if util.wait_image('harvest',max_attempts=10):
            util.wait_and_click_image('harvest')  # 这一句目前不是100%成功
            util.click_coordinate(1800, 770)
            util.wait_and_click_image('dig2')
        util.to_main_menu()