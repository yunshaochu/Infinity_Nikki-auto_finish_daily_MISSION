




from Util.util import  map_jump
from task.daily import DailyMissionRecognizer
from task.dig import DiggingTask
from task.energy import EnergyTask
from task.fight import Fight
from task.launch import GameLauncher
from task.minigame import Minigame
from task.photo import PhotoTask




# 1.每周一次：商店免费礼包，周本

# 2.日常：每完成一个，检查90钻是否到手。支持自定义任务顺序，建议顺序 先做代价低时间短的
# 第一梯队：挖掘
# 第二梯队：小游戏 魔气怪（仅限有八音盒）
# 第三梯队：体力 素材激化幻境 魔物试炼幻境 祝福闪光幻境
# 第四梯队：祝福闪光升级 照片（如果不介意被垃圾照片塞满，可以升级第一梯队）
# 当作空气：制作服装 昆虫 采集


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