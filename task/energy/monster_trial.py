import time
import pyautogui
import json
from Util.get_path import get_picture_path, get_config_path
from Util.util import activate_window_by_title, click_coordinate, wait_and_click_image
from 微信ocr import wechat_ocr

# 魔物试炼幻境
class MonsterTrialAutomation:
    def __init__(self):
        self.config_path = get_config_path()
        self.config = self._load_config()
        self.monster = self.config['副本设置']['魔物试炼幻境']['怪物']
        self.target = self.config['副本设置']['魔物试炼幻境']['副本']
        self.ocr_results = None

    def _load_config(self):
        """加载配置文件"""
        with open(self.config_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def find_target_coordinates(ocr_data, target_text):
        """从OCR结果中查找目标坐标"""
        for item in ocr_data['ocrResult']:
            if target_text in item['text']:
                pos = item['pos']
                return pos['x'] + 100, pos['y'] + 160  # 直接返回调整后的坐标
        return None

    def _prepare_environment(self):
        """环境准备工作"""
        # activate_window_by_title()
        if self.monster == "贪婪囚鸟":
            click_coordinate(375, 200)
            time.sleep(0.5)

    def _process_ocr(self):
        """处理OCR识别流程"""
        image_path = get_picture_path(self.monster)
        self.ocr_results = wechat_ocr(image_path)

    def _execute_actions(self,num):
        """执行自动化操作序列"""
        target_pos = self.find_target_coordinates(self.ocr_results, self.target)

        if not target_pos:
            print(f"未找到目标 '{self.target}'")
            return

        print(f"目标 '{self.target}' 的坐标为: x={target_pos[0]}, y={target_pos[1]}")
        click_coordinate(*target_pos)
        wait_and_click_image("quickChallenge")
        if num == "all":
            wait_and_click_image("max")
        wait_and_click_image("useEnergy")

    def run(self,num):
        """执行完整自动化流程"""
        self._prepare_environment()
        self._process_ocr()
        self._execute_actions(num)


if __name__ == "__main__":
    activate_window_by_title()
    automation = MonsterTrialAutomation()
    automation.run("one")