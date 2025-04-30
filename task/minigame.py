import pyautogui
import time
import os

from Util.get_path import get_picture_path
from Util.util import press_keyboard, click_coordinate, activate_window_by_title, wait_image, map_jump, is_main_menu


class Minigame:
    def __init__(self):
        """
        初始化类实例，设置坐标列表。
        """
        # 依次点击的坐标列表
        self.coordinates = [
            (630, 170), # 传送锚点位置
            (1400, 625) # 二级菜单点击位置
        ]



    def walk_to_minigame(self):
        """
        模拟走路到小游戏的具体位置。
        """
        map_jump(coordinates=self.coordinates,destination="石树田无人区")

        pyautogui.keyDown('a')
        time.sleep(2.3)
        press_keyboard('space')
        time.sleep(0.1)
        press_keyboard('space')
        time.sleep(11)
        pyautogui.keyUp('a')
        time.sleep(1)
        press_keyboard('s', duration=1)
        press_keyboard('a', duration=2)
        press_keyboard('s', duration=2)
        self.start_minigame()

    def start_minigame(self):
        """
        开启小游戏。
        """
        # activate_window_by_title()
        press_keyboard('f')  # 按下 f 键
        time.sleep(1)  



        # 不停点击（1420, 700），直到图片 dialog 消失
        while True:
            if not wait_image("dialog", max_attempts=1):
                break 
            click_coordinate(1420, 700)
            print("点击坐标（1420, 700)")
            time.sleep(0.5)  

        # 不停按下 f，直到图片 dialog 出现
        while True:
            if wait_image("dialog", max_attempts=1):
                break

            try:
                location_retry = pyautogui.locateOnScreen(get_picture_path('retry'), confidence=0.8)
            except Exception as e:
                location_retry = None

            if location_retry:
                x, y = pyautogui.center(location_retry)
                pyautogui.mouseDown(x, y)  # 按下鼠标
                time.sleep(0.1)
                pyautogui.mouseUp(x, y)  # 松开鼠标
                time.sleep(5)
                pyautogui.mouseDown(x, y)  # 按下鼠标
                time.sleep(0.1)
                pyautogui.mouseUp(x, y)  # 松开鼠标
                print("重试小游戏")


            press_keyboard('f') # 推球
            time.sleep(0.1)  

        while True:
            # if wait_image("daMiao", max_attempts=1):
            #     break
            if is_main_menu():
                break
            click_coordinate(1446, 760)
            print("点击坐标（1446, 760)")
            time.sleep(0.5)


# 实例化并运行小游戏定位
if __name__ == "__main__":
    activate_window_by_title()
    locator = Minigame()
    locator.walk_to_minigame()

    # locator.walk_to_minigame()
    # locator.start_minigame()