import os
import pyautogui
import time

from Util.get_path import get_image_path, get_picture_path
from Util.util import activate_window_by_title, click_coordinate, press_keyboard
from 微信ocr import wechat_ocr, OutputType

# 1. 点击一次L
# 2. 点击（540，650）
# 3. 截图（310，840）到（1570，1000），保存到"./resource/image/mission.png"
# 4. 调用方法 res = wechat_ocr("./resource/image/mission.png", OutputType.Concise)，如果ocr结果（res）包含"活跃能量"，往一个任务队列加入"活跃能量"——对于"素材激化幻境"、"小游戏"、"拍照"做一样的处理

# 接下来，把2的坐标依次换成（760，300）（1140，455）（1500，700）（1700，500），分别执行1到4步骤。




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
        for x, y in self.coordinates:
            try:
                click_coordinate(x, y)  # 点击指定坐标
                self.capture_and_analyze()  # 截图并分析OCR结果
            except Exception as e:
                print(f"处理坐标({x}, {y})时发生错误: {str(e)}")
                continue  # 发生错误继续处理下一个坐标



    def capture_and_analyze(self):
        """
        3. 截图指定区域并调用OCR分析结果。
        """
        pyautogui.screenshot(
            self.screenshot_path,
            region=(310, 840, 1570 - 310, 1000 - 840)  # 计算区域宽高
        )
        res_text = wechat_ocr(self.screenshot_path, OutputType.Concise)  # 调用OCR获取文本
        print(res_text)
        self.analyze_ocr_result(res_text)  # 分析OCR结果

    def analyze_ocr_result(self, res_text):
        """
        分析OCR结果，提取任务类型并加入任务队列。
        :param res_text: OCR返回的文本列表
        """
        keywords = ["活跃能量", "素材激化幻境", "小游戏", "照片", "祝福闪光", "挖掘", "昆虫"]
        for text_line in res_text:
            for keyword in keywords:
                if keyword in text_line:
                    if keyword == "祝福闪光":
                        # 检查是否同时包含“等级”或“幻境”
                        if "等级" in text_line:
                            self.task_queue.add("祝福闪光+等级")
                        elif "幻境" in text_line:
                            self.task_queue.add("祝福闪光+幻境")
                    else:
                        self.task_queue.add(keyword)
                    break  # 如果找到一个关键词，跳出内层循环（避免重复添加）

    def run(self):
        """
        执行任务检测流程。
        """
        press_keyboard('l')
        self.process_coordinates()  # 处理坐标列表
        press_keyboard('l')
        print("检测到的任务类型:", self.task_queue)  # 输出最终任务队列


# 实例化并运行任务检测
if __name__ == "__main__":
    recognizer = DailyMissionRecognizer()
    recognizer.run()