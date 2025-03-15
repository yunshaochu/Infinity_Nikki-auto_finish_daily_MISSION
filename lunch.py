import subprocess
import os
import pyautogui
import time
import pygetwindow as gw

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

    def activate_window_by_title(self, window_title):
        """
        根据窗口标题激活窗口。
        :param window_title: 窗口标题
        """
        try:
            # 查找窗口
            window = gw.getWindowsWithTitle(window_title)
            if window:
                # 激活找到的第一个窗口
                target_window = window[0]
                if not target_window.isActive:
                    target_window.activate()
                    print(f"成功激活窗口: {window_title}")
            else:
                print(f"未找到标题为 '{window_title}' 的窗口。")
        except Exception as e:
            print(f"激活窗口时发生错误: {e}")

    def wait_and_click(self, window_title="无限暖暖"):
        """
        在屏幕上查找图片并点击，同时确保指定窗口已激活。
        :param window_title: 要激活的窗口标题
        """
        print(f"正在寻找图片: {self.image_path}")
        while True:
            try:
                # 激活指定窗口
                self.activate_window_by_title(window_title)

                # 尝试在屏幕上查找图片
                location = pyautogui.locateOnScreen(self.image_path, confidence=0.8)

                # 计算图片中心坐标
                x, y = pyautogui.center(location)

                # 移动鼠标并点击
                pyautogui.click(x, y)
                print("成功点击图片！")
                break  # 点击后退出循环
            except pyautogui.ImageNotFoundException:
                # 若未找到图片，等待一段时间后继续查找
                print("未找到图片，继续检测...")
                time.sleep(self.wait_interval)
            except Exception as e:
                print(f"发生未知错误: {e}")
                break

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
    image_path = "./resource/image/lunch.png"

    # 创建 GameLauncher 实例
    launcher = GameLauncher(exe_path, image_path)

    # 启动游戏并执行相关操作
    launcher.launch_game(window_title="无限暖暖")