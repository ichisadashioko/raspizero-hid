#!/usr/bin/env python3
# Reference: https://wiki.osdev.org/USB_Human_Interface_Devices#Report_format
from __future__ import print_function
import os
import time


def compile_hid_report(m=0b00000000, r=0b00000000, k1=0b00000000, k2=0b00000000, k3=0b00000000, k4=0b00000000, k5=0b00000000, k6=0b00000000):
    """
    Write USB HID report.

    `m`: Modifier keys status. This byte is a bitfield, where each bit corresponds to a specific modifier key. When a bit is set to 1, the corresponding modifier key is being pressed. Unlike PS/2 keyboards, USB keyboards don't have "scancodes" for modifier keys.

    ```
    1st bit - Left Ctrl
    2nd bit - Left Shift
    3rd bit - Left Alt
    4th bit - Left GUI
    5th bit - Right Ctrl
    6th bit - Right Shift
    7th bit - Right Alt
    8th bit - Right GUI
    ```

    `r`: Reserved field.

    `k1`: Keypress #1

    `k2`: Keypress #2

    `k3`: Keypress #3

    `k4`: Keypress #4

    `k5`: Keypress #5

    `k6`: Keypress #6
    """
    return bytes([m, r, k1, k2, k3, k4, k5, k6])


keycode_dict = {
    'a': 0x4,
    'b': 0x5,
    'c': 0x6,
    'd': 0x7,
    'e': 0x8,
    'f': 0x9,
    'g': 0xa,
    'h': 0xb,
    'i': 0xc,
    'j': 0xd,
    'k': 0xe,
    'l': 0xf,
    'm': 0x10,
    'n': 0x11,
    'o': 0x12,
    'p': 0x13,
    'q': 0x14,
    'r': 0x15,
    's': 0x16,
    't': 0x17,
    'u': 0x18,
    'v': 0x19,
    'w': 0x1a,
    'x': 0x1b,
    'y': 0x1c,
    'z': 0x1d,
    '1': 0x1e,
    '2': 0x1f,
    '3': 0x20,
    '4': 0x21,
    '5': 0x22,
    '6': 0x23,
    '7': 0x24,
    '8': 0x25,
    '9': 0x26,
    '0': 0x27,
    'enter': 0x28,
    'esc': 0x29,
    'backspace': 0x2a,
    'tab': 0x2b,
    'space': 0x2c,
    '-': 0x2d,
    '=': 0x2e,
    '[': 0x2f,
    ']': 0x30,
    '\\': 0x31,
    ';': 0x33,
    '\'': 0x34,
    '`': 0x35,
    ',': 0x36,
    '.': 0x37,
    '/': 0x38,
    'capslock': 0x39,
    'f1': 0x3a,
    'f2': 0x3b,
    'f3': 0x3c,
    'f4': 0x3d,
    'f5': 0x3e,
    'f6': 0x3f,
    'f7': 0x40,
    'f8': 0x41,
    'f9': 0x42,
    'f10': 0x43,
    'f11': 0x44,
    'f12': 0x45,
}

