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
    # GameLauncher().launch_game(config["游戏启动路径"])
    # 获取每日任务
    recognizer = DailyMissionRecognizer()
    daily = recognizer.run()
    # 加载任务配置
    task_list = config.get("task_list", [])
    # 总之先挖掘
    # DiggingTask().execute()
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
        # 检查是否完成每日活跃度
        if recognizer.isFinish():
            break

    recognizer.get_diamond()
    SeasonPassTask().execute()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        config = load_task_config()
        if config.get("完成每日任务后关闭游戏", False):
            close_game_window()
