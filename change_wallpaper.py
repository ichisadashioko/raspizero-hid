# Download and change wallpaper (Windows 10)
import os
import time
import HID
from HID import CODE

if __name__ == '__main__':
    HID.press(bytes([CODE.LEFT_CTRL, 0, CODE.ESC, *[0] * 5]))
    time.sleep(0.1)
    # open web browser with this URL
    cmd = 'chrome http://www.thecuriosityworkshop.com/wp-content/uploads/2015/03/01-rubberduck-hongkong.jpg'
    HID.type_string(cmd)
    time.sleep(1.0)

    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(5.0)

    HID.press(bytes([CODE.LEFT_CTRL, 0, CODE.KEY_S, *[0] * 5]))
    time.sleep(1.0)
    # save location
    # for Chrome: %USERPROFILE%\Downloads\01-rubberduck-hongkong.jpg
    cmd = '%USERPROFILE%\\Downloads\\01-rubberduck-hongkong.jpg'
    HID.type_string(cmd)
    time.sleep(0.2)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)

    # TAB to move focus to Show all Downloads (Chrome)
    # HID.press(bytes([*[0] * 2, CODE.TAB, *[0] * 5]))
    # time.sleep(0.2)
    # HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))

    # or Ctrl + J
    HID.press(bytes([CODE.LEFT_CTRL, 0, CODE.KEY_J, *[0] * 5]))
    time.sleep(1.0)
    # press tab 2 times to move focus to the latest download
    for _ in range(2):
        HID.press(bytes([*[0] * 2, CODE.TAB, *[0] * 5]))
        time.sleep(0.5)

    # open the image using default Windows image viewer (Photo)
    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(3.0)

    # press tab 11 times
    for _ in range(11):
        HID.press(bytes([*[0] * 2, CODE.TAB, *[0] * 5]))
        time.sleep(0.5)

    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)

    # press down 6 times
    for _ in range(6):
        HID.press(bytes([*[0] * 2, CODE.KEY_DOWN, *[0] * 5]))
        time.sleep(0.5)

    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)

    HID.press(bytes([*[0] * 2, CODE.KEY_DOWN, *[0] * 5]))
    time.sleep(0.5)

    HID.press(bytes([*[0] * 2, CODE.ENTER, *[0] * 5]))
    time.sleep(0.5)

    # close 2 windows
    for _ in range(2):
        HID.press(bytes([CODE.LEFT_ALT, 0, CODE.F4, *[0] * 5]))
        time.sleep(1.0)
