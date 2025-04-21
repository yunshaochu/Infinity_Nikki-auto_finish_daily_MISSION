import time
import pyautogui
from Util.util import press_keyboard, wait_image, wait_and_click_image, to_main_menu


class ShopTask:
    def __init__(self):
        pass

    def run(self):
        to_main_menu()
        press_keyboard('h')
        wait_image('return')
        # time.sleep(3)
        wait_and_click_image("weekShop")
        pyautogui.moveTo(1000, 500)
        pyautogui.scroll(-10000)
        wait_and_click_image("freeShop")
        wait_and_click_image("yes")
        to_main_menu()

# 示例用法
if __name__ == "__main__":
    shop_task = ShopTask()
    shop_task.run()