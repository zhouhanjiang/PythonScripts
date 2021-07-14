#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: logger.py
# Author: zhouhanjiang@xunlei.com
# Create: 2021/03/19 11:28
# LastMod: 2021/04/25 16:30

"""
   logger.py
"""

import logging
import os
import sys
# import json

# 控制台日志输入颜色
from colorlog import ColoredFormatter
# 按文件大小滚动备份
# 解决多进程打印日志到同一个文件重命名冲突问题
# https://pypi.org/project/concurrent-log-handler/
from concurrent_log_handler import ConcurrentRotatingFileHandler

from DesignPattern.singleton import singleton
# import Utils.global_var as global_var

loggers = {}

log_dir = None
log_level = None
valid_log_level_list = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
valid_log_level_dict = {"NOTSET": 0, "DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40, "CRITICAL": 50}
valid_log_int_level_dict = {v: k for k, v in valid_log_level_dict.items()}


# https://docs.python.org/3/library/logging.html#levels
# CRITICAL>ERROR>WARNING>INFO>DEBUG>NOTSET
# https://zhuanlan.zhihu.com/p/93712428
def get_logger(name=None, file=None, level=None, log_to_file=False, log_file_max_bytes=1024 * 1024 * 10,
               log_file_backup_count=1):
    """
    :param name: 日志文件名,如果不传递就是使用当前文件名"__main__"
    :param file: 调用日志的文件完整路径,根据此路径设置日志目录(建议在主函数中传递该参数)
    :param level: 日志级别,进程级全局性的.建议在主函数中传递
    :param log_to_file: 日志是否写文件,文件级别.按需配置
    :param log_file_max_bytes: 最大单日志文件大小,按需配置
    :param log_file_backup_count: 最大日志备份数,按需配置
    :return: 单文件对应的日志logger对象
    """

    # 如果没有传递日志文件名参数,则取默认值
    if not name:
        name = __name__

    # 如果已经存在同名文件日志对象,直接返回
    if loggers.get(name):
        return loggers.get(name)

    # 如果不存在同名文件日志对象,新生成一个
    logger = logging.getLogger(name)
    # 日志级别,进程级全局唯一
    global log_level
    if not log_level:
        if not level:
            log_level = "INFO"
        else:
            level = str(level).strip().upper()
            global valid_log_level_list
            if level in valid_log_level_list:
                log_level = level
            else:
                log_level = "INFO"
    logger.setLevel(log_level)

    # 输出到控制台
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(level=log_level)
    # formatter = logging.Formatter(LOG_FORMAT)
    stream_handler.setFormatter(
        ColoredFormatter(
            "%(log_color)s%(asctime)s %(levelname)-4s%(reset)s %(filename)s - %(funcName)s - %(lineno)d: %(message)s")
    )
    # LOG_FORMAT = '%(asctime)s %(levelname)s %(filename)s - %(lineno)d :%(message)s'  # 每条日志输出格式
    logger.addHandler(stream_handler)

    # 输出到文件
    if log_to_file:
        # 日志目录,进程级全局唯一
        global log_dir
        if not log_dir:
            if not file:
                # 如果路径不存在，创建日志文件文件夹
                log_dir = os.path.abspath(__file__)
                log_dir = os.path.dirname(log_dir)
                log_dir = os.path.join(log_dir, "pythonlog")
            else:
                try:
                    # 如果路径不存在，创建日志文件文件夹
                    log_dir = os.path.abspath(file)
                    log_dir = os.path.dirname(log_dir)
                    log_dir = os.path.join(log_dir, "pythonlog")
                except Exception as e:
                    print(f"初始化log_dir失败,使用默认值{e}")
                    # 如果路径不存在，创建日志文件文件夹
                    log_dir = os.path.abspath(__file__)
                    log_dir = os.path.dirname(log_dir)
                    log_dir = os.path.join(log_dir, "pythonlog")

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # 添加 FileHandler
        abs_log_name = str(name).replace(os.sep, "-").replace("/", "-").replace("\\", "-").replace(":", "-")
        if abs_log_name.endswith(".py"):
            abs_log_name = abs_log_name[:-3]
        if abs_log_name.endswith(".pyi"):
            abs_log_name = abs_log_name[:-4]
        # dot_pos = abs_log_name.rfind(".")
        # if dot_pos>0:
        #     abs_log_name = abs_log_name[:dot_pos]
        if len(abs_log_name) > 100:
            abs_log_name = abs_log_name[len(abs_log_name) - 100:]
        log_path = os.path.join(log_dir, str(abs_log_name) + ".log")
        # file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler = ConcurrentRotatingFileHandler(filename=log_path, maxBytes=log_file_max_bytes,
                                                     backupCount=log_file_backup_count, encoding='utf8')
        file_handler.setLevel(level=log_level)
        file_handler.setFormatter(
            ColoredFormatter(
                "%(log_color)s%(asctime)s %(levelname)-4s%(reset)s "
                "%(filename)s - %(funcName)s - %(lineno)d: %(message)s")
        )
        logger.addHandler(file_handler)

    # 保存到进程级全局 loggers
    loggers[name] = logger
    return logger


