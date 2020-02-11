#!/usr/bin/python
# -*- coding: utf-8 -*-


from __future__ import division

from functools import wraps

'''
__Author__:zhouhanjiang
学习Python中装饰器
'''


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# an example of multiple python decorator
def deco1(func):
    print("step1.deco1 start")
    print("in deco1.func.__name__=" + str(func.__name__))
    @wraps(func)
    def wrapper1(*args,**kwargs):
        print("step2.wrapper1 start")
        print("in wrapper1.func.__name__=" + str(func.__name__))
        print("in wrapper1.args=" + str(args) + ";*kwargs=" + str(*kwargs))
        result1 = func(*args, **kwargs)
        print("in wrapper1.result=" + str(result1))
        print("step3.wrapper1 end")
        return result1
    print("step4.deco1 end")
    return wrapper1

def deco2(func):
    print("step5.deco2 start")
    print("in deco2.func.__name__=" + str(func.__name__))
    #@wraps(func)
    def wrapper2(*args,**kwargs):
        print("step6.wrapper2 start")
        print("in wrapper2.func.__name__=" + str(func.__name__))
        print("in wrapper2.args=" + str(args) + ";*kwargs=" + str(*kwargs))
        result2 = func(*args,**kwargs)
        print("in wrapper2.result=" + str(result2))
        print("step7.wrapper2 end")
        return result2
    print("step8.deco2 end")
    return wrapper2

def deco3_with_para(deco_para="deco3_para"):
    print("step9.deco3_with_para start")
    print("in deco3_with_para.deco_para=" + str(deco_para))
    def deco3(func):
      print("in deco3.func.__name__=" + str(func.__name__))
      #@wraps(func)
      def wrapper3(*args,**kwargs):
        print("step10.wrapper3 start")
        print("in wrapper3.func.__name__=" + str(func.__name__))
        print("in wrapper3.deco_para=" + str(deco_para))
        print("in wrapper3.args="+str(args)+";*kwargs="+str(*kwargs))
        result3 = func(*args,**kwargs)
        print("in wrapper3.result="+str(result3))
        print("step11.wrapper3 end")
        return result3
      return wrapper3

    print("step12.deco3_with_para end")
    return deco3


@deco3_with_para("deco3_para_test")
@deco1
@deco2
def multi_deco_test_with_return(*args,**kwargs):
    print('multi_deco_test called')
    return args


#multi_deco_test_result = multi_deco_test_with_return("args_para1","args_para2",kwargs_key="kwargs_value")
#print("multi_deco_test_result="+str(multi_deco_test_result))
'''
output:

step9.deco3_with_para start
in deco3_with_para.deco_para=deco3_para_test
step12.deco3_with_para end
step5.deco2 start
in deco2.func.__name__=multi_deco_test_with_return
step8.deco2 end
step1.deco1 start
in deco1.func.__name__=wrapper2
step4.deco1 end
in deco3.func.__name__=wrapper2
step10.wrapper3 start
in wrapper3.func.__name__=wrapper2
in wrapper3.deco_para=deco3_para_test
in wrapper3.args=('args_para1', 'args_para2');*kwargs=kwargs_key
step2.wrapper1 start
in wrapper1.func.__name__=wrapper2
in wrapper1.args=('args_para1', 'args_para2');*kwargs=kwargs_key
step6.wrapper2 start
in wrapper2.func.__name__=multi_deco_test_with_return
in wrapper2.args=('args_para1', 'args_para2');*kwargs=kwargs_key
multi_deco_test called
in wrapper2.result=('args_para1', 'args_para2')
step7.wrapper2 end
in wrapper1.result=('args_para1', 'args_para2')
step3.wrapper1 end
in wrapper3.result=('args_para1', 'args_para2')
step11.wrapper3 end
multi_deco_test_result=('args_para1', 'args_para2')
'''
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


def Decorator_Test():
  pass


if __name__ == '__main__':
    Decorator_Test()
