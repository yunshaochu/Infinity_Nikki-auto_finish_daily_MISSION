import time
import pyautogui
from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()


class ShopTask:
    def __init__(self):
        pass

    def run(self):
        util.to_main_menu()
        util.press_keyboard('h')
        util.wait_image('return')
        # time.sleep(3)
        # 先尝试直接查找weekShop
        found_week_shop = util.wait_image("weekShop", max_attempts=5)
        if not found_week_shop:
            # 如果没找到weekShop，尝试通过滚动来查找
            start_time = time.time()
            x, y = 180, 625
            pyautogui.moveTo(x, y)
            time.sleep(0.5)
            
            # 在一分钟内持续寻找
            scroll_count = 0
            while time.time() - start_time < 60:
                if util.wait_image("weekShop", max_attempts=1):
                    util.wait_and_click_image("weekShop")
                    found_week_shop = True
                    break
                # 向下滚动一点继续寻找
                pyautogui.scroll(-200)  # 向下滚动
                scroll_count += 1
                time.sleep(0.5)
                
            # 如果最终没有找到，直接返回主菜单
            if not found_week_shop:
                util.to_main_menu()
                return
        else:
            util.wait_and_click_image("weekShop")
        
        pyautogui.moveTo(1000, 500)
        time.sleep(1)
        pyautogui.scroll(-10000)
        pyautogui.scroll(-10000)

        if  util.wait_image("freeShop1", max_attempts=5):
            util.wait_and_click_image("freeShop1")
            util.wait_and_click_image("yes")
            util.click_coordinate(950,40)
            util.click_coordinate(950,40)
            util.click_coordinate(950,40)

        if  util.wait_image("freeShop3", max_attempts=5):
            util.wait_and_click_image("freeShop3")
            util.wait_and_click_image("yes")
            util.click_coordinate(950,40)
            util.click_coordinate(950,40)
            util.click_coordinate(950,40)

        pyautogui.moveTo(1000, 500)
        pyautogui.scroll(2000)

        if  util.wait_image("freeShop2", max_attempts=5):
            util.wait_and_click_image("freeShop2")
            util.wait_and_click_image("yes")
        util.to_main_menu()

# 示例用法
if __name__ == "__main__":
    util.activate_window_by_title()
    shop_task = ShopTask()
    shop_task.run()