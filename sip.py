"""Remind to water plants"""
from win10toast import ToastNotifier
import schedule
import time

from constants import ICON_PATH


def remind() -> None:
   
    toaster = ToastNotifier()
    toaster.show_toast("It is time...", "WATER THE PLANTS!", icon_path=ICON_PATH)
print("CODE IS WORKING NOW WAIT SOMETIME")

schedule.every().day.at("17:09").do(remind)
while True:
    schedule.run_pending()
    time.sleep(1)
