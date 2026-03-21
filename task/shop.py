import time
import pyautogui
from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()

FREE_SHOP_ITEMS = ["freeShop1", "freeShop2", "freeShop3"]
# 滚到顶部后，连续多少次没找到任何免费商品则结束
MAX_EMPTY_SCROLLS = 10


class ShopTask:
    def __init__(self):
        pass

    def _find_and_enter_week_shop(self):
        """在商店侧边栏中找到并进入周商店，返回是否成功"""
        util.press_keyboard('h')
        if not util.wait_image('return', max_attempts=10):
            return False

        # 先尝试直接查找
        if util.wait_image("weekShop", max_attempts=3):
            util.wait_and_click_image("weekShop")
            return True

        # 没找到则通过滚动寻找
        pyautogui.moveTo(180, 625)
        time.sleep(0.5)
        start_time = time.time()
        while time.time() - start_time < 60:
            if util.wait_image("weekShop", max_attempts=1):
                util.wait_and_click_image("weekShop")
                return True
            pyautogui.scroll(-200)
            time.sleep(0.5)

        return False

    def _claim_free_item(self):
        """找到一个免费商品并领取，返回是否成功"""
        found = util.wait_images(FREE_SHOP_ITEMS, max_attempts=3)
        if not found:
            return False

        util.wait_and_click_image(found)
        util.wait_and_click_image("yes")
        for _ in range(3):
            util.click_coordinate(950, 40)
        return True

    def _collect_free_items(self):
        """滚到底部后逐页往上滚动，领取所有免费商品"""
        pyautogui.moveTo(1000, 500)
        time.sleep(1)
        pyautogui.scroll(-10000)
        pyautogui.scroll(-10000)

        empty_count = 0
        while empty_count < MAX_EMPTY_SCROLLS:
            if self._claim_free_item():
                empty_count = 0
            else:
                empty_count += 1
                pyautogui.scroll(1000)
                time.sleep(0.5)

    def run(self):
        util.to_main_menu()
        if not self._find_and_enter_week_shop():
            util.to_main_menu()
            return

        self._collect_free_items()
        util.to_main_menu()

# 示例用法
if __name__ == "__main__":
    util.activate_window_by_title()
    shop_task = ShopTask()
    shop_task.run()