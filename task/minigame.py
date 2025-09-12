import pyautogui
import time
import os

from Util.get_path import get_picture_path
from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()


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
        max_attempts = 3  # 最大尝试次数
        attempts = 0
        
        while attempts < max_attempts:
            attempts += 1
            print(f"尝试第 {attempts} 次执行小游戏流程")
            
            util.map_jump(coordinates=self.coordinates, destination="石树田无人区")

            pyautogui.keyDown('a')
            time.sleep(2.3)
            util.press_keyboard('space')
            time.sleep(0.1)
            util.press_keyboard('space')
            time.sleep(11)
            pyautogui.keyUp('a')
            time.sleep(1)
            util.press_keyboard('s', duration=1)
            util.press_keyboard('a', duration=2)
            util.press_keyboard('s', duration=2)
            
            # 调用start_minigame并检查返回值
            result = self.start_minigame()
            if result:  # 如果成功执行则退出循环
                print("小游戏流程执行成功")
                break
            else:
                print(f"第 {attempts} 次尝试失败")
                if attempts >= max_attempts:
                    print("已达到最大尝试次数，结束小游戏流程")
        else:
            print("小游戏流程执行失败，已达到最大尝试次数")

    def start_minigame(self):
        """
        开启小游戏。
        """
        # util.activate_window_by_title()
        util.press_keyboard('f')  # 按下 f 键
        time.sleep(1)  

        # 检查是否出现dialog图片，如果没有则直接结束方法
        if not util.wait_image("dialog", max_attempts=3):
            print("未检测到dialog图片，结束小游戏方法并重新开始")
            return False

        # 不停点击（1420, 700），直到图片 dialog 消失
        while True:
            if not util.wait_image("dialog", max_attempts=1):
                break
            util.click_coordinate(1420, 700)
            print("点击坐标（1420, 700)")
            time.sleep(0.5)

        # 不停按下 f，直到图片 dialog 出现
        while True:
            if util.wait_image("dialog", max_attempts=1):
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

            util.press_keyboard('f') # 推球
            time.sleep(0.1)

        while True:
            # if util.wait_image("daMiao", max_attempts=1):
            #     break
            if util.is_main_menu():
                break
            util.click_coordinate(1446, 760)
            print("点击坐标（1446, 760)")
            time.sleep(0.5)

        return True  # 成功执行


# 实例化并运行小游戏定位
if __name__ == "__main__":
    util.activate_window_by_title()
    locator = Minigame()
    locator.walk_to_minigame()

    # locator.walk_to_minigame()
    # locator.start_minigame()