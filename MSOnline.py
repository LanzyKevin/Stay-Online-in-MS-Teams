import pyautogui
import time

try:
    while True:
        pyautogui.moveRel(0,10)
        time.sleep(5)
except KeyboardInterrupt:
    print("nScript terminated by user.")
  
