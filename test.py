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

# StarSeaTask().execute()
util.map_jump(coordinates=[
            (1410, 553)  # 传送锚点位置1 主岛
        ], destination="星海")

