import time
import pyautogui
from Util.util import press_keyboard, wait_image, wait_and_click_image, to_main_menu, click_coordinate


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
        if  wait_image("freeShop1", max_attempts=5):
            wait_and_click_image("freeShop1")
            wait_and_click_image("yes")
            click_coordinate(950,40)
            click_coordinate(950,40)
            click_coordinate(950,40)


        if  wait_image("freeShop2", max_attempts=5):
            wait_and_click_image("freeShop2")
            wait_and_click_image("yes")
        to_main_menu()

# 示例用法
if __name__ == "__main__":
    shop_task = ShopTask()
    shop_task.run()