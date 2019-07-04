# encoding=utf-8
import os
import time
import re

def line_count(path):
    assert os.path.exists(path)

    num_lines = 0
    with open(path) as f:
        for line in f:
            num_lines += 1
    
    return num_lines