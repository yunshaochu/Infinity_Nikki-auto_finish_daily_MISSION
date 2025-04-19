

from Util.util import  map_jump
from task.daily import DailyMissionRecognizer
from task.dig import DiggingTask
from task.energy import EnergyTask
from task.fight import Fight
from task.launch import GameLauncher
from task.minigame import Minigame
from task.photo import PhotoTask

if __name__ == "__main__":

    launcher = GameLauncher()

    # 启动游戏并执行相关操作
    launcher.launch_game()


    recognizer = DailyMissionRecognizer()
    daily = recognizer.run()


    #
    # # 以下随便排序的，之后再认真排
    task = DiggingTask()
    task.execute()
    if "魔气怪" in daily:
        fight = Fight()
        fight.run()
    if "小游戏" in daily:
        locator = Minigame()
        map_jump(locator.coordinates)
        locator.walk_to_minigame()
    if "素材激化幻境" in daily or "活跃能量" in daily:

        task = EnergyTask()
        task.locate_minigame()
        task.enter_material_activation()

    if "魔物试炼幻境" in daily:
        task = EnergyTask()
        task.locate_minigame()
        task.enter_monster_trial()
    if "照片" in daily:
        photo_task = PhotoTask()
        photo_task.get_photo()