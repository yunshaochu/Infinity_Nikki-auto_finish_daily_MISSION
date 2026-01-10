import time
import pyautogui
import json
from Util.get_path import get_picture_path, get_config_path
from Util import NikkiUtil
from 微信ocr import wechat_ocr

# 初始化工具类实例
util = NikkiUtil()

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
                return pos['x'], pos['y']  # 直接返回调整后的坐标
        return None

    def _prepare_environment(self):
        """环境准备工作"""
        # util.activate_window_by_title()
        if self.monster == "贪婪囚鸟":
            util.click_coordinate(375, 200)
            time.sleep(0.5)

    def _process_ocr(self):
        """处理OCR识别流程"""
        # 全屏截图
        screenshot_path = get_picture_path("monster_trial_temp")
        pyautogui.screenshot(screenshot_path)
        # 对截图进行OCR
        self.ocr_results = wechat_ocr(screenshot_path)

    def _execute_actions(self,num):
        """执行自动化操作序列"""
        # 0. 鼠标放到(456, 532)，滚轮向上滚10000，确保回到顶部
        pyautogui.moveTo(456, 532)
        pyautogui.scroll(10000)
        time.sleep(0.5)

        # 1-3. 滚动查找目标
        max_attempts = 10  # 最大滚动次数
        scroll_amount = int(1080 * 0.75)  # 3/4屏幕高度（假设1080p）

        for attempt in range(max_attempts):
            # 进行OCR识别
            self._process_ocr()

            # 查找目标坐标
            target_pos = self.find_target_coordinates(self.ocr_results, self.target)

            if target_pos:
                # 3. 找到了，点击目标位置打开对应的标签页
                print(f"目标 '{self.target}' 的坐标为: x={target_pos[0]}, y={target_pos[1]}")
                util.click_coordinate(*target_pos)
                break
            else:
                print(f"第 {attempt + 1} 次未找到目标 '{self.target}'，向下滚动...")
                # 2. 向下滚动一定幅度
                pyautogui.moveTo(456, 532)
                pyautogui.scroll(-scroll_amount)
                time.sleep(0.5)
        else:
            # 达到最大滚动次数仍未找到
            print(f"达到最大滚动次数 {max_attempts}，未找到目标 '{self.target}'")
            return

        # 4. 正常执行后续操作
        util.wait_and_click_image("quickChallenge")
        if num == "all":
            util.wait_and_click_image("max")

    def run(self,num):
        """执行完整自动化流程"""
        # self._prepare_environment()
        self._execute_actions(num)


if __name__ == "__main__":
    util.activate_window_by_title()
    automation = MonsterTrialAutomation()
    automation.run("one")