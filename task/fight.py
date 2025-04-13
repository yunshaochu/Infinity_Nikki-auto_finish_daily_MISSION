import time
import pyautogui
from Util.util import press_keyboard, activate_window_by_title, map_jump, wait_image, wait_and_click_image


class Fight:
    def __init__(self):
        pass


    def _walk_to_fight(self, movement_sequence):
        """根据动作序列移动角色"""
        activate_window_by_title()

        for action in movement_sequence:
            act = action.get('type')
            if act == 'key_down':
                pyautogui.keyDown(action['key'])
            elif act == 'key_up':
                pyautogui.keyUp(action['key'])
            elif act == 'press':
                press_keyboard(action['key'])
            elif act == 'wait':
                time.sleep(action['duration'])
            elif act == 'attack':
                self._attack_sequence(action.get('times', 16))
                result = wait_image('daMiao', max_attempts=3)
                # 如果没出现"daMiao"说明死了，点一下复活
                if not result:
                    wait_and_click_image('revive')
                    wait_image('daMiao')

            elif act == 'ultimate':
                self._release_ultimate()

    def _release_ultimate(self):
        pyautogui.keyDown('q')
        pyautogui.mouseDown(button='left')
        time.sleep(0.1)
        pyautogui.mouseUp(button='left')
        pyautogui.keyUp('q')

    def _attack_sequence(self, times):
        for _ in range(times):
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            time.sleep(1)

    def fight_at_location(self, coordinates, movement_sequence):
        map_jump(coordinates)
        self._walk_to_fight(movement_sequence)

    def run(self):
        # 示例点位1
        self.fight_at_location(
            coordinates=[
                (1740, 110),
                (1560, 950),
                (555, 500),
                (1600, 1000)
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
            coordinates=[
                (1740, 110),
                (1560, 950),
                (580, 730),
                (1600, 1000)
            ],
            movement_sequence=[
                {'type': 'key_down', 'key': 'd'},
                {'type': 'wait', 'duration': 17},
                {'type': 'key_up', 'key': 'd'},
                {'type': 'ultimate'},
                {'type': 'attack', 'times': 16}
            ]
        )

        # 绿野微风
        self.fight_at_location(
            coordinates=[
                (1740, 110),
                (1500, 500),
                (1515, 460),
                (1600, 1000)
            ],
            movement_sequence=[
                {'type': 'key_down', 'key': 's'},
                {'type': 'key_down', 'key': 'd'},
                {'type': 'wait', 'duration': 5},
                {'type': 'press', 'key': 'space'},
                {'type': 'wait', 'duration': 20},
                {'type': 'key_up', 'key': 's'},
                {'type': 'key_up', 'key': 'd'},
                {'type': 'key_down', 'key': 'w'},
                {'type': 'wait', 'duration': 4},
                {'type': 'key_up', 'key': 'w'},
                {'type': 'press', 'key': 's'},
                {'type': 'ultimate'},
                {'type': 'attack', 'times': 16}
            ]
        )

        # 小石头树田
        self.fight_at_location(
            coordinates=[
                (1740, 110),
                (1600, 600),
                (560, 200),
                (1600, 1000)
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


if __name__ == "__main__":
    fight = Fight()
    fight.run()
