import time

import pyautogui

from Util.util import press_keyboard, wait_image, click_coordinate, wait_and_click_image, map_jump, to_main_menu, \
    wait_main_menu, activate_window_by_title
from task.monster_trial import MonsterTrialAutomation

class EnergyTask:
    def __init__(self):
        self.coordinates = [
            (1740, 110),
            (1644, 720),
            (630, 170),
            (1400, 625),
            (1600, 1000)
        ]

    def locate_minigame(self, attempts=0):
        map_jump(self.coordinates)

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
                self.locate_minigame(attempts + 1)
            else:
                print("Failed to locate minigame after 3 attempts.")

    def enter_monster_trial(self):
        click_coordinate(280, 500)
        automation = MonsterTrialAutomation()
        automation.run()

    def enter_blessing_glory(self):
        click_coordinate(500, 800)

    def enter_material_activation(self, choice_material="bubble", choice_consumable="flower"):
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

    def enter_weekly_dungeon(self):
        click_coordinate(1600, 500)
        wait_and_click_image("quickChallenge")
        wait_and_click_image("useEnergy")




if __name__ == "__main__":
    task = EnergyTask()
    task.locate_minigame()
    task.enter_material_activation()