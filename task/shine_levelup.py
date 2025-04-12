import time

import pyautogui

from Util.util import press_keyboard, wait_and_click_image, wait_image, click_coordinate, get_picture_path

press_keyboard('esc')
wait_and_click_image('shine')
wait_image('return')
click_coordinate(1855,1020)
wait_and_click_image('levelup')
time.sleep(2)
click_coordinate(1300,850)
click_coordinate(125,200)
wait_image('add')
click_coordinate(1055,460)
click_coordinate(1055,460)
click_coordinate(1055,460)
click_coordinate(1055,460)
wait_and_click_image('yes3')
# wait_image("yes3")
wait_and_click_image('levelup')

# 返回主页面
image_path = get_picture_path('daMiao')
while True:
    click_coordinate(70, 50)
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    except Exception as e:
        print(f"没找到图像daMiao")
        location = None
    if location is not None:
        break  # 图片出现，退出循环
