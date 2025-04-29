import pyautogui

from 微信ocr import wechat_ocr, OutputType


def capture_and_analyze_mission_detail(region,screenshot_path,destination="花焰群岛",):
    """
    截图指定区域并调用OCR分析结果。
    """
    from Util.util import click_coordinate

    pyautogui.screenshot(
        screenshot_path,
        region=region  # 计算区域宽高
    )
    res_text = wechat_ocr(screenshot_path, OutputType.Detailed)
    print(res_text)
    target_pos = find_target_coordinates(res_text, destination)
    if not target_pos:
        print(f"未找到目标 '{destination}'")
        return None
    print(f"目标 '{destination}' 的坐标为: x={target_pos[0]}, y={target_pos[1]}")
    # click_coordinate(*target_pos)
    return target_pos
def find_target_coordinates(ocr_data, target_text):
    """从OCR结果中查找目标坐标"""
    for item in ocr_data['ocrResult']:
        if target_text in item['text']:
            pos = item['pos']
            return pos['x'], pos['y']  # 直接返回相对截图左上角的坐标
    return None


