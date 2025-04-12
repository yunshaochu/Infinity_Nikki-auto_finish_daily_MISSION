import time
import pyautogui
from Util.get_path import get_picture_path
from Util.util import press_keyboard, wait_image, click_coordinate, activate_window_by_title


class Fight:
    def __init__(self):
        pass

    def _navigate_coordinates(self, coordinates):
        """内部方法：执行坐标导航核心流程"""
        press_keyboard('m')
        wait_image("return")

        for x, y in coordinates:
            try:
                click_coordinate(x, y)
                if x == 1740 and y == 110:
                    try:
                        location = pyautogui.locateOnScreen(get_picture_path('navigate'), confidence=0.8)
                    except Exception as e:
                        print(f"没找到图像daMiao")
                        location = None
                    if location is None:
                        click_coordinate(x, y)
                time.sleep(0.5)
            except Exception as e:
                print(f"处理坐标({x}, {y})时发生错误: {str(e)}")
                continue

        wait_image("daMiao")

    def _execute_walk_actions(self, duration):
        """内部方法：执行行走相关操作"""
        activate_window_by_title()

        # 横向移动
        pyautogui.keyDown('d')
        time.sleep(duration)
        pyautogui.keyUp('d')

        # 释放大招
        pyautogui.keyDown('q')
        pyautogui.mouseDown(button='left')
        time.sleep(0.1)
        pyautogui.mouseUp(button='left')
        pyautogui.keyUp('q')

        # 连击操作
        for _ in range(16):
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            time.sleep(1)

    def locate_fight_v1(self):
        """版本1的定位战斗流程"""
        coordinates = [
            (1740, 110),
            (1560, 950),
            (555, 500),
            (1600, 1000)
        ]
        self._navigate_coordinates(coordinates)
        self._execute_walk_actions(6)

    def locate_fight_v2(self):
        """版本2的定位战斗流程"""
        coordinates = [
            (1740, 110),
            (1560, 950),
            (580, 730),
            (1600, 1000)
        ]
        self._navigate_coordinates(coordinates)
        self._execute_walk_actions(17)

    def run(self):
        self.locate_fight_v1()
        self.locate_fight_v2()


# 使用示例
if __name__ == "__main__":
    navigator = Fight()
    navigator.run()