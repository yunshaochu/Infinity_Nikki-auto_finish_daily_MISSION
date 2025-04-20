import json
from Util.util import map_jump, close_game_window
from task.daily import DailyMissionRecognizer
from task.dig import DiggingTask
from task.energy.energy import EnergyTask
from task.fight import Fight
from task.launch import GameLauncher
from task.minigame import Minigame
from task.photo import PhotoTask
from task.season_pass import SeasonPassTask
from task.shine_levelup import ShineLevelUpTask
from datetime import datetime


def load_task_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def is_new_week(weekly_energy_time: str) -> bool:
    """
    判断当前时间是否和weekly_energy_time不在同一周。

    参数:
    - weekly_energy_time: 字符串格式，表示上次打周本的时间，比如 "2025-04-19"

    返回:
    - 如果不在同一周，返回 True；否则返回 False
    """
    if weekly_energy_time == '':
        return True
    last_time = datetime.strptime(weekly_energy_time, "%Y-%m-%d")
    now = datetime.now()

    last_year, last_week, _ = last_time.isocalendar()
    now_year, now_week, _ = now.isocalendar()

    return (last_year, last_week) != (now_year, now_week)


def main():
    config = load_task_config()

    # 启动游戏
    GameLauncher().launch_game(config["游戏启动路径"])
    # 获取每日任务
    recognizer = DailyMissionRecognizer()
    daily = recognizer.run()
    # 加载任务配置
    task_list = config.get("task_list", [])
    # 总之先挖掘
    DiggingTask().execute()
    energyTask = EnergyTask()
    weekly_energy_time = config["上次打周本的时间"]
    # 如果weekly_energy_time和当前时间相比，不属于同一个星期内，那么返回true。比如2025-4-19是周六，2025-4-20是同一周的周日，那么是false；2025-4-21是不同周的星期一，可以true
    if is_new_week(weekly_energy_time):
        print("可以打周本")
        energyTask.enter_weekly_dungeon()
        #     更新周本时间
        config["上次打周本的时间"] = datetime.now().strftime("%Y-%m-%d")
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
    else:
        print("不可打周本")



    for task in task_list:
        name = task["name"]
        if not task.get("enabled", True):
            continue
        if name not in daily:
            continue

        num = "one"
        # 任务执行
        if name == "魔气怪":
            Fight().run()

        elif name == "小游戏":
            Minigame().walk_to_minigame()

        elif name == "素材激化幻境":
            """
            解释思路：
            素材激化幻境需要消耗体力，如果只是为了做每日任务而不是想刷材料，那就不能吧体力耗光。所以这里加判断，如果想刷的副本(每日体力)刚好就是素材激化幻境，那么num = "max"吧体力刷光，否则只刷一次。
            """
            if "活跃能量" in task_list and 500-recognizer.Finish_data()<=200: # 如果每日任务中有"活跃能量"，且每日任务进度只剩下200了，则不做这个任务了
                continue
            if config["每日体力"] == "素材激化幻境":
                num = "max"
            else:
                num = "one"
            energyTask.enter_material_activation(num=num,choice_material=config["副本设置"]["素材激化幻境"]["获取素材"],choice_consumable=config["副本设置"]["素材激化幻境"]["消耗"])

        elif name == "魔物试炼幻境":
            if "活跃能量" in task_list and 500-recognizer.Finish_data()<=200:
                continue
            if config["每日体力"] == "魔物试炼幻境":
                num = "max"
            else:
                num = "one"
            energyTask.enter_monster_trial(num=num)

        elif name == "祝福闪光幻境":
            if "活跃能量" in task_list and 500-recognizer.Finish_data()<=200:
                continue
            if config["每日体力"] == "祝福闪光幻境":
                num = "max"
            else:
                num = "one"
            energyTask.enter_blessing_glory(num=num)

        elif name == "活跃能量":
            # 如果num是one，说明每日体力还没清；如果是max，说明体力在前三个任务清理完毕了
            if num == "one":
                choose = config["每日体力"]
                energyTask.daily_run(choose,choice_material=config["副本设置"]["素材激化幻境"]["获取素材"],choice_consumable=config["副本设置"]["素材激化幻境"]["消耗"])

        elif name == "提升祝福闪光等级":
            task = ShineLevelUpTask()
            task.execute()

        elif name == "照片":
            PhotoTask().get_photo()

        # 检查是否完成每日活跃度
        if recognizer.isFinish():
            break
    recognizer.get_diamond()
    task = SeasonPassTask()
    task.execute()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        config = load_task_config()
        if config.get("完成每日任务后关闭游戏", False):
            close_game_window()
