import time

from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()


class PhotoTask:
    def __init__(self):
        pass

    def get_photo(self):
        util.activate_window_by_title()
        util.press_keyboard('p')
        util.wait_image('return')
        util.click_coordinate(1800, 550)

        if util.wait_image('delete'):
            util.wait_and_click_image('delete')
            util.wait_and_click_image('yes4')

        util.to_main_menu()

if __name__ == "__main__":

    # 实例化类并调用方法
    photo_task = PhotoTask()
    photo_task.get_photo()