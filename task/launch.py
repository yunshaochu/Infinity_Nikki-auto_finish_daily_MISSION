import subprocess
import os
import pyautogui
import time
import pygetwindow as gw

from Util.get_path import get_picture_path
from Util.util import wait_and_click_image, click_coordinate, is_main_menu, activate_window_by_title


class GameLauncher:
    def __init__(self):
        self.exe_path = r"D:\game\nikki\InfinityNikki Launcher\launcher.exe"


    def launch_game(self):
        """
        启动游戏程序并开始检测图片。
        :param window_title: 游戏窗口标题
        """
        print("开始启动游戏")
        activate_window_by_title()
        if not is_main_menu():
            if os.path.exists(self.exe_path):
                try:
                    subprocess.run([self.exe_path])
                    print("程序已启动，开始检测图片...")
                except subprocess.CalledProcessError as e:
                    print(f"启动程序时出错: {e}")
                except Exception as e:
                    print(f"发生未知错误: {e}")
            else:
                print("指定路径的文件不存在，请检查路径是否正确。")
                return

            time.sleep(5)

            # 开始检测图片并点击
            try:
                wait_and_click_image("launch")
            except KeyboardInterrupt:
                print("程序被用户中断。")

        count = 0
        while True:
            count += 1
            if count % 5 == 0:
                activate_window_by_title()

            daMiao = is_main_menu()
            if daMiao:
                break
            click_coordinate(900,900)
            time.sleep(0.1)

if __name__ == "__main__":
    activate_window_by_title()
    launcher = GameLauncher()

    launcher.launch_game()