#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: __init__.py
# Author: zhouhanjiang@xunlei.com
# Create: 2021/07/14 10:03
# LastMod: 2021/07/14 10:03

"""
        __init__.py
"""

import os
import time

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


class RestartMyself:
    """
        RestartMyself
    """
    def __init__(self):
        self.pid = -1

    def __del__(self):
        pass

    def restart_if_changed(self):
        """
            restart_if_changed
            https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/
        """
        # Check if the file has changed.
        # If so, restart the application.
        import sys
        last_mtime = os.path.getmtime(__file__)

        old_pid = os.getpid()
        self.pid = old_pid
        print("old_pid=" + str(old_pid))

        while True:
            if os.path.getmtime(__file__) > last_mtime:
                print('file has changed => restarting')

                # Restart the application (os.execv() does not return).
                # os.execv(__file__, sys.argv)
                os.execv(sys.executable, ['python'] + sys.argv)

                # 下面的语句不会执行到,因为已经重新启动一个新的进程了
                new_pid = os.getpid()
                self.pid = new_pid
                print("new_pid=" + str(new_pid))

                break
            else:
                print('file not changed')
                time.sleep(5)

    # 不断重启程序(外部)
    def restart_myself(self, repeat_time=1, interval=30):
        """
           restart_myself
        """
        restart_myself_flag = False
        try:
            import time
            import os
            import sys
            print("repeat_time=" + str(repeat_time))
            print("interval=" + str(interval))

            for repeat_index in range(repeat_time):
                print("repeat_index=" + str(repeat_index))
                old_pid = os.getpid()
                self.pid = old_pid
                print("old_pid=" + str(old_pid))
                time.sleep(interval)
                # python = sys.executable
                # os.execl(python, python, * sys.argv)
                # https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself
                os.execv(sys.executable, ['python'] + sys.argv)

                # 下面的语句不会执行到,因为已经重新启动一个新的进程了
                new_pid = os.getpid()
                self.pid = new_pid
                print("new_pid=" + str(new_pid))

            restart_myself_flag = True
            print("restart_myself_flag=" + str(restart_myself_flag))
            return restart_myself_flag

        except Exception as msg:
            logger.warning("err,msg=" + str(msg))
            return restart_myself_flag


if __name__ == '__main__':
    # 极容易导致死循环,慎用(建议重启间隔不小于30S,以便外部终止)
    restart_myself_cls = RestartMyself()
    # restart_myself_cls.restart_myself()
    restart_myself_cls.restart_if_changed()
