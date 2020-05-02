# encoding=utf-8
# plug Raspberry Pi Zero into a Windows PC with cygwin installed.
# put your cursor in the cygwin terminal
# SSH into Raspberry Pi Zero
# execute this script
# - this script will open vi in cygwin terminal
# - read file content and type them into vi then save the file
import os
import re
import time
import argparse

import HID
import HID.utils.windows.cygwin as cygwin

file_types = [
    #'.txt',
    '.java',
    # '.html',
    '.css',
    '.js',
    '.jsp',
    '.sql',
    '.svg',
    '.base64',
    #'.py',
    '.xml',
]
ignore_files = [
    'build',
    'test',
    '__pycache__',
    '.pyc',
    '.git',
    '.md',
    'nbproject',
]


def inject_file(path):
    assert os.path.exists(path)

    if os.path.isdir(path):
        file_list = os.listdir(path)
        for filename in file_list:
            filepath = '{}/{}'.format(path, filename)

            if True in (ignore_file in filepath for ignore_file in ignore_files):
                continue

            inject_file(filepath)
    else:
        basename, ext = os.path.splitext(path)
        if ext in file_types:
            print(path)
            cygwin.type_file_to_vim(
                path, 
                where='/cygdrive/c/Users/"$USER"/Downloads',
            )
            time.sleep(0.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', type=str, default='.', help='input file')

    args = parser.parse_args()

    inp_filepath = args.input

    print('Injecting {}'.format(inp_filepath))

    try:
        start = time.time()
        inject_file(inp_filepath)
        inj_time = time.time() - start
        print('Total inject time: {:.2f} sec'.format(inj_time))
    except KeyboardInterrupt:
        HID.press(HID.REPORTS.RELEASE)
        time.sleep(1.0)
