# encoding=utf-8
import os
import time

from tqdm import tqdm

import HID
import HID.CODE


def open_run():
    # press Left Start + R
    HID.press(bytes([HID.CODE.LEFT_GUI, 0, HID.CODE.KEY_R, *[0] * 5]))


def command_prompt(run_as=False):
    open_run()
    time.sleep(0.2)
    if run_as:
        HID.type_string('powershell Start-Process cmd -Verb runAs')
        time.sleep(1.5)
        # Press Enter
        HID.type_string('\n')
        time.sleep(5.0)
        # press Left Alt + Y
        HID.press(bytes([HID.CODE.LEFT_ALT, 0, HID.CODE.KEY_Y, *[0] * 5]))
    else:
        HID.type_string('cmd\n')


def notepad(gui_wait=0.25):
    """Open Windows notepad."""
    open_run()
    time.sleep(gui_wait)
    HID.type_string('notepad\n')


def save_notepad(filename: str, gui_wait=0.5):
    HID.press(bytes([HID.CODE.LEFT_CTRL, 0, HID.CODE.KEY_S, *[0] * 5]))
    time.sleep(gui_wait)
    HID.type_string(filename)
    HID.press(bytes([0, 0, HID.CODE.ENTER, *[0] * 5]))


def type_file_to_notepad(filepath: str, close=True, gui_wait=0.5):
    assert os.path.exists(filepath)
    # open notepad
    notepad()
    # wait
    time.sleep(gui_wait)
    # open file to read content
    with open(filepath, encoding='utf-8') as inp_file:
        # use generator with tqdm for progress visualization
        for line in tqdm(inp_file):
            HID.type_string(line)

    filename = os.path.basename(filepath)
    save_notepad(filename)
    if close:
        time.sleep(gui_wait)
        HID.press(bytes([HID.CODE.LEFT_ALT, 0, HID.CODE.F4, *[0] * 5]))
