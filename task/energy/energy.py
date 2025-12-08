import time

from Util import NikkiUtil
from task.energy.blessing_glory import BlessingGlory
from task.energy.monster_trial import MonsterTrialAutomation

# 初始化工具类实例
util = NikkiUtil()

class EnergyTask:
    def __init__(self):
        # 依次点击的坐标列表
        self.coordinates = [
            (630, 170), # 传送锚点位置
            (1400, 625) # 二级菜单点击位置
        ]




    def open_energy(self, attempts=0):
        """
        打开体力副本
        :return:
        """
        # util.map_jump(coordinates=self.coordinates,destination="石树田无人区")
        util.press_keyboard('l')
        
        # 等待"幻境挑战"图片出现，如果没出现则重试，最多5次
        if not util.wait_image('challenge', max_attempts=10):
            if attempts < 4:  # 最多尝试5次（0-4）
                return self.open_energy(attempts + 1)
            else:
                raise Exception("无法找到'challenge'，已尝试5次")
        
        util.click_coordinate(1200, 250)
        util.wait_image('return')

        # if util.wait_image("return", max_attempts=10):
        #     time.sleep(1.4)
        # else:
        #     if attempts < 3:
        #         self.open_energy(attempts + 1)
        #     else:
        #         print("Failed to locate minigame after 3 attempts.")

    def enter_monster_trial(self, num="one"):
        self.open_energy()
        util.click_coordinate(280, 500)
        automation = MonsterTrialAutomation()
        automation.run(num)
        util.wait_and_click_image("useEnergy")
        util.click_coordinate(1350, 335) # 保险措施，如果此时体力不够/周本次数耗尽，要点击这里关闭页面
        util.click_coordinate(1350, 335) # 保险措施，如果此时体力不够/周本次数耗尽，要点击这里关闭页面
        util.to_main_menu()

    def enter_blessing_glory(self, num="one"):
        self.open_energy()
        util.click_coordinate(500, 800)
        automation = BlessingGlory()
        automation.run(num)
        util.wait_and_click_image("useEnergy")
        util.click_coordinate(1350, 335) # 保险措施，如果此时体力不够/周本次数耗尽，要点击这里关闭页面
        util.click_coordinate(1350, 335) # 保险措施，如果此时体力不够/周本次数耗尽，要点击这里关闭页面
        util.to_main_menu()

    def enter_material_activation(self, num="one", choice_material="bubble", choice_consumable="flower"):
        self.open_energy()
        util.click_coordinate(1500, 800)
        util.wait_and_click_image("go")
        # util.wait_image("daMiao")
        util.wait_main_menu()
        util.press_keyboard('w', duration=2)
        util.press_keyboard('f')
        util.wait_and_click_image(choice_material)
        util.wait_and_click_image(choice_consumable)
        # 选择：要不要把体力全部花费
        if num == "all":
            util.wait_and_click_image("max")
        util.wait_and_click_image("yes3")
        util.wait_and_click_image("material_activation")
        util.press_keyboard('f')
        util.press_keyboard('f')
        util.press_keyboard('f')
        util.click_coordinate(1350, 335) # 保险措施，如果此时体力不够/周本次数耗尽，要点击这里关闭页面
        util.click_coordinate(1350, 335) # 保险措施，如果此时体力不够/周本次数耗尽，要点击这里关闭页面
        util.to_main_menu()

    def enter_weekly_dungeon(self):
        self.open_energy()
        util.click_coordinate(1600, 500)
        time.sleep(3)
        util.click_coordinate(377, 320)
        util.wait_and_click_image("quickChallenge")
        util.wait_and_click_image("useEnergy")
        util.click_coordinate(1350, 335) # 保险措施，如果此时体力不够/周本次数耗尽，要点击这里关闭页面
        util.click_coordinate(1350, 335) # 保险措施，如果此时体力不够/周本次数耗尽，要点击这里关闭页面
        util.to_main_menu()

    def daily_run(self, choose, choice_material="bubble", choice_consumable="fish"):
        if choose == "素材激化幻境":
           self.enter_material_activation(num="all",choice_material=choice_material, choice_consumable=choice_consumable)
        elif choose == "魔物试炼幻境":
            self.enter_monster_trial(num="all")
        elif choose == "祝福闪光幻境":
            self.enter_blessing_glory(num="all")



if __name__ == "__main__":
    task = EnergyTask()
    util.activate_window_by_title()
    task.daily_run("素材激化幻境")