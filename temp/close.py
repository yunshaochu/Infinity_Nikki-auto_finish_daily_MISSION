import pygetwindow as gw
import time


def close_game_window(window_title="无限暖暖"):
    # 尝试根据标题关闭窗口
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        window.close()
        print(f"已尝试关闭窗口: {window_title}")
        time.sleep(60)
        window = gw.getWindowsWithTitle(window_title)[0]
        window.close()
    except IndexError:
        print(f"未找到窗口: {window_title}")


close_game_window()
