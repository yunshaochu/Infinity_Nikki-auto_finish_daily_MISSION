import json

from datetime import datetime

from Util.get_path import get_picture_path
from Util.util import close_game_window, wait_image, wait_and_click_image
from task.daily import DailyMissionRecognizer
from task.energy.energy import EnergyTask
from 微信ocr import wechat_ocr, OutputType
def load_task_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
config = load_task_config()

energyTask = EnergyTask()

energyTask.enter_material_activation(num="one", choice_material=config["副本设置"]["素材激化幻境"]["获取素材"],
                                     choice_consumable=config["副本设置"]["素材激化幻境"]["消耗"])

