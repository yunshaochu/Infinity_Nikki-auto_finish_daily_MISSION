from Util.util import press_keyboard, wait_image, click_coordinate, to_main_menu, activate_window_by_title

class SeasonPassTask:
    def __init__(self):
        pass

    def execute(self):
        activate_window_by_title()
        print("开始奇迹之旅")
        press_keyboard('j')
        wait_image('return')

        click_coordinate(100,400)
        click_coordinate(100,400)
        click_coordinate(100,400)
        click_coordinate(1255,1000)
        click_coordinate(1255,1000)
        click_coordinate(1255,1000)
        click_coordinate(1255,1000)

        click_coordinate(100,250)
        click_coordinate(100,250)
        click_coordinate(100,250)
        click_coordinate(1255,1000)
        click_coordinate(1255,1000)
        click_coordinate(1255,1000)
        click_coordinate(1255,1000)

        to_main_menu()

if __name__ == "__main__":
    task = SeasonPassTask()
    task.execute()