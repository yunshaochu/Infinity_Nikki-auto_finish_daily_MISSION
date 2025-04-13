from Util.util import wait_and_click_image, wait_image, activate_window_by_title, map_jump, press_keyboard, \
    click_coordinate

activate_window_by_title()

press_keyboard('m')
wait_image("return")

# 扩大四次地图，缩小一次地图
click_coordinate(376, 1037)
click_coordinate(376, 1037)
click_coordinate(376, 1037)
click_coordinate(376, 1037)
click_coordinate(60, 1040)
