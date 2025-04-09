import subprocess
import os
import pyautogui
import time
import pygetwindow as gw

from Util.get_path import get_picture_path


class GameLauncher:
    def __init__(self, exe_path, image_path, wait_interval=1):
        """
        初始化游戏启动器。
        :param exe_path: 可执行文件路径
        :param image_path: 图片文件路径
        :param wait_interval: 等待间隔时间（秒）
        """
        self.exe_path = exe_path
        self.image_path = image_path
        self.wait_interval = wait_interval


    def launch_game(self, window_title="无限暖暖"):
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
            self.wait_and_click(window_title)
        except KeyboardInterrupt:
            print("程序被用户中断。")


if __name__ == "__main__":
    # 定义可执行文件路径和图片路径
    exe_path = r"D:\game\nikki\InfinityNikki Launcher\launcher.exe"
    image_path = get_picture_path("launch")

    # 创建 GameLauncher 实例
    launcher = GameLauncher(exe_path, image_path)

    # 启动游戏并执行相关操作
    launcher.launch_game(window_title="无限暖暖")