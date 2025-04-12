import subprocess
import os
import pyautogui
import time
import pygetwindow as gw

from Util.get_path import get_picture_path
from Util.util import wait_and_click_image


class GameLauncher:
    def __init__(self):
        """
        初始化游戏启动器。
        """
        self.exe_path = r"D:\game\nikki\InfinityNikki Launcher\launcher.exe"


    def launch_game(self):
        """
        启动游戏程序并开始检测图片。
        :param window_title: 游戏窗口标题
        """
        # 检查可执行文件是否存在
        if os.path.exists(self.exe_path):
            try:
                # 启动程序
                subprocess.run([self.exe_path])
                print("程序已启动，开始检测图片...")
            except subprocess.CalledProcessError as e:
                print(f"启动程序时出错: {e}")
            except Exception as e:
                print(f"发生未知错误: {e}")
        else:
            print("指定路径的文件不存在，请检查路径是否正确。")
            return

        # 等待一段时间以确保程序完全加载
        time.sleep(5)

        # 开始检测图片并点击
        try:
            wait_and_click_image("launch")
        except KeyboardInterrupt:
            print("程序被用户中断。")


if __name__ == "__main__":

    # 创建 GameLauncher 实例
    launcher = GameLauncher()

    # 启动游戏并执行相关操作
    launcher.launch_game()