modifier_dict = {
    'left_ctrl': 0b00000001,
    'left_shift': 0b00000010,
    'left_alt': 0b00000100,
    'left_gui': 0b00001000,
    'right_ctrl': 0b00010000,
    'right_shift': 0b00100000,
    'right_alt': 0b01000000,
    'right_gui': 0b10000000,
}
report_dict = {
    # 'gui r': compile_hid_report(m=modifier_dict['left_gui'], k1=keycode_dict['r']),
    # 'alt f4': compile_hid_report(m=modifier_dict['left_alt'], k1=keycode_dict['f1']),
    '\t': compile_hid_report(k1=keycode_dict['tab']),
    '\n': compile_hid_report(k1=keycode_dict['enter']),
    ' ': compile_hid_report(k1=keycode_dict['space']),

    '0': compile_hid_report(k1=keycode_dict['0']),
    '1': compile_hid_report(k1=keycode_dict['1']),
    '2': compile_hid_report(k1=keycode_dict['2']),
    '3': compile_hid_report(k1=keycode_dict['3']),
    '4': compile_hid_report(k1=keycode_dict['4']),
    '5': compile_hid_report(k1=keycode_dict['5']),
    '6': compile_hid_report(k1=keycode_dict['6']),
    '7': compile_hid_report(k1=keycode_dict['7']),
    '8': compile_hid_report(k1=keycode_dict['8']),
    '9': compile_hid_report(k1=keycode_dict['9']),
    '-': compile_hid_report(k1=keycode_dict['-']),
    '=': compile_hid_report(k1=keycode_dict['=']),
    '`': compile_hid_report(k1=keycode_dict['`']),
    ',': compile_hid_report(k1=keycode_dict[',']),
    '.': compile_hid_report(k1=keycode_dict['.']),
    '/': compile_hid_report(k1=keycode_dict['/']),
    ';': compile_hid_report(k1=keycode_dict[';']),
    '\'': compile_hid_report(k1=keycode_dict['\'']),
    '[': compile_hid_report(k1=keycode_dict['[']),
    ']': compile_hid_report(k1=keycode_dict[']']),
    '\\': compile_hid_report(k1=keycode_dict['\\']),

    '~': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['`']),
    '!': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['1']),
    '@': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['2']),
    '#': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['3']),
    '$': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['4']),
    '%': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['5']),
    '^': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['6']),
    '&': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['7']),
    '*': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['8']),
    '(': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['9']),
    ')': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['0']),
    '_': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['-']),
    '+': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['=']),
    '<': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict[',']),
    '>': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['.']),
    '?': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['/']),
    '{': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['[']),
    '}': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict[']']),
    ':': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict[';']),
    '"': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['\'']),
    '|': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['\\']),

    'a': compile_hid_report(k1=keycode_dict['a']),
    'b': compile_hid_report(k1=keycode_dict['b']),
    'c': compile_hid_report(k1=keycode_dict['c']),
    'd': compile_hid_report(k1=keycode_dict['d']),
    'e': compile_hid_report(k1=keycode_dict['e']),
    'f': compile_hid_report(k1=keycode_dict['f']),
    'g': compile_hid_report(k1=keycode_dict['g']),
    'h': compile_hid_report(k1=keycode_dict['h']),
    'i': compile_hid_report(k1=keycode_dict['i']),
    'j': compile_hid_report(k1=keycode_dict['j']),
    'k': compile_hid_report(k1=keycode_dict['k']),
    'l': compile_hid_report(k1=keycode_dict['l']),
    'm': compile_hid_report(k1=keycode_dict['m']),
    'n': compile_hid_report(k1=keycode_dict['n']),
    'o': compile_hid_report(k1=keycode_dict['o']),
    'p': compile_hid_report(k1=keycode_dict['p']),
    'q': compile_hid_report(k1=keycode_dict['q']),
    'r': compile_hid_report(k1=keycode_dict['r']),
    's': compile_hid_report(k1=keycode_dict['s']),
    't': compile_hid_report(k1=keycode_dict['t']),
    'u': compile_hid_report(k1=keycode_dict['u']),
    'v': compile_hid_report(k1=keycode_dict['v']),
    'w': compile_hid_report(k1=keycode_dict['w']),
    'x': compile_hid_report(k1=keycode_dict['x']),
    'y': compile_hid_report(k1=keycode_dict['y']),
    'z': compile_hid_report(k1=keycode_dict['z']),

    'A': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['a']),
    'B': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['b']),
    'C': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['c']),
    'D': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['d']),
    'E': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['e']),
    'F': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['f']),
    'G': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['g']),
    'H': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['h']),
    'I': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['i']),
    'J': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['j']),
    'K': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['k']),
    'L': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['l']),
    'M': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['m']),
    'N': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['n']),
    'O': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['o']),
    'P': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['p']),
    'Q': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['q']),
    'R': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['r']),
    'S': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['s']),
    'T': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['t']),
    'U': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['u']),
    'V': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['v']),
    'W': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['w']),
    'X': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['x']),
    'Y': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['y']),
    'Z': compile_hid_report(m=modifier_dict['left_shift'], k1=keycode_dict['z']),
}


def write_report(report: bytes):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)
        fd.write(compile_hid_report())


def write_reports(reports: list):
    with open('/dev/hidg0', 'rb+') as fd:
        for report in reports:
            fd.write(report)
            fd.write(compile_hid_report())


def hid_type(x: str):
    reports = [report_dict[c] for c in x]
    write_reports(reports)


if __name__ == "__main__":
    # single_key = '-=`,./;\'[]\\'
    # for c in single_key:
    #     print(f'\'{c}\': compile_hid_report(k1=keycode_dict[\'{c}\']),')

    # shift_chars = '~!@#$%^&*()_+<>?{}:"|'
    # for c in shift_chars:
    #     print(f'\'{c}\': compile_hid_report(m=modifier_dict[\'left_shift\'], k1=keycode_dict[\'{c}\']),')

    open_run = compile_hid_report(m=modifier_dict['left_gui'], k1=keycode_dict['r'])
    write_report(open_run)
    time.sleep(0.1)

    hid_type('cmd\n')

    time.sleep(0.05)
    hid_type('notepad\n')

    lines = open(os.path.basename(__file__)).readlines()
    lines = ''.join(lines)

    write_report(compile_hid_report(k1=keycode_dict['f5']))

    hid_type('\n')

    hid_type(lines)

    hid_type('\n')

    write_report(compile_hid_report(k1=keycode_dict['f5']))
