'''
Uses pyautogui module to click certain buttons on facebook post to keep
it near the top of news feed.
'''

import time
import pyautogui

# X and Y coordinates of the screen positions
comment_ellipses = [470, 814]
delete_comment = [433, 889]
im_sure = [697, 532]
comment_box = [378, 814]
iterations = 2
time_between = 0.2  # in minutes

# LOOP
i = 0

while i < iterations:
    # DELETE OLD COMMENT
    time.sleep(2)
    pyautogui.click(x=comment_ellipses[0], y=comment_ellipses[1], clicks=1)  # click the ellipses next to comment
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
    time.sleep(time_between * 60)  # sleep for 5 minutes

    i = i + 1
print("All done. Re-posted a comment", iterations, "times with a delay of ", time_between, " minutes.")

