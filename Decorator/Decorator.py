#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: decorator.py
# Author: zhouhanjiang@xunlei.com
# Create: 2021/07/14 10:03
# LastMod: 2021/07/14 10:03

"""
    decorator.py
"""

from __future__ import division

# @wraps 接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性
# 保留函数的名字和注释文档(docstring)
from functools import wraps

'''
__Author__:zhouhanjiang
学习Python中装饰器
https://www.runoob.com/w3cnote/python-func-decorators.html
'''

import os
# import time

from Utils.logger import get_logger

logger = get_logger(
    os.path.basename(os.path.abspath(__file__)),
    os.path.abspath(__file__),
    level="INFO",
    log_file_max_bytes=1024 * 1024)


# import builtins as __builtin__


def print(*args, **kwargs):
    """
        overwrite print
    """
    # My custom print() function.
    # Adding new arguments to the print function signature
    # is probably a bad idea.
    # Instead consider testing if custom argument keywords
    # are present in kwargs
    # __builtin__.print('My overridden print() function!')
    # return __builtin__.print(*args, **kwargs)
    return logger.info(*args, **kwargs)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# an example of multiple python decorator
def deco1_with_wrapper(func):
    """
       deco1_with_wrapper
    """
    print("step1.deco1_with_wrapper start")
    print("in deco1_with_wrapper.func.__name__=" + str(func.__name__))

    @wraps(func)
    def deco_with_wrapper_innder(*args, **kwargs):
        """
           deco_with_wrapper_innder
        """
        print("step2.deco_with_wrapper_innder start")
        print("in deco_with_wrapper_innder.func.__name__=" + str(func.__name__))
        print("in deco_with_wrapper_innder.args=" + str(args) + ";*kwargs=" + str(*kwargs))
        result1 = func(*args, **kwargs)
        print("in deco_with_wrapper_innder.result=" + str(result1))
        print("step3.deco_with_wrapper_innder end")
        return result1

    print("step4.deco1_with_wrapper end")
    return deco_with_wrapper_innder


def deco2_without_wrapper(func):
    """
        deco2_without_wrapper
    """
    print("step5.deco2_without_wrapper start")
    print("in deco2_without_wrapper.func.__name__=" + str(func.__name__))

    # @wraps(func)
    def deco_without_wrapper_innder(*args, **kwargs):
        """
          deco_without_wrapper_innder
        """
        print("step6.deco_without_wrapper_innder start")
        print("in deco_without_wrapper_innder.func.__name__=" + str(func.__name__))
        print("in deco_without_wrapper_innder.args=" + str(args) + ";*kwargs=" + str(*kwargs))
        result2 = func(*args, **kwargs)
        print("in deco_without_wrapper_innder.result=" + str(result2))
        print("step7.deco_without_wrapper_innder end")
        return result2

    print("step8.deco2_without_wrapper end")
    return deco_without_wrapper_innder


def deco3_para_without_wrapper(deco_para="deco3_para"):
    """
        deco3_para_without_wrapper
    """
    print("step9.deco3_para_without_wrapper start")
    print("in deco3_para_without_wrapper.deco_para=" + str(deco_para))

    def deco3_innder(func):
        """
           deco3_innder
        """
        print("in deco3_innder.func.__name__=" + str(func.__name__))

        # @wraps(func)
        def deco3_para_without_wrapper_innder(*args, **kwargs):
            """
                deco3_para_without_wrapper_innder
            """
            print("step10.deco3_para_without_wrapper_innder start")
            print("in deco3_para_without_wrapper_innder.func.__name__=" + str(func.__name__))
            print("in deco3_para_without_wrapper_innder.deco_para=" + str(deco_para))
            print("in deco3_para_without_wrapper_innder.args=" + str(args) + ";*kwargs=" + str(*kwargs))
            result3 = func(*args, **kwargs)
            print("in deco3_para_without_wrapper_innder.result=" + str(result3))
            print("step11.deco3_para_without_wrapper_innder end")
            return result3

        return deco3_para_without_wrapper_innder

    print("step12.deco3_para_without_wrapper end")
    return deco3_innder


@deco3_para_without_wrapper("deco3_para_test")
@deco1_with_wrapper
@deco2_without_wrapper
def multi_deco_test_with_return(*args, **kwargs):
    """
       multi_deco_test_with_return
    """
    print('multi_deco_test called')
    print(kwargs)
    return args


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


def decorator_test():
    """
        decorator_test
    """
    multi_deco_test_result = multi_deco_test_with_return("args_para1", "args_para2", kwargs_key="kwargs_value")
    print("multi_deco_test_result=" + str(multi_deco_test_result))
    '''
    output:

    step9.deco3_para_without_wrapper start
    in deco3_para_without_wrapper.deco_para=deco3_para_test
    step12.deco3_para_without_wrapper end
    step5.deco2_without_wrapper start
    in deco2_without_wrapper.func.__name__=multi_deco_test_with_return
    step8.deco2_without_wrapper end
    step1.deco1_with_wrapper start
    in deco1_with_wrapper.func.__name__=deco_without_wrapper_innder
    step4.deco1_with_wrapper end
    in deco3.func.__name__=deco_without_wrapper_innder
    step10.deco3_para_without_wrapper_innder start
    in deco3_para_without_wrapper_innder.func.__name__=deco_without_wrapper_innder
    in deco3_para_without_wrapper_innder.deco_para=deco3_para_test
    in deco3_para_without_wrapper_innder.args=('args_para1', 'args_para2');*kwargs=kwargs_key
    step2.deco_with_wrapper_innder start
    in deco_with_wrapper_innder.func.__name__=deco_without_wrapper_innder
    in deco_with_wrapper_innder.args=('args_para1', 'args_para2');*kwargs=kwargs_key
    step6.deco_without_wrapper_innder start
    in deco_without_wrapper_innder.func.__name__=multi_deco_test_with_return
    in deco_without_wrapper_innder.args=('args_para1', 'args_para2');*kwargs=kwargs_key
    multi_deco_test called
    in deco_without_wrapper_innder.result=('args_para1', 'args_para2')
    step7.deco_without_wrapper_innder end
    in deco_with_wrapper_innder.result=('args_para1', 'args_para2')
    step3.deco_with_wrapper_innder end
    in deco3_para_without_wrapper_innder.result=('args_para1', 'args_para2')
    step11.deco3_para_without_wrapper_innder end
    multi_deco_test_result=('args_para1', 'args_para2')
    '''


if __name__ == '__main__':
    decorator_test()
