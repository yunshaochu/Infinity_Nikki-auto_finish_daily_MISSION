import subprocess
import os
import pyautogui
import time
import pygetwindow as gw

from Util.get_path import get_picture_path
from Util.util import wait_and_click_image, click_coordinate, is_main_menu, activate_window_by_title, wait_image


class GameLauncher:
    def __init__(self):
        self.exe_path = r"D:\game\nikki\InfinityNikki Launcher\launcher.exe"


    def launch_game(self, exe_path=r"D:\game\nikki\InfinityNikki Launcher\launcher.exe"):
        """
        启动游戏程序并开始检测图片。
        :param exe_path:
        :param window_title: 游戏窗口标题
        """
        print("开始启动游戏")
        if exe_path == '':
            exe_path = self.exe_path
        # activate_window_by_title()
        if not is_main_menu():
            if os.path.exists(exe_path):
                try:
                    subprocess.run([exe_path])
                    print("程序已启动，开始检测图片...")
                except subprocess.CalledProcessError as e:
                    print(f"启动程序时出错: {e}")
                except Exception as e:
                    print(f"发生未知错误: {e}")
            else:
                print("指定路径的文件不存在，请检查路径是否正确。")
                return

            time.sleep(5)


            wait_and_click_image("launch")
            if wait_image("update2",max_attempts=10):
                wait_and_click_image("update2")
                wait_and_click_image("launch",max_attempts=600)



        count = 0
        while True:
            count += 1
            if count % 4 == 0:
                activate_window_by_title()
            if wait_image("update", max_attempts=1):
                wait_and_click_image("update")

            if is_main_menu():
                break
            click_coordinate(900,900)
            time.sleep(0.1)

if __name__ == "__main__":
    activate_window_by_title()
    launcher = GameLauncher()

    launcher.launch_game()