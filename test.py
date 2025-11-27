import time

import pyautogui

from Util import NikkiUtil
from task.daily import DailyMissionRecognizer
from task.energy.energy import EnergyTask
from task.photo import PhotoTask
from task.starSea import StarSeaDaily, StarSeaTask

# 初始化工具类实例
util = NikkiUtil()

util.activate_window_by_title()


def _attack_sequence(times):
    for _ in range(times):
        pyautogui.mouseDown()
        time.sleep(0.05)
        pyautogui.mouseUp()


_attack_sequence(10)
