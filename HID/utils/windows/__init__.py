# encoding=utf-8
import time

import HID
import HID.CODE


def open_run():
    HID.press(bytes([HID.CODE.LEFT_GUI, 0, HID.CODE.KEY_R, *[0] * 5]))


def command_prompt(run_as=False):
    open_run()
    time.sleep(0.2)
    if run_as:
        HID.type_string('powershell Start-Process cmd -Verb runAs')
        time.sleep(1.5)
        HID.type_string('\n')
        time.sleep(5.0)
        HID.press(bytes([HID.CODE.LEFT_ALT, 0, HID.CODE.KEY_Y, *[0] * 5]))
    else:
        HID.type_string('cmd\n')
