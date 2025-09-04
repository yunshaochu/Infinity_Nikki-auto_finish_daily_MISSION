import os
import time

import pyautogui

from Util.get_path import get_image_path, get_picture_path
from Util.util import activate_window_by_title, press_keyboard, map_jump, click_coordinate, to_main_menu, is_main_menu, \
    wait_and_click_image, wait_image
from 微信ocr import wechat_ocr, OutputType


class StarSeaDaily:
    def __init__(self):
        """
        初始化类实例，设置任务队列、坐标列表和截图路径。
        """
        self.task_queue = set()  # 任务队列，用于存储检测到的任务类型
        # 5个日常任务的坐标
        self.coordinates = [
            (700, 500),
            (900, 500),
            (1100, 500),
            (1350, 500),
            (1570, 500),

        ]
        self.screenshot_path = get_picture_path("mission_sea")  # 截图保存路径
        os.makedirs(get_image_path(), exist_ok=True)  # 确保截图保存目录存在



    def process_coordinates(self):
        """
        遍历坐标列表，依次点击每个坐标并执行任务检测。
        """
        time.sleep(1)
        for x, y in self.coordinates:
            try:
                click_coordinate(x, y)
                self.capture_and_analyze_mission_detail()
            except Exception as e:
                print(f"处理坐标({x}, {y})时发生错误: {str(e)}")
                continue

    def get_diamond(self):
        self.open_daily_first()
        time.sleep(3)
        click_coordinate(1800,675)
        click_coordinate(1800,675)
        click_coordinate(1800,675)
        # press_keyboard('l')
        to_main_menu()



    def capture_and_analyze_mission_detail(self):
        """
        3. 截图指定区域并调用OCR分析结果。
        """
        pyautogui.screenshot(
            self.screenshot_path,
            region=(310, 840, 1570 - 310, 1000 - 840)  # 计算区域宽高
        )
        res_text = wechat_ocr(self.screenshot_path, OutputType.Concise)
        print(res_text)
        self.analyze_ocr_result(res_text)

    def analyze_ocr_result(self, res_text):
        """
        分析OCR结果，提取任务类型并加入任务队列。
        :param res_text: OCR返回的文本列表
        """
        keywords = ["心愿信笺"]
        for text_line in res_text:
            for keyword in keywords:
                if keyword in text_line:
                    if keyword == "祝福闪光":
                        # 检查是否同时包含“等级”或“幻境”
                        if "等级" in text_line:
                            self.task_queue.add("提升祝福闪光等级")
                        elif "幻境" in text_line:
                            self.task_queue.add("祝福闪光幻境")
                    elif keyword == "魔气怪":
                        if "魔物试炼幻境" in text_line:
                            self.task_queue.add("魔物试炼幻境")
                        else:
                            self.task_queue.add(keyword)
                    else:
                        self.task_queue.add(keyword)
                    break

    def run(self):
        """
        执行任务检测流程。
        """
        print("开始检测日常任务")
        self.open_daily_first()
        self.process_coordinates()
        # press_keyboard('l')
        to_main_menu()
        print("检测到的任务类型:", self.task_queue)
        return self.task_queue


    def open_daily_first(self):
        """
        打开日常任务1
        :return:
        """
        press_keyboard('l')
        wait_image('return')
        time.sleep(1)
        click_coordinate(550, 750)
        time.sleep(1)
        wait_image('return')







class StarSeaTask:

    def __init__(self):
        self.mian_island = [
            (1410, 553)  # 传送锚点位置1 主岛
        ]
        self.beach = [
            (1665, 866)  # 传送锚点位置2 海滩
        ]

    def _walk(self, movement_sequence):
        """根据动作序列移动角色"""

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


    def post_card(self):
        """
        投递心愿信笺
        :return:
        """
        map_jump(coordinates=self.beach, destination="星海")
        movement_sequence = [



            {'type': 'key_down', 'key': 's'},
            {'type': 'wait', 'duration': 5.3},
            {'type': 'key_up', 'key': 's'},

            {'type': 'key_down', 'key': 'a'},
            {'type': 'wait', 'duration': 0.5},
            {'type': 'key_up', 'key': 'a'},

            {'type': 'wait', 'duration': 2},

        ]
        self._walk(movement_sequence)

        press_keyboard('F')
        wait_and_click_image('yes_post')
        wait_and_click_image("yes4")




    def light(self):
        map_jump(coordinates=self.mian_island, destination="星海")
        movement_sequence = [
            {'type': 'key_down', 'key': 'w'},
            {'type': 'key_down', 'key': 'd'},
            {'type': 'wait', 'duration': 10},
            {'type': 'key_up', 'key': 'd'},
            {'type': 'key_up', 'key': 'w'},



            {'type': 'key_down', 'key': 'w'},
            {'type': 'wait', 'duration': 0.2},
            {'type': 'press', 'key': 'space'},
            {'type': 'wait', 'duration': 6},
            {'type': 'key_up', 'key': 'w'},


            {'type': 'key_down', 'key': 'a'},
            {'type': 'key_down', 'key': 'space'},
            {'type': 'wait', 'duration': 1},
            {'type': 'key_up', 'key': 'space'},
            {'type': 'wait', 'duration': 4},
            {'type': 'press', 'key': 'space'},
            {'type': 'wait', 'duration': 4},
            {'type': 'key_up', 'key': 'a'},

        ]
        self._walk(movement_sequence)


    def share(self):
        # 懒得截图了，直接模拟点击
        to_main_menu()
        press_keyboard("C")
        time.sleep(2)
        click_coordinate(45, 700)
        time.sleep(2)
        click_coordinate(50, 600)
        time.sleep(2)
        click_coordinate(800, 970)
        time.sleep(2)
        click_coordinate(1240, 500)
        to_main_menu()

    def ring(self):
        to_main_menu()
        map_jump(coordinates=self.mian_island, destination="星海")
        # 长按E键
        press_keyboard("E", duration=5)
        to_main_menu()

    def execute(self):
        activate_window_by_title("无限暖暖")
        self.share()
        self.ring()
        self.light()
        self.post_card()


if __name__ == '__main__':
    activate_window_by_title("无限暖暖")
    task = StarSeaTask()
    task.execute()
    # task.post_card()