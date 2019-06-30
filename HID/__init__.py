# encoding=utf-8
from HID.REPORTS import CHARS, RELEASE

HID_FILENAME = '/dev/hidg0'


def type_string(s):
    out_file = open(HID_FILENAME, mode='rb+')
    for c in s:
        if c in CHARS.keys():
            out_file.write(CHARS[c])
            out_file.write(RELEASE)
            #out_file.flush()
    out_file.close()


def press(inp_rpt: bytes, release=True):
    with open(HID_FILENAME, mode='rb+') as out_file:
        out_file.write(inp_rpt)
        if release:
            out_file.write(RELEASE)
