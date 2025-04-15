import time

import pyautogui

from Util.util import press_keyboard, wait_image, click_coordinate, wait_and_click_image, map_jump, to_main_menu, \
    wait_main_menu, activate_window_by_title
from task.monster_trial import MonsterTrialAutomation

coordinates = [
            (1740, 110),
            (1644, 720),
            (630, 170),
            (1400, 625),
            (1600, 1000)
        ]


def locate_minigame(attempts=0):
    map_jump(coordinates)

    # 走到传送锚点面前
    pyautogui.keyDown('a')
    pyautogui.keyDown('w')
    time.sleep(1.4)
    pyautogui.keyUp('a')
    pyautogui.keyUp('w')

    # 进入副本
    press_keyboard('f')
    if wait_image("return", max_attempts=10):
        time.sleep(1.4)
    else:
        if attempts < 3:
            locate_minigame(attempts + 1)
        else:
            print("Failed to locate minigame after 3 attempts.")

# 魔物试炼幻境（280，500）
def enter_monster_trial():
    click_coordinate(280, 500)
    automation = MonsterTrialAutomation()
    automation.run()

# 祝福闪光幻境（500，800）
def enter_blessing_glory():
    click_coordinate(500, 800)

# 素材激化幻境（1500，800），
# 获得的物品（choice_material）:bubble、line、money
# 消耗的物品（choice_consumable）我打算用flower或者fish，这俩很好获得。
def enter_material_activation(choice_material="bubble", choice_consumable="flower"):
    click_coordinate(1500, 800)
    wait_and_click_image("go")
    # wait_image("daMiao")
    wait_main_menu()
    press_keyboard('w', duration=2)
    press_keyboard('f')
    wait_and_click_image(choice_material)
    wait_and_click_image(choice_consumable)
    wait_and_click_image("max")
    wait_and_click_image("yes3")
    wait_and_click_image("material_activation")
    press_keyboard('f')
    press_keyboard('f')
    press_keyboard('f')
    to_main_menu()


# 周本（1600，500）
def enter_weekly_dungeon():
    click_coordinate(1600, 500)
    wait_and_click_image("quickChallenge")
    wait_and_click_image("useEnergy")


activate_window_by_title()
locate_minigame()
enter_material_activation()