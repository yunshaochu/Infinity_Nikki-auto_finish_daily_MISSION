import pyautogui
import time
import pygetwindow as gw

from Util.get_path import get_picture_path
from Util.ocr_handle import capture_and_analyze_mission_detail
from 微信ocr import wechat_ocr, OutputType


def map_jump(coordinates, destination="花焰群岛", screenshot_path="map"):
    """
    地图传送
    :param coordinates: 列表，比如
    coordinates = [
            (1740, 110),
            (1644, 720),
            (630, 170),
            (1400, 625),
            (1600, 1000)
        ]

    :param max_retries: 最大重试次数
    """
    print("跳转地图")

    to_main_menu()  # 确保在主菜单界面
    press_keyboard('m')
    if not wait_image("return"):
        press_keyboard('m')

    # 扩大四次地图，缩小一次地图
    click_coordinate(376, 1037)
    click_coordinate(376, 1037)
    click_coordinate(376, 1037)
    click_coordinate(376, 1037)
    click_coordinate(60, 1040)

    click_coordinate(1700, 100)
    # 鼠标移动到（1555，555）
    pyautogui.moveTo(1555, 555)
    # 鼠标滚轮向下滑动1000
    pyautogui.scroll(-1000)

    time.sleep(1)

    screenshot_path = get_picture_path(screenshot_path)
    region = (1300, 100, 1850 - 1300, 1000 - 100) # 截图区域，氛围是将要跳转的地图名称列表
    target_pos = capture_and_analyze_mission_detail(region,screenshot_path,destination)



    if not target_pos:
        click_coordinate(1600, 300)
        time.sleep(1)
        # 鼠标移动到（1555，555）
        pyautogui.moveTo(1555, 555)
        # 鼠标滚轮向下滑动1000
        pyautogui.scroll(-1000)
        target_pos = capture_and_analyze_mission_detail(region,screenshot_path,destination)

    # 把坐标转为相对于屏幕左上角的坐标，1300 100是截图的图片左上角顶点
    target_pos = list(target_pos)
    target_pos[0] = target_pos[0] + 1300
    target_pos[1] = target_pos[1] + 100
    click_coordinate(*target_pos)
    click_coordinate(*target_pos)
    click_coordinate(*target_pos)

    time.sleep(0.5)

    for x, y in coordinates:
        click_coordinate(x, y)
        time.sleep(0.5)

    wait_and_click_image('teleport', max_attempts=5)

    wait_main_menu()


def activate_window_by_title(window_title="无限暖暖"):
    """
    根据窗口标题激活窗口。
    :param window_title: 窗口标题
    """
    try:
        # 查找窗口
        window = gw.getWindowsWithTitle(window_title)
        if window:
            # 激活找到的第一个窗口
            target_window = window[0]
            if not target_window.isActive:
                target_window.activate()
                print(f"成功激活窗口: {window_title}")
        else:
            print(f"未找到标题为 '{window_title}' 的窗口。")
    except Exception as e:
        print(f"激活窗口时发生错误: {e}")




def wait_image(image_path, wait_interval=0.5, max_attempts=100):
    """
    在屏幕上查找图片并点击，同时确保指定窗口已激活。
    :param image_path: 图片路径
    :param wait_interval: 等待间隔时间
    :param max_attempts: 最大尝试次数
    """
    image_path = get_picture_path(image_path)
    print(f"正在寻找图片: {image_path}")
    time.sleep(wait_interval)
    attempts = 0
    result = True
    while attempts < max_attempts:
        try:
            # 激活指定窗口
            # activate_window_by_title()

            # 尝试在屏幕上查找图片
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            print("找到图片！")
            break  # 点击后退出循环
        except pyautogui.ImageNotFoundException:
            # 若未找到图片，等待一段时间后继续查找
            print("未找到图片，继续检测...")
            time.sleep(wait_interval)
        except Exception as e:
            print(f"发生未知错误: {e}")
            result = False
            break
        attempts += 1
    else:
        print(f"达到最大尝试次数 {max_attempts}，仍未找到图片: {image_path}")
        result = False
    return result

