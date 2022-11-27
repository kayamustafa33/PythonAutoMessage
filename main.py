import pyautogui
import time

time.sleep(10)

def message():
    pyautogui.write("Mert")
    pyautogui.press('enter')

while True:
    message()
    time.sleep(0)