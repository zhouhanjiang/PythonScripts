#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: singleton.py
# Author: zhouhanjiang@xunlei.com
# Create: 2021/03/19 11:28
# LastMod: 2021/03/19 14:33

"""
   singleton.py
"""


def singleton(cls):
    """

    :param cls:
    :return:
    """

    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


if __name__ == "main":
    pass
