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

# pyautogui.keyDown('tab')
# time.sleep(1)
# pyautogui.click(750, 150)
# time.sleep(1)
# pyautogui.click(750, 150)
# time.sleep(0.2)
# pyautogui.keyUp('tab')

recognizer = DailyMissionRecognizer()
print(recognizer.isFinish())
