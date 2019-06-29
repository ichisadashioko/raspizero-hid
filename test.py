# encoding=utf-8
import os
import time
import argparse

import hid_utils

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, default=__file__)

    args = parser.parse_args()

    gui_wait = 1.0  # sec

    hid_utils.open_run()
    time.sleep(gui_wait)
    hid_utils.hid_type('notepad\n')
    # time.sleep(gui_wait)

    encode_start = time.time()
    pay_load_info = hid_utils.encode_file(args.i)
    encode_time = time.time() - encode_start

    payload_fname = pay_load_info['out_fname']
    chars_count = pay_load_info['chars_count']
    skip_count = pay_load_info['skip_count']
    reports_count = pay_load_info['reports_count']

    inject_start = time.time()
    hid_utils.inject_payload(payload_fname)
    inject_time = time.time() - inject_start

    char_type_speed = (chars_count - skip_count) / inject_time
    type_speed = reports_count / inject_time

    print('encode_time: {:.4f} sec'.format(encode_time))
    print('inject_time: {:.4f} sec'.format(inject_time))
    print('char_type_speed: {:.2f} chars/sec'.format(char_type_speed))
    print('type_speed: {:.2f} keys/sec (include release action)'.format(type_speed))
    print(pay_load_info)
