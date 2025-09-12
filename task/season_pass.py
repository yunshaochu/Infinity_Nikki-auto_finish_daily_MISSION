from Util import NikkiUtil

# 初始化工具类实例
util = NikkiUtil()

class SeasonPassTask:
    def __init__(self):
        pass

    def execute(self):
        util.activate_window_by_title()
        print("开始奇迹之旅")
        util.press_keyboard('j')
        util.wait_image('return')

        util.click_coordinate(100,400)
        util.click_coordinate(100,400)
        util.click_coordinate(100,400)
        util.click_coordinate(1255,1000)
        util.click_coordinate(1255,1000)
        util.click_coordinate(1255,1000)
        util.click_coordinate(1255,1000)

        util.click_coordinate(100,250)
        util.click_coordinate(100,250)
        util.click_coordinate(100,250)
        util.click_coordinate(1255,1000)
        util.click_coordinate(1255,1000)
        util.click_coordinate(1255,1000)
        util.click_coordinate(1255,1000)

        util.to_main_menu()

if __name__ == "__main__":
    task = SeasonPassTask()
    task.execute()