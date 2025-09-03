import time

from Util.util import activate_window_by_title, press_keyboard, map_jump, click_coordinate, to_main_menu


class StarSeaTask:


    def share(self):
        # 懒得截图了，直接模拟点击
        press_keyboard("C")
        time.sleep(2)
        click_coordinate(45, 700)
        time.sleep(2)
        click_coordinate(50, 600)
        time.sleep(2)
        click_coordinate(800, 970)
        time.sleep(2)
        click_coordinate(1240, 500)
        to_main_menu()

    def ring(self):
        coordinates = [
            (1410, 553)  # 传送锚点位置
        ]
        map_jump(coordinates=coordinates, destination="星海")
        # 长按E键
        press_keyboard("E", duration=5)

    def execute(self):
        activate_window_by_title("无限暖暖")
        self.share()
        self.ring()


if __name__ == '__main__':
    task = StarSeaTask()
    task.execute()