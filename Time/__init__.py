#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: __init__.py
# Author: zhouhanjiang@xunlei.com
# Create: 2021/07/14 10:03
# LastMod: 2021/07/14 10:03

"""
    __init__.py
"""

# https://stackoverflow.com/questions/550470/overload-print-python
from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string,
# Python comments, other future statements, or blank lines before the __future__ line.


import os
from Utils.logger import get_logger

logger = get_logger(
    os.path.basename(os.path.abspath(__file__)),
    os.path.abspath(__file__),
    level="INFO",
    log_file_max_bytes=1024 * 1024)

# import builtins as __builtin__


def print(*args, **kwargs):
    """My custom print() function."""
    # Adding new arguments to the print function signature
    # is probably a bad idea.
    # Instead consider testing if custom argument keywords
    # are present in kwargs
    # __builtin__.print('My overridden print() function!')
    # return __builtin__.print(*args, **kwargs)
    return logger.info(*args, **kwargs)


if __name__ == "main":
    pass
