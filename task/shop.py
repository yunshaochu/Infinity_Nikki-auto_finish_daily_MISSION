import time
import pyautogui
from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()


class ShopTask:
    def __init__(self):
        pass

    def run(self):
        util.to_main_menu()
        util.press_keyboard('h')
        util.wait_image('return')
        # time.sleep(3)
        util.wait_and_click_image("weekShop")
        pyautogui.moveTo(1000, 500)
        time.sleep(1)
        pyautogui.scroll(-10000)
        pyautogui.scroll(-10000)

        if  util.wait_image("freeShop1", max_attempts=5):
            util.wait_and_click_image("freeShop1")
            util.wait_and_click_image("yes")
            util.click_coordinate(950,40)
            util.click_coordinate(950,40)
            util.click_coordinate(950,40)

        if  util.wait_image("freeShop3", max_attempts=5):
            util.wait_and_click_image("freeShop3")
            util.wait_and_click_image("yes")
            util.click_coordinate(950,40)
            util.click_coordinate(950,40)
            util.click_coordinate(950,40)

        pyautogui.moveTo(1000, 500)
        pyautogui.scroll(800)

        if  util.wait_image("freeShop2", max_attempts=5):
            util.wait_and_click_image("freeShop2")
            util.wait_and_click_image("yes")
        util.to_main_menu()

# 示例用法
if __name__ == "__main__":
    util.activate_window_by_title()
    shop_task = ShopTask()
    shop_task.run()