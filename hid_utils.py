#!/usr/bin/env python3
# Reference: https://wiki.osdev.org/USB_Human_Interface_Devices#Report_format
from __future__ import print_function
import os
import time

HID_FILENAME = '/dev/hidg0'
RELEASE_REPORT = bytes([0x00] * 8)


def compile_hid_report(m=0b00000000, k1=0x00, k2=0x00, k3=0x00, k4=0x00, k5=0x00, k6=0x00):
    """
    A HID report should have 8 bytes (although shorthand report is available, it is buggy and has un-expected behaviour).

    The first byte is for modifiers. 
    Each bit for each key (Left Ctrl, Left Shift, Left Alt, Left GUI, Right Ctrl, Right Shift, Right Alt, Right GUI).
    Read the reference for more details.

    The second byte is a reversed byte.

    The remain 6 bytes is for `KEY_CODE`. `KEY_CODE` is NOT ASCII.
    """
    REVERSED_FIELD = 0x00
    return bytes([m, REVERSED_FIELD, k1, k2, k3, k4, k5, k6])


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

# the HID keycode to be set in `k1` to `k6`
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
    'delete': 0x4c,
}


# some single, common key / character HID reports
report_dict = {
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

shifted_chars = {
    '~': keycode_dict['`'],
    '!': keycode_dict['1'],
    '@': keycode_dict['2'],
    '#': keycode_dict['3'],
    '$': keycode_dict['4'],
    '%': keycode_dict['5'],
    '^': keycode_dict['6'],
    '&': keycode_dict['7'],
    '*': keycode_dict['8'],
    '(': keycode_dict['9'],
    ')': keycode_dict['0'],
    '_': keycode_dict['-'],
    '+': keycode_dict['='],
    '<': keycode_dict[','],
    '>': keycode_dict['.'],
    '?': keycode_dict['/'],
    '{': keycode_dict['['],
    '}': keycode_dict[']'],
    ':': keycode_dict[';'],
    '"': keycode_dict['\''],
    '|': keycode_dict['\\'],
    'A': keycode_dict['a'],
    'B': keycode_dict['b'],
    'C': keycode_dict['c'],
    'D': keycode_dict['d'],
    'E': keycode_dict['e'],
    'F': keycode_dict['f'],
    'G': keycode_dict['g'],
    'H': keycode_dict['h'],
    'I': keycode_dict['i'],
    'J': keycode_dict['j'],
    'K': keycode_dict['k'],
    'L': keycode_dict['l'],
    'M': keycode_dict['m'],
    'N': keycode_dict['n'],
    'O': keycode_dict['o'],
    'P': keycode_dict['p'],
    'Q': keycode_dict['q'],
    'R': keycode_dict['r'],
    'S': keycode_dict['s'],
    'T': keycode_dict['t'],
    'U': keycode_dict['u'],
    'V': keycode_dict['v'],
    'W': keycode_dict['w'],
    'X': keycode_dict['x'],
    'Y': keycode_dict['y'],
    'Z': keycode_dict['z'],
}


def write_report(report: bytes):
    """Press and release key(s)"""
    # Press keys means to write 8 bytes report to a file. In this case is `/dev/hidg0`.
    # Release keys mean to write 8 bytes report (all bytes are 0s) to `/dev/hidg0`
    global HID_FILENAME
    with open(HID_FILENAME, 'rb+') as fd:
        fd.write(report)
        fd.write(compile_hid_report())


def write_reports(reports: list):
    global HID_FILENAME
    with open(HID_FILENAME, 'rb+') as fd:
        for report in reports:
            fd.write(report)
            fd.write(compile_hid_report())


def hid_type(x: str):
    # Loop through every character in the string
    # and generate the HID report for each character
    # then pass the list to `write_reports`
    reports = [report_dict[c] for c in x]
    write_reports(reports)


def open_run():
    # open Windows Run
    write_report(compile_hid_report(m=modifier_dict['left_gui'], k1=keycode_dict['r']))


def close_windows():
    write_report(compile_hid_report(m=modifier_dict['left_alt'], k1=keycode_dict['f4']))


def encode_file_to_payload(filepath):
    if not os.path.exists(filepath):
        print('[encode_file_to_payload]', filepath, 'does not exist!')
        return

    # stats (info)
    chars_count = 0
    skip_count = 0
    hid_reports_count = 0

    out_fname = os.path.basename(filepath) + '.HID'

    with open(filepath, mode='r', encoding='utf-8') as inp_file, open(out_fname, mode='wb') as out_file:
        # stack keys together to increase bandwidth (precision of key order is not tested)
        key_stack = []
        # 6 is the maximum of keys can be contained in a HID report (exclude modifiers (Ctrl, Shift, Alt, GUI))
        max_key_stack = 6
        # can only stack either with or without modifiers in the HID report
        have_modifiers = None
        modifiers = 0b01000000  # Left Shift

        def key_stack_to_file():
            """Write `key_stack` as HID report followed by a `RELEASE_REPORT`"""
            nonlocal key_stack, modifiers, have_modifiers, out_file, hid_reports_count

            if len(key_stack) == 0:
                return

            # generate dictionary for arguments mapping
            key_args = {'k{}'.format(idx + 1): key_code for idx, key_code in enumerate(key_stack)}

            if not have_modifiers:
                # write HID report for key stack without modifiers
                # `**key_args` will unpack every element in the dict as arguments for the function
                out_file.write(compile_hid_report(m=0x00, **key_args))
            else:
                out_file.write(compile_hid_report(m=modifiers, **key_args))

            out_file.write(RELEASE_REPORT)
            key_stack = []

            hid_reports_count += 2

        last_char = None
        for line in inp_file:
            chars_count += len(line)
            for c in line:
                if c == last_char:
                    key_stack_to_file()

                if len(key_stack) == max_key_stack:
                    key_stack_to_file()
                    have_modifiers = None

                if c in keycode_dict.keys():
                    if have_modifiers:
                        key_stack_to_file()
                        have_modifiers = False

                    key_stack.append(keycode_dict[c])
                elif c in shifted_chars.keys():
                    if not have_modifiers:
                        key_stack_to_file()
                        have_modifiers = True

                    key_stack.append(shifted_chars[c])
                else:
                    skip_count += 1
                    continue

                last_char = c

    info = {
        'out_fname': out_fname,
        'chars_count': chars_count,
        'skip_count': skip_count,
        'reports_count': hid_reports_count,
    }

    return info


def inject_payload(filepath, throttle=0):
    if not os.path.exists(filepath):
        print('[inject_payload]', filepath, 'does not exist!')
        return

    # write 16 bytes at a time as the encoded HID report is followed by a `RELEASE_REPORT`
    num_bytes = 16
    with open(HID_FILENAME, mode='rb+') as hid_stream, open(filepath, mode='rb') as inp_file:
        bs = inp_file.read(num_bytes)
        while bs != b'':
            hid_stream.write(bs)
            bs = inp_file.read(num_bytes)

            if throttle > 0:
                time.sleep(throttle)
