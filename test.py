import time
import json
import pyautogui
import random

from Util import NikkiUtil
from task.daily import DailyMissionRecognizer
from task.energy.energy import EnergyTask
from task.photo import PhotoTask
from task.shenYuan import ShenYuanInnerLoop
from task.starSea import StarSeaDaily, StarSeaTask


n = NikkiUtil()
n.activate_window_by_title()

inner_loop = ShenYuanInnerLoop()
inner_loop.run(max_iterations=7)