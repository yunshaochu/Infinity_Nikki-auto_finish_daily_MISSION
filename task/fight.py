import time
import pyautogui
from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()


class Fight:
    def __init__(self):
        print("开始战斗")
        pass


    def _walk_to_fight(self, movement_sequence):
        """根据动作序列移动角色"""

        for action in movement_sequence:
            act = action.get('type')
            if act == 'key_down':
                pyautogui.keyDown(action['key'])
            elif act == 'key_up':
                pyautogui.keyUp(action['key'])
            elif act == 'press':
                util.press_keyboard(action['key'])
            elif act == 'wait':
                time.sleep(action['duration'])
            elif act == 'attack':
                self._attack_sequence(action.get('times', 30))
                # result = util.wait_image('daMiao',max_attempts=10)
                result = util.is_main_menu()
                # 如果没出现"daMiao"说明死了，点一下复活
                if not result:
                    util.wait_and_click_image('revive')
                    util.wait_image('daMiao')
            elif act == 'ultimate':
                self._release_ultimate()

    def _release_ultimate(self):

        # 蛇形走位：注意，必须同时按住shift和up（或者任意方向键）才能冲刺
        pyautogui.keyDown('shift')
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')
        pyautogui.keyUp('shift')

        pyautogui.keyDown('q')
        pyautogui.mouseDown(button='left')
        time.sleep(0.1)
        pyautogui.mouseUp(button='left')
        pyautogui.keyUp('q')

        # 如果开启了大招动画，开大后一瞬间是没有daMiao的，如何有说明开大失败了，再开一次
        # if not util.wait_image('daMiao', max_attempts=1):
        #     pyautogui.keyDown('q')
        #     pyautogui.mouseDown(button='left')
        #     time.sleep(0.1)
        #     pyautogui.mouseUp(button='left')
        #     pyautogui.keyUp('q')

    def _attack_sequence(self,times):
        for _ in range(times):
            pyautogui.mouseDown()
            time.sleep(0.05) # 如果是弓箭，就要0.05s
            pyautogui.mouseUp()
            time.sleep(0.2)

    def fight_at_location(self, coordinates, destination, movement_sequence):
        util.map_jump(coordinates=coordinates,destination=destination)
        print("开始寻路")
        self._walk_to_fight(movement_sequence)

    def run(self):
        """

        coordinates 写传送点在地图上的坐标
        :return:
        """
        # 1. 开启八音盒：在按下tab键之后，等待1s，点击坐标（1175，150），松开tab
        pyautogui.keyDown('tab')
        time.sleep(1)
        pyautogui.click(1175, 150)
        time.sleep(0.5)
        pyautogui.click(1175, 150)
        time.sleep(0.1)
        pyautogui.keyUp('tab')



        # 示例点位1
        self.fight_at_location(
            destination = "花焰群岛",
            coordinates=[
                (555, 500)
            ],
            movement_sequence=[
                {'type': 'key_down', 'key': 'd'},
                {'type': 'wait', 'duration': 6},
                {'type': 'key_up', 'key': 'd'},
                {'type': 'ultimate'},
                {'type': 'attack', 'times': 16}
            ]
        )

        # 示例点位2
        self.fight_at_location(
            destination = "花焰群岛",
            coordinates=[
                (580, 730)
            ],
            movement_sequence=[
                {'type': 'key_down', 'key': 'd'},
                {'type': 'wait', 'duration': 17},
                {'type': 'key_up', 'key': 'd'},
                {'type': 'ultimate'},
                {'type': 'attack', 'times': 16}
            ]
        )

        # 小石树田
        self.fight_at_location(
            destination="小石树田村",
            coordinates=[
                (560, 200)
            ],
            movement_sequence=[
                {'type': 'key_down', 'key': 'a'},
                {'type': 'key_down', 'key': 's'},
                {'type': 'wait', 'duration': 4},
                {'type': 'key_up', 'key': 'a'},
                {'type': 'key_up', 'key': 's'},
                {'type': 'ultimate'},
                {'type': 'attack', 'times': 16}
            ]
        )

        # 2. 关闭八音盒：在按下tab键之后，等待1s，点击坐标（750，150），松开tab
        pyautogui.keyDown('tab')
        time.sleep(1)
        pyautogui.click(750, 150)
        pyautogui.keyUp('tab')


if __name__ == "__main__":
    util.activate_window_by_title()
    fight = Fight()
    fight.run()