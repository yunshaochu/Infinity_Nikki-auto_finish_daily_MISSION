import time

import pyautogui

from Util import NikkiUtil
from task.daily import DailyMissionRecognizer
from task.starSea import StarSeaDaily

# 初始化工具类实例
util = NikkiUtil()

util.activate_window_by_title()

# util.wait_and_click_image('巨石岩仔')
# StarSeaDaily().get_diamond()

DailyMissionRecognizer().isFinish()