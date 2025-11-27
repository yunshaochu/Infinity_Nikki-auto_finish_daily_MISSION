import os
import time

import pyautogui

from Util.get_path import get_image_path, get_picture_path
from Util import NikkiUtil
from task.photo import PhotoTask
from 微信ocr import wechat_ocr, OutputType

# 初始化工具类实例
util = NikkiUtil()


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
                util.click_coordinate(x, y)
                self.capture_and_analyze_mission_detail()
            except Exception as e:
                print(f"处理坐标({x}, {y})时发生错误: {str(e)}")
                continue

    def get_diamond(self):
        self.open_daily_first()
        time.sleep(3)
        util.click_coordinate(1800,675)
        util.click_coordinate(1800,675)
        util.click_coordinate(1800,675)
        # util.press_keyboard('l')
        util.to_main_menu()



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
        keywords = ["星愿","星图绘册","点亮"]
        for text_line in res_text:
            for keyword in keywords:
                if keyword in text_line:
                    self.task_queue.add(keyword)
                    break

    def run(self):
        """
        执行任务检测流程。
        """
        print("开始检测星海日常任务")
        self.open_daily_first()
        self.process_coordinates()
        # util.press_keyboard('l')
        util.to_main_menu()
        print("检测到的任务类型:", self.task_queue)
        return self.task_queue


    def open_daily_first(self):
        """
        打开日常任务1
        :return:
        """
        util.press_keyboard('l')
        util.wait_image('return')
        time.sleep(1)
        util.click_coordinate(550, 750)
        time.sleep(1)
        util.wait_image('return')






class StarSeaTask:

    def __init__(self):
        self.mian_island = [
            (1410, 553)  # 传送锚点位置1 主岛
        ]
        self.beach = [
            (1665, 866)  # 传送锚点位置2 海滩
        ]
        self.center = [
            (72, 616)  # 传送锚点位置3 中心
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
                util.press_keyboard(action['key'])
            elif act == 'wait':
                time.sleep(action['duration'])


    def post_card(self):
        """
        投递心愿信笺
        :return:
        """
        util.map_jump(coordinates=self.beach, destination="星海")
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

        util.press_keyboard('F')
        util.wait_and_click_image('yes_post')
        util.wait_and_click_image("yes4")
        time.sleep(1)
        PhotoTask().get_photo()




    def photo_star_book(self):
        """
        星图绘册拍照，好像能顺便light（）
        :return:
        """
        util.map_jump(coordinates=self.mian_island, destination="星海")
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


            {'type': 'key_down', 'key': 'w'},
            {'type': 'wait', 'duration': 2.5},
            {'type': 'key_up', 'key': 'w'},


        ]
        self._walk(movement_sequence)

        PhotoTask().get_photo()

    # light的功能好像被photo_star_book包括了，所以这个功能被注释掉
    # def light(self):
    #     util.map_jump(coordinates=self.mian_island, destination="星海")
    #     movement_sequence = [
    #         {'type': 'key_down', 'key': 'w'},
    #         {'type': 'key_down', 'key': 'd'},
    #         {'type': 'wait', 'duration': 10},
    #         {'type': 'key_up', 'key': 'd'},
    #         {'type': 'key_up', 'key': 'w'},
    #
    #
    #
    #         {'type': 'key_down', 'key': 'w'},
    #         {'type': 'wait', 'duration': 0.2},
    #         {'type': 'press', 'key': 'space'},
    #         {'type': 'wait', 'duration': 6},
    #         {'type': 'key_up', 'key': 'w'},
    #
    #
    #         {'type': 'key_down', 'key': 'a'},
    #         {'type': 'key_down', 'key': 'space'},
    #         {'type': 'wait', 'duration': 1},
    #         {'type': 'key_up', 'key': 'space'},
    #         {'type': 'wait', 'duration': 4},
    #         {'type': 'press', 'key': 'space'},
    #         {'type': 'wait', 'duration': 4},
    #         {'type': 'key_up', 'key': 'a'},
    #
    #     ]
    #     self._walk(movement_sequence)


    def share(self):
        # 懒得截图了，直接模拟点击
        util.to_main_menu()
        util.press_keyboard("C")
        time.sleep(2)
        util.click_coordinate(45, 700)
        time.sleep(2)
        util.click_coordinate(50, 600)
        time.sleep(2)
        util.click_coordinate(800, 970)
        time.sleep(2)
        util.click_coordinate(1240, 500)

        # 退出到主页面
        util.click_coordinate(1310,350)
        util.click_coordinate(1310,350)
        util.click_coordinate(1310,350)
        util.to_main_menu()

    def ring(self):
        util.to_main_menu()
        util.map_jump(coordinates=self.center, destination="星海")
        # 长按E键
        util.press_keyboard("X", duration=5)
        util.to_main_menu()
        #

    def execute(self):
        util.activate_window_by_title("无限暖暖")

        mission = StarSeaDaily().run()


        self.share()

        if "星图绘册" in mission or "点亮" in mission:
            print("————————————————————————执行星图绘册/点亮任务————————————————————————————")
            self.photo_star_book()
            time.sleep(2)
            self.photo_star_book()
            time.sleep(2)

        if "星愿" in mission:
            print("————————————————————————执行星愿信笺任务————————————————————————————")
            self.post_card()
            time.sleep(2)
            self.post_card()
            time.sleep(2)

        self.ring()

        StarSeaDaily().get_diamond()
        time.sleep(340) # 等待星光凝结


if __name__ == '__main__':
    util.activate_window_by_title("无限暖暖")
    task = StarSeaTask()
    # task.post_card()
    task.photo_star_book()