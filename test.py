from Util.util import wait_and_click_image, is_main_menu, wait_image, wait_images
from task.daily import DailyMissionRecognizer

recognizer = DailyMissionRecognizer()





# print(recognizer.isFinish())
# recognizer.get_diamond()
# wait_image('yes')
# is_main_menu()
found_image = wait_images(["update", "yes3", "yes", "launch", "update2"], max_attempts=100)
print(found_image)
