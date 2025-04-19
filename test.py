import json

from datetime import datetime

from task.daily import DailyMissionRecognizer

recognizer = DailyMissionRecognizer()

print(recognizer.isFinish())