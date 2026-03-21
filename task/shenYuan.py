import time
import pyautogui
from datetime import datetime
from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()


class ShenYuanInnerLoop:
    """深渊内循环"""
    
    def __init__(self):
        pass
    
    def run(self, max_iterations=10):
        """
        执行内循环，最多重复max_iterations次
        
        参数:
            max_iterations: 最大循环次数，默认为10
        """
        for i in range(max_iterations):
            print(f"----------------------------------开始第 {i+1} 次内循环----------------------------------")
            
            # 1. 检查recomand.png是否存在，如果找不到则退出内循环
            print("检查是否有recomand.png...")
            if not util.wait_image("recomand", max_attempts=3):
                print("未找到recomand.png，退出内循环")
                break
            
            # 等待并点击recomand.png，多点几次
            print("等待并点击recomand.png...")
            util.wait_and_click_image("recomand")
            util.wait_and_click_image("recomand")
            util.wait_and_click_image("recomand")
            time.sleep(1)
            
            # 2. 点击10次（194，988）
            print("点击10次坐标（194，988）...")
            for _ in range(10):
                util.click_coordinate(194, 988)
            
            # 3. 什么都不做等待0.5min，直到比赛结束
            print("等待0.5分钟，直到比赛结束...")
            time.sleep(30)
            
            # 4. 等待结束后，不停点击（1377，576），起码10次
            print("不停点击坐标（965，133），至少10次...")
            for _ in range(10):
                util.click_coordinate(965, 133)
                time.sleep(0.2)

            print("不停点击坐标（1377，576），如果recomand出现则提前停止...")
            for _ in range(10):
                util.click_coordinate(1377, 576)
                time.sleep(0.2)
                # 检查是否出现recomand.png，如果出现则提前停止
                if util.wait_image("recomand", max_attempts=1):
                    print("检测到recomand.png，提前停止点击")
                    break
            
            time.sleep(2)
            print(f"----------------------------------第 {i+1} 次内循环完成----------------------------------")


class ShenYuan:
    """深渊任务"""
    
    def __init__(self):
        print("开始深渊任务")
    
    def _outer_loop(self):
        """
        执行外层流程
        """
        print("==================================开始外层流程==================================")
        
        # 1. 回到主界面
        print("回到主界面...")
        util.to_main_menu()
        
        # 2. 按下L键
        print("按下L键...")
        util.press_keyboard('l')
        time.sleep(1)
        
        # 3. 点击（1330，513）
        print("点击坐标（1330，513）...")
        util.click_coordinate(1330, 513)
        
        # 4. 点击（413，449）
        print("点击坐标（413，449）...")
        util.click_coordinate(413, 449)
        time.sleep(1)
        
        # 5. 检查是否有图片getReward.png
        print("检查是否有getReward.png...")
        if not util.wait_image("getReward", max_attempts=3):
            # 如果没有图，回到主界面，重新来过
            print("未找到getReward.png，重新开始外层流程...")
            return False
        
        # 6. 如果有getReward.png，点击这个图片，等待10s
        print("找到getReward.png，点击图片并等待10秒...")
        util.wait_and_click_image("getReward")
        time.sleep(10)
        
        # 7. 多次点击(1225,760)，起码10次
        print("多次点击坐标（1225，760），至少10次...")
        for _ in range(10):
            util.click_coordinate(1225, 760)
        
        # 8. 点击start.png，点击后等待主页面加载出来
        print("点击start.png并等待主页面加载...")
        util.wait_and_click_image("start")
        util.wait_main_menu()
        
        # 9. 主界面加载出来后，按住w向前走4s再松开w
        print("按住w向前走4秒...")
        pyautogui.keyDown('w')
        time.sleep(2)
        pyautogui.keyUp('w')
        
        # 10. 松开w后等待2s，按键盘f。接着不停点击（1377，642），至少10次
        print("等待2秒后按键盘f...")
        time.sleep(2)
        util.press_keyboard('f')
        print("不停点击坐标（1377，642），至少10次...")
        for _ in range(10):
            util.click_coordinate(1377, 642)
        
        print("==================================外层流程完成==================================")
        return True
    
    def run(self):
        """
        执行深渊任务
        """
        # 先尝试执行外层流程
        outer_success = self._outer_loop()
        
        if not outer_success:
            print("外层流程失败，退出深渊任务")
            return
        
        # 开始内循环
        print("开始内循环...")
        inner_loop = ShenYuanInnerLoop()
        inner_loop.run(max_iterations=10)
        
        print("深渊任务执行完成")


def is_shenyuan_day(last_shenyuan_time: str) -> bool:
    """
    判断当前时间是否需要打深渊（每月1号和15号）。
    
    参数:
    - last_shenyuan_time: 字符串格式，表示上次打深渊的时间，比如 "2025-04-19"
    
    返回:
    - 如果需要打深渊（当前日期是1号或15号，且与上次打深渊不是同一天），返回 True；否则返回 False
    """
    if last_shenyuan_time == '':
        return True
    
    now = datetime.now()
    current_day = now.day
    
    # 检查是否是1号或15号
    if current_day not in [1, 15]:
        return False
    
    # 检查是否已经在今天打过深渊了
    last_time = datetime.strptime(last_shenyuan_time, "%Y-%m-%d")
    if last_time.date() == now.date():
        return False
    
    return True


if __name__ == "__main__":
    util.activate_window_by_title()
    # 完整
    # shenyuan = ShenYuan()
    # shenyuan.run()

    # 内层
    inner_loop = ShenYuanInnerLoop()
    inner_loop.run(max_iterations=10)
