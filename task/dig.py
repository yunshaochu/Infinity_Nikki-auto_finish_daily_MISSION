import time

from Util.util import press_keyboard, wait_and_click_image, to_main_menu, activate_window_by_title, click_coordinate


class DiggingTask:
    def __init__(self):
        pass

    def execute(self):
        print("开始挖掘")
        activate_window_by_title()
        press_keyboard('esc')
        wait_and_click_image('dig')
        wait_and_click_image('harvest')  # 这一句目前不是100%成功
        # wait_and_click_image('harvest') # 这一句目前不是100%成功
        click_coordinate(1800, 770)
        wait_and_click_image('dig2')
        to_main_menu()


if __name__ == "__main__":
    task = DiggingTask()
    task.execute()