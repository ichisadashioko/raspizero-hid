# encoding=utf-8
import os
import time
import argparse

import HID.utils.windows

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, default=__file__, help='input file')

    args = parser.parse_args()

    inp_filepath = args.i

    HID.utils.windows.type_file_to_notepad(inp_filepath, close=False)
