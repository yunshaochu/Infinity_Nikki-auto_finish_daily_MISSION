import time

from Util.util import press_keyboard, click_coordinate, wait_and_click_image, wait_image, to_main_menu, \
    activate_window_by_title


class PhotoTask:
    def __init__(self):
        pass

    def get_photo(self):
        activate_window_by_title()
        press_keyboard('p')
        wait_image('return')
        click_coordinate(1800, 550)
        to_main_menu()

if __name__ == "__main__":

    # 实例化类并调用方法
    photo_task = PhotoTask()
    photo_task.get_photo()