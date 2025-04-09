import os
import pyautogui
import time

from Util.get_path import get_image_path, get_picture_path
from Util.util import activate_window_by_title
from 微信ocr import wechat_ocr, OutputType

# 1. 点击一次L
# 2. 点击（540，650）
# 3. 截图（310，840）到（1570，1000），保存到"./resource/image/mission.png"
# 4. 调用方法 res = wechat_ocr("./resource/image/mission.png", OutputType.Concise)，如果ocr结果（res）包含"活跃能量"，往一个任务队列加入"活跃能量"——对于"素材激化幻境"、"小游戏"、"拍照"做一样的处理

# 接下来，把2的坐标依次换成（760，300）（1140，455）（1500，700）（1700，500），分别执行1到4步骤。




activate_window_by_title()

# 假设OutputType和wechat_ocr已正确导入或定义
# from some_module import OutputType, wechat_ocr

# 定义坐标列表（包含初始坐标和后续四个坐标）
coordinates = [
    (540, 650),
    (760, 300),
    (1140, 455),
    (1500, 700),
    (1700, 500)
]

# 初始化任务队列
task_queue = set()

# 确保截图保存目录存在
os.makedirs(get_image_path(), exist_ok=True)

# 1. 点击L键
pyautogui.keyDown('l')
time.sleep(0.1)
pyautogui.keyUp('l')
time.sleep(1)  # 等待界面响应

for x, y in coordinates:
    try:
        # 2. 点击指定坐标
        pyautogui.mouseDown(x, y)
        time.sleep(0.1)
        pyautogui.mouseUp(x, y)

        time.sleep(1)  # 等待界面加载

        # 3. 截图指定区域
        screenshot_path = get_picture_path("mission")
        pyautogui.screenshot(
            screenshot_path,
            region=(310, 840, 1570 - 310, 1000 - 840)  # 计算区域宽高
        )

        # 4. 调用OCR并分析结果
        res_text = wechat_ocr(screenshot_path, OutputType.Concise)
        print(res_text)

        # 定义关键词列表
        keywords = ["活跃能量", "素材激化幻境", "小游戏", "照片"]

        # 遍历每行文本，检查是否包含关键词
        for text_line in res_text:
            for keyword in keywords:
                if keyword in text_line:
                    task_queue.add(keyword)
                    break  # 如果找到一个关键词，跳出内层循环（避免重复添加）

    except Exception as e:
        print(f"处理坐标({x}, {y})时发生错误: {str(e)}")
        continue  # 发生错误继续处理下一个坐标

# 输出最终任务队列
print("检测到的任务类型:", task_queue)