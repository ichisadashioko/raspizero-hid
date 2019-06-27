# encoding=utf-8
import os
import time
import argparse

import hid_utils

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', description='input file path', type=str, default=__file__)

    args = parser.parse_args()

    gui_wait = 1.0  # sec

    hid_utils.open_run()
    time.sleep(gui_wait)
    hid_utils.hid_type('notepad\n')
    time.sleep(gui_wait)

    encode_start = time.time()
    pay_load_info = hid_utils.encode_file_to_payload(args.i)
    encode_time = time.time() - encode_start

    payload_fname = pay_load_info['out_fname']
    chars_count = pay_load_info['chars_count']
    skip_count = pay_load_info['skip_count']
    reports_count = pay_load_info['reports_count']

    inject_start = time.time()
    hid_utils.inject_payload(payload_fname)
    inject_time = time.time() - inject_start

    char_type_speed = inject_time / (chars_count - skip_count)
    type_speed = inject_time / reports_count

    print('encode_time: {:.4f}'.format(encode_time))
    print('inject_time: {:.4f}'.format(inject_time))
    print('char_type_speed: {:.2f}'.format(char_type_speed))
    print('type_speed: {:.2f}'.format(type_speed))
