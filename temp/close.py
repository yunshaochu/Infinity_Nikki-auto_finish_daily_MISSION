import pygetwindow as gw
import time
import psutil
import win32process  # 需要安装 pywin32
import win32gui  # 需要安装 pywin32


def close_game_process(window_title="无限暖暖"):
    print(f"尝试查找窗口: {window_title}")

    try:
        # 1. 获取窗口对象
        window = gw.getWindowsWithTitle(window_title)[0]

        # 2. 尝试温柔地关闭窗口 (可选，但推荐先尝试)
        # window.close()
        # time.sleep(1) # 等待 1 秒看是否能自己关闭

        # 3. 获取窗口句柄 (HWND)
        # 注意: pygetwindow的window对象在Windows上通常有_hWnd属性
        hwnd = window._hWnd

        # 4. 通过 HWND 获取线程ID和进程ID (PID)
        # 注意: 此处使用了 win32process，是 Windows 特有的 API
        thread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)

        print(f"找到窗口句柄: {hwnd}, 进程ID (PID): {process_id}")

        # 5. 使用 psutil 强制终止进程
        try:
            process = psutil.Process(process_id)
            process.terminate()  # 尝试温和终止
            time.sleep(1)
            if process.is_running():
                process.kill()  # 如果未终止，强制杀死

            print(f"进程已彻底终止: PID {process_id}, 窗口: {window_title}")

        except psutil.NoSuchProcess:
            print(f"进程 PID {process_id} 已终止。")
        except Exception as e:
            print(f"终止进程时发生错误: {e}")

        time.sleep(3)

        # 在一分钟内不断检测窗口，如果有的话就关闭并退出循环
        start_time = time.time()
        while time.time() - start_time < 60:
            windows = gw.getWindowsWithTitle(window_title)
            if windows:
                window = windows[0]
                window.close()
                print(f"在 {int(time.time() - start_time)} 秒后检测到窗口并已关闭")
                break
            time.sleep(1)  # 每秒检测一次

    except IndexError:
        print(f"未找到窗口: {window_title}")
    except Exception as e:
        print(f"操作中发生意外错误: {e}")


# 运行函数
close_game_process()