# 设置特定logger句柄级别,仅供调试使用
def set_global_logger_level(logger_name="", level="INFO"):
    """
    :param logger_name:  待配置的logger句柄名称,局部匹配即可
    :param level: 待设置的logger句柄级别
    :return:
    """
    logger_flag = False

    try:
        for name, logger in loggers.items():
            level = str(level).strip().upper()
            global valid_log_level_list
            if level in valid_log_level_list:
                pass  # level = level
            else:
                level = "INFO"

            logger_name = str(logger_name).lower().strip()
            if logger_name == "":
                logger.setLevel(level)
                logger_handlers = logger.handlers
                for Logger_handler in logger_handlers:
                    Logger_handler.setLevel(level=level)
                loggers[name] = logger
            else:
                if str(name).lower().find(logger_name) >= 0:  # or str(logger_name).lower().find(name)>=0:
                    logger.setLevel(level)
                    logger_handlers = logger.handlers
                    for Logger_handler in logger_handlers:
                        Logger_handler.setLevel(level=level)
                    loggers[name] = logger

        logger_flag = True
        return logger_flag
    except Exception as msg:
        print("err,msg=" + str(msg))
        return logger_flag


@singleton
class Logger(object):
    """
        logger.py
    """

    def __init__(self):
        self._logger = logging.getLogger("autotest")
        self._logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(ColoredFormatter("%(log_color)s%(asctime)s %(levelname)-4s%(reset)s | %(log_color)s%("
                                              "message)s%(reset)s"))

        self._logger.addHandler(handler)

    def critical(self, msg, *args, **kwargs):
        """

        :param msg:
        :param args:
        :param kwargs:
        """

        self._logger.critical(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """

        :param msg:
        :param args:
        :param kwargs:
        """

        self._logger.error(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """

        :param msg:
        :param args:
        :param kwargs:
        """

        self._logger.warning(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """

        :param msg:
        :param args:
        :param kwargs:
        """

        self._logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """

        :param msg:
        :param args:
        :param kwargs:
        """

        self._logger.debug(msg, *args, **kwargs)

    def set_level(self, level="DEBUG"):
        """

        :param level:
        """

        level = str(level).strip().upper()
        if level == "CRITICAL":
            self._logger.setLevel(logging.CRITICAL)
        elif level == "ERROR":
            self._logger.setLevel(logging.ERROR)
        elif level == "WARNING":
            self._logger.setLevel(logging.WARNING)
        elif level == "INFO":
            self._logger.setLevel(logging.INFO)
        elif level == "DEBUG":
            self._logger.setLevel(logging.DEBUG)
        elif level == "NOTSET":
            self._logger.setLevel(logging.NOTSET)
        else:
            self._logger.setLevel(logging.DEBUG)


# 只打控制台日志,仅供内部调试用.日常打印日志推荐调用get_logger函数获取日志句柄
_logger = Logger()

if __name__ == '__main__':
    _logger.info("test")
