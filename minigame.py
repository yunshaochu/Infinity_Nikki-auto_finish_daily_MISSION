import pyautogui
import time
import os

from Util.get_path import get_picture_path
from Util.util import press_keyboard, click_coordinate, activate_window_by_title, wait_and_click_image, wait_image


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

    def locate_minigame(self):
        """
        执行点击操作以找到小游戏的位置。
        """
        press_keyboard('m')  # 点击键盘上的 m 键
        wait_image(get_picture_path("return"))
        for x, y in self.coordinates:
            try:
                click_coordinate(x, y)  # 点击指定坐标
            except Exception as e:
                print(f"处理坐标({x}, {y})时发生错误: {str(e)}")
                continue  # 发生错误继续处理下一个坐标
        wait_image(get_picture_path("daMiao"))
        self.walk_to_minigame()

    def walk_to_minigame(self):
        """
        模拟走路到小游戏的具体位置。
        """
        activate_window_by_title()
        pyautogui.keyDown('a')
        time.sleep(2.3)
        press_keyboard('space', duration=0.1)
        time.sleep(0.1)
        press_keyboard('space', duration=0.1)
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
        time.sleep(1)  # 等待一小段时间

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
                break  # 图片消失，退出循环
            click_coordinate(1420, 700)  # 点击坐标
            time.sleep(0.5)  # 等待一小段时间

        # 不停按下 f，直到图片 dialog 出现
        while True:
            try:
                location = pyautogui.locateOnScreen(dialog_path, confidence=0.8)
            except Exception as e:
                location = None

            if location is not None:
                break  # 图片出现，退出循环
            press_keyboard('f')  # 按下 f 键
            time.sleep(0.5)  # 等待一小段时间

        daMiao = get_picture_path('daMiao')
        while True:
            try:
                location = pyautogui.locateOnScreen(daMiao, confidence=0.8)
            except Exception as e:
                location = None

            if location:
                break  # 图片消失，退出循环
            click_coordinate(1446, 760)  # 点击坐标
            time.sleep(0.5)  # 等待一小段时间


# 实例化并运行小游戏定位
if __name__ == "__main__":
    locator = Minigame()
    locator.locate_minigame()
    # locator.walk_to_minigame()
    # locator.start_minigame()