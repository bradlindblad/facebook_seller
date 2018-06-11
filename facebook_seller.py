''' Info

Args:
    [1]
    [2]

Returns:

'''

comment_elipses = [470, 814]
delete_comment = [433, 889]
im_sure = [697, 532]
comment_box = [378, 814]

import time
import pyautogui

i = 0

while i < 100:
    # DELETE OLD COMMENT
    time.sleep(2)
    pyautogui.click(x=comment_elipses[0], y=comment_elipses[1], clicks=1)  # click the elipses next to comment
    time.sleep(2)
    pyautogui.click(x=delete_comment[0], y=delete_comment[1], clicks=1)  # click delete comment
    time.sleep(2)
    pyautogui.click(x=im_sure[0], y=im_sure[1], clicks=1)  # are I sure? Yes I'm sure...
    time.sleep(2)

    # WRITE NEW COMMENT
    pyautogui.click(x=comment_box[0], y=comment_box[1], clicks=1)  # select the comment box
    time.sleep(2)
    pyautogui.typewrite(message=".", interval=0.2)
    pyautogui.press('enter')

    # SLEEP
    time.sleep(300)  # sleep for 5 minutes

    i = i + 1
