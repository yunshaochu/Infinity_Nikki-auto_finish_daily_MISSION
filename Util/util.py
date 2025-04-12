import subprocess
import os
from pathlib import Path

import pyautogui
import time
import pygetwindow as gw

from Util.get_path import get_picture_path


def activate_window_by_title(window_title="无限暖暖"):
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




def wait_image(image_path, wait_interval=0.5, max_attempts=100):
    """
    在屏幕上查找图片并点击，同时确保指定窗口已激活。
    :param window_title: 要激活的窗口标题
    :param max_attempts: 最大尝试次数
    """
    image_path = get_picture_path(image_path)
    print(f"正在寻找图片: {image_path}")
    time.sleep(wait_interval)
    attempts = 0
    while attempts < max_attempts:
        try:
            # 激活指定窗口
            activate_window_by_title()

            # 尝试在屏幕上查找图片
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            print("找到图片！")
            break  # 点击后退出循环
        except pyautogui.ImageNotFoundException:
            # 若未找到图片，等待一段时间后继续查找
            print("未找到图片，继续检测...")
            time.sleep(wait_interval)
        except Exception as e:
            print(f"发生未知错误: {e}")
            break
        attempts += 1
    else:
        print(f"达到最大尝试次数 {max_attempts}，仍未找到图片: {image_path}")

def wait_and_click_image(image_path, wait_interval=1, max_attempts=15):
    """
    在屏幕上查找图片并点击，同时确保指定窗口已激活。
    :param window_title: 要激活的窗口标题
    :param max_attempts: 最大尝试次数
    """
    image_path = get_picture_path(image_path)
    print(f"正在寻找图片: {image_path}")
    time.sleep(wait_interval)
    attempts = 0
    while attempts < max_attempts:
        try:
            # 激活指定窗口
            activate_window_by_title()

            # 尝试在屏幕上查找图片
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            # 计算图片中心坐标
            x, y = pyautogui.center(location)

            pyautogui.mouseDown(x, y)  # 按下鼠标
            time.sleep(0.1)
            pyautogui.mouseUp(x, y)  # 松开鼠标
            print("成功点击图片！")
            break  # 点击后退出循环
        except pyautogui.ImageNotFoundException:
            # 若未找到图片，等待一段时间后继续查找
            print("未找到图片，继续检测...")
            time.sleep(wait_interval)
        except Exception as e:
            print(f"发生未知错误: {e}")
            break
        attempts += 1
    else:
        print(f"达到最大尝试次数 {max_attempts}，仍未找到图片: {image_path}")

def click_coordinate(x, y):
    """
    点击指定坐标，并等待界面加载。
    :param x: 横坐标
    :param y: 纵坐标
    """
    activate_window_by_title()  # 激活目标窗口
    time.sleep(0.1)
    pyautogui.mouseDown(x, y)  # 按下鼠标
    time.sleep(0.1)
    pyautogui.mouseUp(x, y)  # 松开鼠标
    time.sleep(1)  # 等待界面加载

def press_keyboard(key, duration=0.1):
    """
    模拟按下键盘上的某个键。
    :param key: 要按下的键
    :param duration: 按住键的持续时间（秒）
    """
    activate_window_by_title()  # 激活目标窗口
    pyautogui.keyDown(key)
    if duration > 0:
        time.sleep(duration)  # 使用time模块的sleep方法
    pyautogui.keyUp(key)
