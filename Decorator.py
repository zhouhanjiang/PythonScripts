#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import division

'''
__Author__:zhouhanjiang
学习Python中装饰器
'''


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# an example of multiple python decorator
def deco1(func):
    print("step1.deco1 start")
    def wrapper1():
        print("step2.wrapper1 start")
        func()
        print("step3.wrapper1 end")
    print(4)
    print("step4.deco1 end")
    return wrapper1

def deco2(func):
    print("step5.deco2 start")
    def wrapper2():
        print(6)
        print("step6.wrapper2 start")
        func()
        print("step7.wrapper2 end")
    print("step8.deco2 end")
    return wrapper2

@deco1
@deco2
def multi_deco_test():
    print('multi_deco_test')


#multi_deco_test()
'''
output:
step5.deco2 start
step8.deco2 end
step1.deco1 start
4
step4.deco1 end
step2.wrapper1 start
6
step6.wrapper2 start
multi_deco_test
step7.wrapper2 end
step3.wrapper1 end

'''
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


def Decorator_Test():
  pass


if __name__ == '__main__':
    Decorator_Test()
