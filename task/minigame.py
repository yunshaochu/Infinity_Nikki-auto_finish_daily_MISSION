import pyautogui
import time
import os

from Util.get_path import get_picture_path
from Util.util import press_keyboard, click_coordinate, activate_window_by_title, wait_image, map_jump


class Minigame:
    def __init__(self):
        """
        初始化类实例，设置坐标列表。
        """
        # 依次点击的坐标列表
        self.coordinates = [
            (1740, 110),
            (1644, 720),
            (630, 170),
            (1400, 625),
            (1600, 1000)
        ]



    def walk_to_minigame(self):
        """
        模拟走路到小游戏的具体位置。
        """
        activate_window_by_title()
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
        activate_window_by_title()
        press_keyboard('f')  # 按下 f 键
        time.sleep(1)  

        # 获取图片路径
        dialog_path = get_picture_path('dialog')
        if not os.path.exists(dialog_path):
            print(f"文件不存在: {dialog_path}")
            return

        # 不停点击（1420, 700），直到图片 dialog 消失
        while True:
            try:
                location = pyautogui.locateOnScreen(dialog_path, confidence=0.8)
            except Exception as e:
                location = None

            if location is None:
                break 
            click_coordinate(1420, 700)  
            time.sleep(0.5)  

        # 不停按下 f，直到图片 dialog 出现
        while True:
            try:
                location = pyautogui.locateOnScreen(dialog_path, confidence=0.8)
            except Exception as e:
                location = None

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

            if location:
                break

            press_keyboard('f') # 推球
            time.sleep(0.1)  

        daMiao = get_picture_path('daMiao')
        while True:
            try:
                location = pyautogui.locateOnScreen(daMiao, confidence=0.8)
            except Exception as e:
                location = None

            if location:
                break 
            click_coordinate(1446, 760)  
            time.sleep(0.5)  


# 实例化并运行小游戏定位
if __name__ == "__main__":
    locator = Minigame()
    map_jump(locator.coordinates)
    locator.walk_to_minigame()

    # locator.walk_to_minigame()
    # locator.start_minigame()