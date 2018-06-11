# by Brad Lindblad
import time
import pyautogui

i = 0

while i < 100:
    # DELETE OLD COMMENT
    time.sleep(2)
    pyautogui.click(x=470, y=814, clicks=1)  # click the elipses next to comment
    time.sleep(2)
    pyautogui.click(x=433, y=889, clicks=1)  # click delete comment
    time.sleep(2)
    pyautogui.click(x=697, y=532, clicks=1)  # are I sure? Yes I'm sure...
    time.sleep(2)

    # WRITE NEW COMMENT
    pyautogui.click(x=378, y=814, clicks=1)  # select the comment box
    time.sleep(2)
    pyautogui.typewrite(message=".", interval=0.2)
    pyautogui.press('enter')

    # SLEEP
    time.sleep(300)

    i = i + 1
