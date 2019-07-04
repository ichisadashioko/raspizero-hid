# encoding=utf-8
import os
import re
import time
import argparse

import HID
import HID.utils.windows

def normalize_filename(path: str):
    return re.sub(r'[/\\]', '[_]', path)

file_types = [
    '.java',
    # '.html',
    '.css',
    '.js',
    '.jsp',
    '.sql',
    '.svg',
    # '.base64',
    '.py',
]
ignore_files = [
    'build',
    'test',
    '__pycache__',
    '.pyc',
]


def inject_file(path):
    assert os.path.exists(path)

    if os.path.isdir(path):
        file_list = os.listdir(path)
        for filename in file_list:
            filepath = f'{path}/{filename}'

            if True in (ignore_file in filepath for ignore_file in ignore_files):
                continue

            inject_file(filepath)
    else:
        basename, ext = os.path.splitext(path)
        if ext in file_types:
            filename = normalize_filename(path)
            print(filename)
            HID.utils.windows.type_file_to_notepad(path, filename=filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, default='.', help='input file')

    args = parser.parse_args()

    inp_filepath = args.i

    inject_file(inp_filepath)