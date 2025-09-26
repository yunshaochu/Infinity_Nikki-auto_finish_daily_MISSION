import subprocess
import os
import pyautogui
import time
import pygetwindow as gw

from Util.get_path import get_picture_path
from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()


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
        # util.activate_window_by_title()
        if not util.is_main_menu():
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
            util.activate_window_by_title()

            util.wait_and_click_image("launch")
            if util.wait_image("update2",max_attempts=10):
                util.wait_and_click_image("update2")
                util.wait_and_click_image("launch",max_attempts=600)

        time.sleep(10)
        util.activate_window_by_title()

        start_time = time.time()
        count = 0
        while True:
            count += 1
            if count % 4 == 0:
                # pyautogui.hotkey("alt", "tab")
                util.activate_window_by_title()
                if time.time() - start_time > 900:  # 15分钟 后使用更佳的窗口激活方式。但新wxnn使用这种方法老是闪退，还是谨慎用吧
                    util.activate_window_by_title_force()


            found_image = util.wait_images(["update", "yes3", "yes", "launch", "update2"], max_attempts=1)
            if found_image:
                util.wait_and_click_image(found_image)
                if found_image == "update2" or found_image == "update":
                    time.sleep(15)
                    pyautogui.hotkey("alt", "tab")

            if util.is_main_menu():
                break
            util.click_coordinate(900,800)
            time.sleep(0.1)



            # 检查是否超时
            if time.time() - start_time > 1200:  # 20分钟 = 1200秒
                raise TimeoutError("启动游戏超时，超过20分钟未进入主菜单")

if __name__ == "__main__":
    util.activate_window_by_title()
    launcher = GameLauncher()

    launcher.launch_game()