def wait_and_click_image(image_path, wait_interval=1, max_attempts=15, press_time=0.1):
    """
    在屏幕上查找图片并点击，同时确保指定窗口已激活。
    :param image_path: 图片路径
    :param wait_interval: 等待间隔时间
    :param max_attempts: 最大尝试次数
    :param press_time: 按住鼠标的时间
    """
    image_path = get_picture_path(image_path)
    print(f"正在寻找图片: {image_path}")
    time.sleep(wait_interval)
    attempts = 0
    while attempts < max_attempts:
        try:
            # 激活指定窗口
            # activate_window_by_title()

            # 尝试在屏幕上查找图片
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            # 计算图片中心坐标
            x, y = pyautogui.center(location)

            pyautogui.mouseDown(x, y)  # 按下鼠标
            if press_time > 0:
                time.sleep(press_time)
            pyautogui.mouseUp(x, y)  # 松开鼠标
            # click_coordinate(x, y)
            print("成功点击图片！")
            break  # 点击后退出循环
        except pyautogui.ImageNotFoundException:
            # 若未找到图片，等待一段时间后继续查找
            print("未找到图片，继续检测...")
            time.sleep(wait_interval)
        except Exception as e:
            print(f"发生未知错误: {e}")
            break
        attempts += 1
    else:
        print(f"达到最大尝试次数 {max_attempts}，仍未找到图片: {image_path}")
    time.sleep(0.5)

def click_coordinate(x, y):
    """
    点击指定坐标，并等待界面加载。
    :param x: 横坐标
    :param y: 纵坐标
    """
    # activate_window_by_title()  # 激活目标窗口
    time.sleep(0.1)
    pyautogui.mouseDown(x, y)  # 按下鼠标
    time.sleep(0.2)
    pyautogui.mouseUp(x, y)  # 松开鼠标
    time.sleep(1)  # 等待界面加载

def press_keyboard(key, duration=0.1):
    """
    模拟按下键盘上的某个键。
    :param key: 要按下的键
    :param duration: 按住键的持续时间（秒）
    """
    # activate_window_by_title()  # 激活目标窗口
    pyautogui.keyDown(key)
    if duration > 0:
        time.sleep(duration)  # 使用time模块的sleep方法
    pyautogui.keyUp(key)


def to_main_menu():
    """
    确保当前界面在主菜单。
    通过不断查找并点击“return”按钮，直到找到“daMiao”图像为止。
    """
    while True:
        result = is_main_menu()
        if result:
            print("已找到 'daMiao' 图像，确认在主菜单界面。")
            break
        else:
            # 如果没有找到“daMiao”图像，点击“return”按钮尝试返回主菜单
            print("未找到 'daMiao' 图像，返回主菜单。")
            # if(wait_image("return",max_attempts=1)):
            #     wait_and_click_image("return")
            # else:
            click_coordinate(70,55)
            click_coordinate(70,55)
            click_coordinate(70,55)
            click_coordinate(70,55)
            click_coordinate(70,55)


def is_main_menu():
    """
    判断当前界面是否在主菜单。
    通过查找“daMiao”图像，如果找到则返回True，否则返回False。
    """
    # 尝试查找“daMiao”图像
    if wait_image("daMiao", max_attempts=1):
        return True

    # 如果未找到“daMiao”，尝试按下“esc”键
    press_keyboard("esc")

    # 再次查找“shine”图像
    if wait_image("shine", max_attempts=2):
        press_keyboard("esc")
        return True

    return False


# 等待主页面加载完毕： 等价于damiao加载完毕（wait_image("daMiao")）。但是daMiao的检测太不稳定了，开发本函数替。
def wait_main_menu(max_retries=100):
    """
    等待主页面加载完毕。
    通过不断查找并点击“return”按钮，直到找到“daMiao”图像为止。
    """
    attempts = 0
    while attempts < max_retries:
        result = is_main_menu()
        if result:
            print("已找到 'daMiao' 图像，确认在主菜单界面。")
            break
        else:
            # 如果没有找到“daMiao”图像，点击“return”按钮尝试返回主菜单
            print("未找到 'daMiao'图像，返回主菜单。")
            click_coordinate(70, 55)
            attempts += 1
    else:
        print(f"达到最大重试次数 {max_retries}，仍未找到主菜单界面。")

def close_game_window(window_title="无限暖暖"):
    # 尝试根据标题关闭窗口
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        window.close()
        print(f"已尝试关闭窗口: {window_title}")
        time.sleep(60)
        window = gw.getWindowsWithTitle(window_title)[0]
        window.close()
    except IndexError:
        print(f"未找到窗口: {window_title}")