import os
import time

import pyautogui

from Util.get_path import get_image_path, get_picture_path
from Util.util import click_coordinate, press_keyboard, wait_image, activate_window_by_title
from 微信ocr import wechat_ocr, OutputType



class DailyMissionRecognizer:
    def __init__(self):
        """
        初始化类实例，设置任务队列、坐标列表和截图路径。
        """
        self.task_queue = set()  # 任务队列，用于存储检测到的任务类型
        # 5个日常任务的坐标
        self.coordinates = [
            (540, 650),
            (760, 300),
            (1140, 455),
            (1500, 700),
            (1700, 500)
        ]  
        self.screenshot_path = get_picture_path("mission")  # 截图保存路径
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
        press_keyboard('l')
        wait_image('return')
        time.sleep(3)
        click_coordinate(1210,75)
        click_coordinate(1210,75)
        click_coordinate(1210,75)
        press_keyboard('l')

    def isFinish(self):
        """
        看看每日任务活跃度是否到达500
        """
        press_keyboard('l')
        wait_image('return')
        time.sleep(1)
        pyautogui.screenshot(
            self.screenshot_path,
            region=(985, 90, 1065 - 985, 130 - 90)  # 计算区域宽高
        )
        res_text = wechat_ocr(self.screenshot_path, OutputType.Concise)
        press_keyboard('l')
        if "500" in res_text:
            return True
        else:
            return False


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
        keywords = ["活跃能量", "素材激化幻境", "小游戏", "照片", "祝福闪光", "挖掘", "昆虫", "植物", "魔气怪", "魔物试炼幻境", "服装"]
        for text_line in res_text:
            for keyword in keywords:
                if keyword in text_line:
                    if keyword == "祝福闪光":
                        # 检查是否同时包含“等级”或“幻境”
                        if "等级" in text_line:
                            self.task_queue.add("祝福闪光+等级")
                        elif "幻境" in text_line:
                            self.task_queue.add("祝福闪光+幻境")
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
        press_keyboard('l')
        wait_image('return')
        self.process_coordinates()
        press_keyboard('l')
        print("检测到的任务类型:", self.task_queue)
        return self.task_queue


if __name__ == "__main__":
    activate_window_by_title()
    recognizer = DailyMissionRecognizer()
    # recognizer.run()

    print(recognizer.isFinish())
