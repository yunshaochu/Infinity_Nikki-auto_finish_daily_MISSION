import time

import pyautogui

from Util.get_path import get_picture_path
from Util.util import press_keyboard, wait_image, click_coordinate, wait_and_click_image

coordinates = [
            (1740, 110),
            (1644, 720),
            (630, 170),
            (1400, 625),
            (1600, 1000)
        ]


def locate_minigame():
    press_keyboard('m')  # 点击键盘上的 m 键
    for x, y in coordinates:
        try:
            wait_image("return")
            click_coordinate(x, y)  # 点击指定坐标
        except Exception as e:
            print(f"处理坐标({x}, {y})时发生错误: {str(e)}")
            continue  # 发生错误继续处理下一个坐标
    wait_image("daMiao")

    # 走到传送锚点面前
    pyautogui.keyDown('a')
    pyautogui.keyDown('w')
    time.sleep(1.4)
    pyautogui.keyUp('a')
    pyautogui.keyUp('w')

    press_keyboard('f')
    wait_image("return")

# 魔物试炼幻境（280，500）
def enter_monster_trial():
    click_coordinate(280, 500)

# 祝福闪光幻境（500，800）
def enter_blessing_glory():
    click_coordinate(500, 800)

# 素材激化幻境（1500，800），
# 获得的物品（choice_material）:bubble、line、money
# 消耗的物品（choice_consumable）我打算用flower或者fish，这俩很好获得。
def enter_material_activation(choice_material="bubble", choice_consumable="flower"):
    click_coordinate(1500, 800)
    wait_and_click_image("go")
    wait_image("daMiao")
    press_keyboard('w', duration=2)
    press_keyboard('f')
    wait_and_click_image(choice_material)
    wait_and_click_image(choice_consumable)
    wait_and_click_image("max")
    wait_and_click_image("yes")



# 周本（1600，500）
def enter_weekly_dungeon():
    click_coordinate(1600, 500)
    wait_and_click_image("quickChallenge")



locate_minigame()
enter_material_activation()